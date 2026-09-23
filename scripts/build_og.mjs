// Generate a per-book social (OG) card, skinned from each book's identity.
// Run locally (needs Chrome) and commit the PNGs — Vercel's build has no browser,
// it just copies web/og-<slug>.png. Usage: node scripts/build_og.mjs
import { readdir, readFile, writeFile, mkdtemp } from "node:fs/promises";
import { execFileSync } from "node:child_process";
import { tmpdir } from "node:os";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname;
const CONTENT = join(ROOT, "content");
const WEB = join(ROOT, "web");
const CHROME = process.env.CHROME ||
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const EPN = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"];

const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const titleCase = (s) => String(s || "").replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

// The scene is chosen by identity.cover.kind so each book gets its own picture,
// not just its own colours: "nocturne" = a moonlit skyline with one lit window
// (The Address); "daybreak" = a cold grey street with one warm-lit open doorway
// (The Room). Add a new branch here when a future book needs a new world.
function nocturneScene(c) {
  return `
  <g fill="${c.ink}" opacity="0.6"><circle cx="620" cy="70" r="1.4"/><circle cx="820" cy="120" r="1.1"/><circle cx="1010" cy="70" r="1.2"/><circle cx="1120" cy="150" r="1.3"/></g>
  <g><circle cx="1030" cy="120" r="58" fill="${c.ink}" opacity=".12"/><circle cx="1030" cy="120" r="38" fill="${c.ink}" opacity=".8"/><circle cx="1050" cy="106" r="38" fill="${c.ground}"/></g>
  <g fill="${c.ground}"><rect x="720" y="250" width="90" height="230"/><rect x="820" y="300" width="70" height="180"/><rect x="905" y="210" width="110" height="270"/><rect x="1025" y="290" width="86" height="190"/><rect x="1120" y="330" width="80" height="150"/></g>
  <ellipse cx="666" cy="352" rx="150" ry="170" fill="url(#glow)"/>
  <rect x="656" y="338" width="20" height="30" rx="1" fill="${c.accentHot}"/>
  <rect x="0" y="480" width="1200" height="90" fill="${c.surface}"/>
  <rect x="658" y="484" width="18" height="82" fill="${c.accent}" opacity=".26"/>
  <rect x="0" y="566" width="1200" height="64" fill="${c.ground}"/>
  <g><ellipse cx="300" cy="560" rx="52" ry="8" fill="#000" opacity=".35"/><path d="M300 500 C314 502 320 514 322 530 L328 560 L272 560 L278 530 C280 514 286 502 300 500 Z" fill="#04060d"/><circle cx="300" cy="489" r="11" fill="#04060d"/><path d="M287 486 q13 -11 26 0 z" fill="#04060d"/></g>`;
}
function daybreakScene(c) {
  // a cold overcast day: slate rooftops, a terrace wall, one warm open doorway
  // spilling light onto wet pavement, a lone figure from behind approaching it.
  return `
  <g fill="${c.surface}" opacity="0.85"><rect x="620" y="250" width="120" height="250"/><rect x="748" y="212" width="96" height="288"/><rect x="852" y="272" width="112" height="228"/><rect x="972" y="232" width="92" height="268"/><rect x="1072" y="284" width="112" height="216"/></g>
  <rect x="560" y="330" width="640" height="240" fill="${c.ground}"/>
  <g fill="${c.surface}" opacity="0.9"><rect x="596" y="360" width="34" height="46"/><rect x="820" y="360" width="34" height="46"/><rect x="900" y="360" width="34" height="46"/><rect x="1060" y="360" width="34" height="46"/><rect x="1140" y="360" width="34" height="46"/></g>
  <ellipse cx="722" cy="470" rx="128" ry="150" fill="url(#glow)"/>
  <rect x="700" y="398" width="46" height="112" rx="2" fill="${c.accentHot}"/>
  <rect x="700" y="398" width="46" height="112" rx="2" fill="none" stroke="${c.accent}" stroke-width="3"/>
  <rect x="0" y="510" width="1200" height="120" fill="${c.surface}"/>
  <path d="M700 510 L746 510 L812 570 L636 570 Z" fill="${c.accent}" opacity=".22"/>
  <rect x="0" y="588" width="1200" height="42" fill="${c.ground}"/>
  <g transform="translate(348,-2)"><ellipse cx="300" cy="562" rx="46" ry="7" fill="#000" opacity=".3"/><path d="M300 508 C312 510 317 520 319 534 L324 562 L276 562 L281 534 C283 520 288 510 300 508 Z" fill="#0a1114"/><circle cx="300" cy="499" r="10" fill="#0a1114"/><path d="M289 496 q11 -9 22 0 z" fill="#0a1114"/></g>`;
}
function lanternScene(c) {
  // a warm crowded night market: a row of paper lanterns strung across, a glowing
  // stall under an awning with a rising column of steam, dark market roofs behind.
  const lantern = (x, y, r) =>
    `<g><line x1="${x}" y1="${y - r - 8}" x2="${x}" y2="${y - r}" stroke="${c.line}"/>` +
    `<ellipse cx="${x}" cy="${y}" rx="${r * 0.72}" ry="${r}" fill="${c.accentHot}" opacity="0.92"/>` +
    `<ellipse cx="${x}" cy="${y}" rx="${r * 0.72}" ry="${r}" fill="none" stroke="${c.accent}" stroke-width="2"/></g>`;
  return `
  <g fill="${c.surface}"><rect x="620" y="250" width="120" height="250"/><rect x="748" y="214" width="96" height="286"/><rect x="852" y="270" width="112" height="230"/><rect x="972" y="234" width="92" height="266"/><rect x="1072" y="286" width="112" height="214"/></g>
  <path d="M600 150 Q900 120 1200 168" fill="none" stroke="${c.line}" stroke-width="2"/>
  ${lantern(660, 196, 26)}${lantern(760, 180, 30)}${lantern(872, 176, 28)}${lantern(984, 182, 30)}${lantern(1096, 196, 26)}
  <ellipse cx="800" cy="470" rx="220" ry="180" fill="url(#glow)"/>
  <path d="M660 356 l24 -34 h232 l24 34 z" fill="${c.surface}"/>
  <path d="M660 356 h280" stroke="${c.accent}" stroke-width="3"/>
  <g stroke="${c.accent}" stroke-width="3" opacity="0.5"><path d="M690 322 l14 34"/><path d="M754 322 l10 34"/><path d="M820 322 l6 34"/><path d="M886 322 l2 34"/></g>
  <rect x="676" y="356" width="248" height="150" fill="${c.ground}"/>
  <rect x="676" y="440" width="248" height="12" fill="${c.accent}" opacity="0.32"/>
  <g><ellipse cx="800" cy="452" rx="46" ry="12" fill="${c.accentHot}" opacity="0.9"/><path d="M792 396 c-6 10 6 14 0 24 M808 396 c-6 10 6 14 0 24" fill="none" stroke="${c.ink}" stroke-width="3" opacity="0.5"/></g>
  <rect x="0" y="506" width="1200" height="124" fill="${c.surface}"/>
  <rect x="0" y="588" width="1200" height="42" fill="${c.ground}"/>
  <g transform="translate(360,4)"><ellipse cx="300" cy="560" rx="48" ry="7" fill="#000" opacity=".3"/><path d="M300 506 C313 508 319 519 321 533 L327 560 L273 560 L279 533 C281 519 287 508 300 506 Z" fill="#160b06"/><circle cx="300" cy="497" r="10" fill="#160b06"/></g>`;
}

function ogHTML(book) {
  const p = (book.identity && book.identity.palette) || {};
  const ground = p.ground || "#0E1320", surface = p.surface || "#121a2c",
        ink = p.ink || "#F4EFE6", accent = p.accent || "#E8A24C",
        accentHot = p.accentHot || "#F4BE72", secondary = p.secondary || "#86C9B4",
        muted = p.muted || "#8A93A6";
  const c = { ground, surface, ink, accent, accentHot, secondary, muted };
  const kind = (book.identity && book.identity.cover && book.identity.cover.kind) || "nocturne";
  const scene = kind === "daybreak" ? daybreakScene(c)
              : kind === "lantern" ? lanternScene(c)
              : nocturneScene(c);
  const skyStops = kind === "daybreak"
    ? `<stop offset="0" stop-color="#AAB7BF"/><stop offset="0.5" stop-color="#6F838D"/><stop offset="1" stop-color="${surface}"/>`
    : `<stop offset="0" stop-color="${ground}"/><stop offset="0.72" stop-color="${surface}"/><stop offset="1" stop-color="${surface}"/>`;
  const line = (book.identity && book.identity.hero && book.identity.hero.line && book.identity.hero.line.en) || book.blurb || "";
  const levels = (book.levels || []).join(" · ");
  const title = book.title || "";
  const titleSize = title.length > 12 ? 92 : 104;
  return `<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:${ground}}svg{display:block}</style></head><body>
<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      ${skyStops}
    </linearGradient>
    <linearGradient id="scrim" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="${ground}" stop-opacity="0.95"/><stop offset="0.52" stop-color="${ground}" stop-opacity="0.55"/><stop offset="1" stop-color="${ground}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="${accentHot}" stop-opacity="0.85"/><stop offset="0.42" stop-color="${accent}" stop-opacity="0.3"/><stop offset="1" stop-color="${accent}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="vig" cx="50%" cy="42%" r="80%"><stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.4"/></radialGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#sky)"/>
  ${scene}
  <rect width="1200" height="630" fill="url(#vig)"/>
  <rect width="720" height="630" fill="url(#scrim)"/>
  <text x="72" y="250" font-family="ui-monospace, Menlo, monospace" font-size="17" letter-spacing="5" fill="${accent}">AN ENGLISH ADVENTURE</text>
  <text x="68" y="360" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="${titleSize}" fill="${ink}">${esc(title)}</text>
  <text x="72" y="416" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="26" fill="#cdd4e2">${esc(line)}</text>
  <line x1="74" y1="452" x2="330" y2="452" stroke="${accent}" stroke-width="1.5" opacity=".65"/>
  <text x="72" y="486" font-family="ui-monospace, Menlo, monospace" font-size="13.5" letter-spacing="3" fill="${muted}">FOR ENGLISH LEARNERS &#183; ${esc(levels)} &#183; 8 LANGUAGES</text>
</svg></body></html>`;
}

const files = (await readdir(CONTENT)).filter((f) => f.endsWith(".json"));
const tmp = await mkdtemp(join(tmpdir(), "wm-og-"));
let n = 0;
for (const f of files) {
  const book = JSON.parse(await readFile(join(CONTENT, f), "utf8"));
  if (!book.nodes) continue;                       // skip the lexicon
  const slug = book.slug || f.replace(/\.json$/, "");
  const htmlPath = join(tmp, slug + ".html");
  const out = join(WEB, `og-${slug}.png`);
  await writeFile(htmlPath, ogHTML(book));
  execFileSync(CHROME, ["--headless", "--disable-gpu", "--hide-scrollbars",
    "--force-device-scale-factor=1", "--window-size=1200,630",
    `--screenshot=${out}`, `file://${htmlPath}`], { stdio: "ignore" });
  console.log(`og-${slug}.png  ← ${book.title}`);
  n++;
}
console.log(`Generated ${n} per-book OG card(s).`);
