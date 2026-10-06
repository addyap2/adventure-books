// Builds the static site into dist/: the reader, every episode, the shared lexicon,
// and a manifest the reader uses to list episodes. No framework, no dependencies.
import { readdir, readFile, writeFile, mkdir, cp, rm } from "node:fs/promises";
import { join } from "node:path";
import { execFileSync } from "node:child_process";

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

// Prerender each book's introduction and reader entry with its own content and metadata.
// Client JavaScript then adds language selection and the interactive reading experience.
const BASE = "https://adventure-books-five.vercel.app";
const tmpl = await readFile(join(ROOT, "web", "book.html"), "utf8");
const attr = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
const htmlText = (s) => attr(s).replace(/>/g, "&gt;");
const readerTmpl = await readFile(join(ROOT, "web", "index.html"), "utf8");
await mkdir(join(DIST, "b"), { recursive: true });
await mkdir(join(DIST, "read"), { recursive: true });
for (const e of episodes) {
  const book = JSON.parse(await readFile(join(CONTENT, e.file), "utf8"));
  const desc = e.blurb || "An interactive story for English learners — you choose what happens.";
  const url = `${BASE}/b/${e.slug}`;
  const og = `${BASE}/og-${e.slug}.png`;
  const coverAlt = e.identity?.cover?.alt || `${e.title} cover artwork.`;
  let html = tmpl
    .replace(/<title>[\s\S]*?<\/title>/, `<title>${attr(e.title)} — an interactive story</title>`)
    .replace(/(<meta name="description" content=")[^"]*(">)/, `$1${attr(desc)}$2`)
    .replace(/(<link rel="canonical" href=")[^"]*(">)/, `$1${url}$2`)
    .replace(/(<meta property="og:url" content=")[^"]*(">)/, `$1${url}$2`)
    .replace(/(<meta property="og:title" content=")[^"]*(">)/, `$1${attr(e.title)} — an interactive story$2`)
    .replace(/(<meta property="og:description" content=")[^"]*(">)/, `$1${attr(desc)}$2`)
    .replace(/(<meta property="og:image" content=")[^"]*(">)/, `$1${og}$2`)
    .replace(/(<meta property="og:image:alt" content=")[^"]*(">)/, `$1${attr(coverAlt)}$2`)
    .replace(/(<meta name="twitter:title" content=")[^"]*(">)/, `$1${attr(e.title)} — an interactive story$2`)
    .replace(/(<meta name="twitter:description" content=")[^"]*(">)/, `$1${attr(desc)}$2`)
    .replace(/(<meta name="twitter:image" content=")[^"]*(">)/, `$1${og}$2`)
    .replace(/<body>/, `<body>\n<script>window.__WM_BOOK=${JSON.stringify({ slug: e.slug, file: e.file })}</script>`);
  // Keep the first painted page specific to this book, including with JavaScript disabled.
  // The hydration script remains after this boundary and can still enhance the page.
  const boundary = html.indexOf('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js');
  if (boundary < 0) throw new Error("Book template script boundary missing");
  let body = html.slice(0, boundary);
  const scripts = html.slice(boundary);
  const headline = htmlText(book.identity?.hero?.line?.en || e.title);
  const sub = htmlText(book.identity?.hero?.sub || "A story where you are the hero — and every choice turns you to a new page.");
  body = body
    .replace(/(<span class="sr-only">)[^<]*(<\/span>)/, `$1${headline}$2`)
    .replace(/(<span class="morph" aria-hidden="true" id="morph">)[^<]*(<\/span>)/, `$1${headline}$2`)
    .replace(/(<p class="sub">)[\s\S]*?(<\/p>)/, `$1${sub}$2`)
    .replaceAll('/read.html?book=episode-01.json&amp;', `/read/${e.slug}.html?`)
    .replaceAll('/read.html?book=episode-01.json', `/read/${e.slug}.html`)
    .replace('href="/read.html"', `href="/read/${e.slug}.html"`);
  if (existsSync(join(ROOT, "web", `cover-${e.slug}.png`))) {
    const focal = e.identity?.cover?.focal || "center";
    body = body.replace('class="stage" id="stage"', 'class="stage has-art" id="stage"')
      .replace('id="art" data-depth="0.05" aria-hidden="true"',
        `id="art" data-depth="0.05" aria-hidden="true" style="background-image:url('/cover-${e.slug}.png');background-position:${attr(focal)}"`);
  }
  if (e.slug !== "the-address") {
    body = body
      .replace('Not a course. A city you <em>find your way</em> through.', 'Not a course. A world you <em>choose your way</em> through.')
      .replace(/(<p class="body reveal d2">)[\s\S]*?(<\/p>)/,
        `$1${htmlText(desc)} What you do next is yours to choose — and the English bends to your level while you read.$2`)
      .replace('Branching sections, twelve endings to find. Read it again and the night goes differently.',
        'Branching sections, twelve endings to find. Read it again and the story goes differently.')
      .replace('The train has gone. The city is <em>yours</em> to read.',
        'The story begins. The next choice is <em>yours</em>.');
  }
  html = body + scripts;
  await writeFile(join(DIST, "b", `${e.slug}.html`), html);

  // The reader is the JS app for the story; its canonical (and matching og:url)
  // point at the /b/<slug> landing page, so search/social signals consolidate on
  // one indexable URL per book instead of splitting across /b and /read.
  const reader = readerTmpl
    .replace(/<title>[\s\S]*?<\/title>/, `<title>${attr(e.title)} — English Reading Adventures</title>`)
    .replace(/(<meta name="description" content=")[^"]*(">)/, `$1${attr(desc)}$2`)
    .replace(/(<link rel="canonical" href=")[^"]*(">)/, `$1${url}$2`)
    .replace(/(<meta property="og:url" content=")[^"]*(">)/, `$1${url}$2`)
    .replace(/(<meta property="og:title" content=")[^"]*(">)/, `$1${attr(e.title)} — English Reading Adventures$2`)
    .replace(/(<meta property="og:description" content=")[^"]*(">)/, `$1${attr(desc)}$2`)
    .replace(/(<meta property="og:image" content=")[^"]*(">)/, `$1${og}$2`)
    .replace(/(<meta property="og:image:alt" content=")[^"]*(">)/, `$1${attr(coverAlt)}$2`)
    .replace(/(<meta name="twitter:title" content=")[^"]*(">)/, `$1${attr(e.title)} — English Reading Adventures$2`)
    .replace(/(<meta name="twitter:description" content=")[^"]*(">)/, `$1${attr(desc)}$2`)
    .replace(/(<meta name="twitter:image" content=")[^"]*(">)/, `$1${og}$2`)
    .replace(/<body>/, `<body>\n<script>window.__WM_READER_BOOK=${JSON.stringify(e.file)}</script>`);
  await writeFile(join(DIST, "read", `${e.slug}.html`), reader);
}

// SEO: a sitemap of the library + every book page, and a robots.txt pointing to it.
// lastmod reflects when each page's own inputs last changed (git commit date),
// not the build time — a sitemap that stamps "today" on everything every deploy
// teaches crawlers to ignore the signal. ISO dates sort lexicographically, so
// `>` picks the most recent; git-less build envs fall back to today.
const today = new Date().toISOString().slice(0, 10);
const gitDate = (paths) => {
  let latest = "";
  for (const p of paths) {
    try {
      const d = execFileSync("git", ["log", "-1", "--format=%cs", "--", p],
        { cwd: ROOT, stdio: ["ignore", "pipe", "ignore"] }).toString().trim();
      if (d && d > latest) latest = d;
    } catch { /* unreadable path or no git — skip */ }
  }
  return latest || today;
};
// a book's landing page is rendered from its episode JSON + cover/og art + the
// shared book.html template; the homepage lists every book from library.html.
const bookDate = (e) => gitDate([
  `content/${e.file}`, `web/cover-${e.slug}.png`, `web/og-${e.slug}.png`, "web/book.html",
]);
const homeDate = gitDate([
  "web/library.html",
  ...episodes.map(e => `content/${e.file}`),
  ...episodes.map(e => `web/cover-${e.slug}.png`),
]);
const urls = [
  { loc: "/", lastmod: homeDate },
  ...episodes.map(e => ({ loc: `/b/${e.slug}`, lastmod: bookDate(e) })),
];
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n` +
  `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
  urls.map(u => `  <url><loc>${BASE}${u.loc}</loc><lastmod>${u.lastmod}</lastmod></url>`).join("\n") +
  `\n</urlset>\n`;
await writeFile(join(DIST, "sitemap.xml"), sitemap);
await writeFile(join(DIST, "robots.txt"), `User-agent: *\nAllow: /\n\nSitemap: ${BASE}/sitemap.xml\n`);
console.log("Wrote sitemap.xml + robots.txt");

console.log(`Built ${episodes.length} episode(s) into dist/`);
for (const e of episodes) {
  console.log(`  ep ${e.episode}: ${e.title} — ${e.paragraphs} paragraphs, ${e.endings} endings, ${e.levels.join("/")}`);
}
