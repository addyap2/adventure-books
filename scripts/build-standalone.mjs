// Packs the whole reader into ONE self-contained HTML file: the app, every episode,
// the lexicon and the manifest inlined as window.__ADVENTURE__, and the favicon as a
// data URI. The result runs from a double-click with no server and is trivial to share
// or publish. Run `node scripts/build-site.mjs` first — this reads from dist/.
import { readdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname;
const DIST = join(ROOT, "dist");

const html = await readFile(join(DIST, "index.html"), "utf8");

// gather every JSON file the reader fetches, keyed by the exact path it asks for
const data = {};
for (const f of (await readdir(DIST)).filter(f => f.endsWith(".json"))) {
  data[f] = JSON.parse(await readFile(join(DIST, f), "utf8"));
}

// inline the favicon so the single file has no external references at all
let faviconTag = "";
try {
  const svg = await readFile(join(DIST, "favicon.svg"), "utf8");
  const uri = "data:image/svg+xml;base64," + Buffer.from(svg).toString("base64");
  faviconTag = `<link rel="icon" href="${uri}" type="image/svg+xml">`;
} catch { /* no favicon — fine */ }

// </ inside JSON would close the script tag early; escape it
const blob = JSON.stringify(data).replace(/<\//g, "<\\/");
const inject = `<script>window.__ADVENTURE__=${blob};</script>\n<script>`;

const out = html
  .replace(/<link rel="icon"[^>]*>/, faviconTag)   // swap the file ref for the data URI
  .replace("<script>", inject);                     // seed data just before the app script

const target = join(DIST, "adventure-book.html");
await writeFile(target, out);
console.log(`Packed standalone reader → dist/adventure-book.html (${(out.length/1024).toFixed(0)} KB, ${Object.keys(data).length} data files inlined)`);
