// Builds the static site into dist/: the reader, every episode, the shared lexicon,
// and a manifest the reader uses to list episodes. No framework, no dependencies.
import { readdir, readFile, writeFile, mkdir, cp, rm } from "node:fs/promises";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname;
const CONTENT = join(ROOT, "content");
const DIST = join(ROOT, "dist");

await rm(DIST, { recursive: true, force: true });
await mkdir(DIST, { recursive: true });
await cp(join(ROOT, "web", "index.html"), join(DIST, "index.html"));
await cp(join(ROOT, "web", "favicon.svg"), join(DIST, "favicon.svg"));

const files = (await readdir(CONTENT)).filter(f => f.endsWith(".json"));
const episodes = [];

for (const f of files) {
  const raw = await readFile(join(CONTENT, f), "utf8");
  const json = JSON.parse(raw);
  await writeFile(join(DIST, f), raw);
  if (!json.nodes) continue;                       // the lexicon, not an episode
  episodes.push({
    file: f,
    episode: json.episode ?? 0,
    title: json.title ?? f,
    levels: json.levels ?? [],
    paragraphs: json.nodes.length,
    endings: json.nodes.filter(n => n.ending).length,
  });
}
episodes.sort((a, b) => a.episode - b.episode);

const manifest = {
  series: episodes[0]?.file ? JSON.parse(await readFile(join(CONTENT, episodes[0].file), "utf8")).series : "",
  lexicon: "lexicon.json",
  episodes,
};
await writeFile(join(DIST, "manifest.json"), JSON.stringify(manifest, null, 2));

console.log(`Built ${episodes.length} episode(s) into dist/`);
for (const e of episodes) {
  console.log(`  ep ${e.episode}: ${e.title} — ${e.paragraphs} paragraphs, ${e.endings} endings, ${e.levels.join("/")}`);
}
