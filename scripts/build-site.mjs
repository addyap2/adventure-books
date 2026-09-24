// Builds the static site into dist/: the reader, every episode, the shared lexicon,
// and a manifest the reader uses to list episodes. No framework, no dependencies.
import { readdir, readFile, writeFile, mkdir, cp, rm } from "node:fs/promises";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname;

// scan for per-section art the team has added: images/<series>/ep-NN/<id>.webp
import { existsSync } from "node:fs";
async function scanImages(series, episode) {
  const dir = join(ROOT, "images", series, `ep-${String(episode).padStart(2,"0")}`);
  if (!existsSync(dir)) return [];
  const files = await readdir(dir);
  return files.filter(f => /\.(webp|avif|png|jpe?g)$/i.test(f)).map(f => f.replace(/\.[^.]+$/, ""));
}

const CONTENT = join(ROOT, "content");
const DIST = join(ROOT, "dist");

await rm(DIST, { recursive: true, force: true });
await mkdir(DIST, { recursive: true });
// English Reading Adventures: the library is the root; each book has its own page; the reader app is /read.html
await cp(join(ROOT, "web", "library.html"), join(DIST, "index.html"));    // / — the English Reading Adventures library (cards from manifest)
await cp(join(ROOT, "web", "index.html"), join(DIST, "read.html"));       // the reader app
await cp(join(ROOT, "web", "favicon.svg"), join(DIST, "favicon.svg"));
// social cards (og-<slug>.png) and wordless library-card covers (cover-<slug>.png),
// both generated locally by build_og.mjs
for (const f of await readdir(join(ROOT, "web"))) {
  if (/^(og|cover).*\.png$/.test(f)) await cp(join(ROOT, "web", f), join(DIST, f));
}
// copy the art folder if the team has added any images
try { await cp(join(ROOT, "images"), join(DIST, "images"), { recursive: true }); console.log("Copied images/"); } catch { /* no images yet — placeholders show */ }
// copy the coverage dictionaries (dict/<lang>.json), lazy-loaded per language by the reader
try { await cp(join(CONTENT, "dict"), join(DIST, "dict"), { recursive: true }); console.log("Copied dict/"); } catch { /* no coverage dict yet */ }
// copy the per-passage gists (gist/<lang>.json), the on-demand "meaning" fallback
try { await cp(join(CONTENT, "gist"), join(DIST, "gist"), { recursive: true }); console.log("Copied gist/"); } catch { /* no gists yet */ }

const files = (await readdir(CONTENT)).filter(f => f.endsWith(".json"));
const episodes = [];

for (const f of files) {
  const raw = await readFile(join(CONTENT, f), "utf8");
  const json = JSON.parse(raw);
  await writeFile(join(DIST, f), raw);
  if (!json.nodes) continue;                       // the lexicon, not an episode
  episodes.push({
    file: f,
    slug: json.slug ?? f.replace(/\.json$/, ""),
    episode: json.episode ?? 0,
    series: json.series ?? "",
    title: json.title ?? f,
    blurb: json.blurb ?? "",
    levels: json.levels ?? [],
    identity: json.identity ?? null,          // palette + cover, so the library card can skin itself
    paragraphs: json.nodes.length,
    endings: json.nodes.filter(n => n.ending).length,
    images: await scanImages(json.series, json.episode),
  });
}
episodes.sort((a, b) => a.episode - b.episode);

const manifest = {
  series: episodes[0]?.file ? JSON.parse(await readFile(join(CONTENT, episodes[0].file), "utf8")).series : "",
  lexicon: "lexicon.json",
  episodes,
};
await writeFile(join(DIST, "manifest.json"), JSON.stringify(manifest, null, 2));

// Prerender one static page per book at dist/b/<slug>.html from the book.html template,
// stamping per-book meta (title, description, canonical, OG/Twitter, og-<slug>.png) so
// each book has its own correct social card and SEO — then the client JS hydrates it.
const BASE = "https://adventure-books-five.vercel.app";
const tmpl = await readFile(join(ROOT, "web", "book.html"), "utf8");
const attr = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
await mkdir(join(DIST, "b"), { recursive: true });
for (const e of episodes) {
  const desc = e.blurb || "An interactive story for English learners — you choose what happens.";
  const url = `${BASE}/b/${e.slug}`;
  const og = `${BASE}/og-${e.slug}.png`;
  const html = tmpl
    .replace(/<title>[\s\S]*?<\/title>/, `<title>${attr(e.title)} — an interactive story</title>`)
    .replace(/(<meta name="description" content=")[^"]*(">)/, `$1${attr(desc)}$2`)
    .replace(/(<link rel="canonical" href=")[^"]*(">)/, `$1${url}$2`)
    .replace(/(<meta property="og:url" content=")[^"]*(">)/, `$1${url}$2`)
    .replace(/(<meta property="og:title" content=")[^"]*(">)/, `$1${attr(e.title)} — an interactive story$2`)
    .replace(/(<meta property="og:description" content=")[^"]*(">)/, `$1${attr(desc)}$2`)
    .replace(/(<meta property="og:image" content=")[^"]*(">)/, `$1${og}$2`)
    .replace(/(<meta name="twitter:title" content=")[^"]*(">)/, `$1${attr(e.title)} — an interactive story$2`)
    .replace(/(<meta name="twitter:description" content=")[^"]*(">)/, `$1${attr(desc)}$2`)
    .replace(/(<meta name="twitter:image" content=")[^"]*(">)/, `$1${og}$2`)
    .replace(/<body>/, `<body>\n<script>window.__WM_BOOK=${JSON.stringify({ slug: e.slug, file: e.file })}</script>`);
  await writeFile(join(DIST, "b", `${e.slug}.html`), html);
}

console.log(`Built ${episodes.length} episode(s) into dist/`);
for (const e of episodes) {
  console.log(`  ep ${e.episode}: ${e.title} — ${e.paragraphs} paragraphs, ${e.endings} endings, ${e.levels.join("/")}`);
}
