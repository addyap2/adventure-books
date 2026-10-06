// Check the palette pairings used for reader text, filled controls and resting
// control edges. Decorative rules use --line and do not define a control shape.
import { readdir, readFile } from "node:fs/promises";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("..", import.meta.url));
const contentDir = join(root, "content");
const readerCss = await readFile(join(root, "web", "index.html"), "utf8");

function cssBlock(selector) {
  let start = 0;
  while ((start = readerCss.indexOf(selector, start)) >= 0) {
    let open = start + selector.length;
    while (/\s/.test(readerCss[open])) open++;
    if (readerCss[open] === "{") {
      const close = readerCss.indexOf("}", open);
      if (close < 0) throw new Error("Invalid CSS block: " + selector);
      return readerCss.slice(open + 1, close);
    }
    start += selector.length;
  }
  throw new Error("Missing CSS block: " + selector);
}

function cssHex(block, token) {
  const match = block.match(new RegExp("--" + token + "\\s*:\\s*(#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?)"));
  if (!match) throw new Error("Missing hex token: --" + token);
  return match[1];
}

function luminance(hex) {
  const h = hex.slice(1);
  const pairs = h.length === 3
    ? [...h].map(c => c + c)
    : h.match(/.{2}/g);
  if (!pairs || pairs.length !== 3) throw new Error("Invalid colour: " + hex);
  const [r, g, b] = pairs.map(pair => {
    const v = Number.parseInt(pair, 16) / 255;
    return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

function ratio(a, b) {
  const [bright, dark] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (bright + 0.05) / (dark + 0.05);
}

const failures = [];
function check(name, foreground, background, minimum) {
  const actual = ratio(foreground, background);
  if (actual < minimum) {
    failures.push(name + ": " + actual.toFixed(2) + ":1 (needs " + minimum + ":1; " + foreground + " on " + background + ")");
  }
}

const darkCss = cssBlock(":root");
const paperCss = cssBlock(':root[data-theme="light"]');
const darkButtonInk = cssHex(darkCss, "accent-ink");
const paper = Object.fromEntries(
  ["bg", "card", "fg", "muted", "accent", "accent-2", "accent-ink"]
    .map(token => [token, cssHex(paperCss, token)])
);

const files = (await readdir(contentDir))
  .filter(name => /^episode-\d+\.json$/.test(name))
  .sort();
if (!files.length) throw new Error("No episode palettes found");

for (const file of files) {
  const book = JSON.parse(await readFile(join(contentDir, file), "utf8"));
  const p = book.identity?.palette;
  if (!p) throw new Error(file + ": missing identity.palette");
  for (const token of ["ground", "surface", "ink", "muted", "accent", "accentHot", "secondary", "line"]) {
    if (!/^#[0-9a-fA-F]{6}$/.test(p[token] || "")) {
      throw new Error(file + ": missing or invalid palette." + token);
    }
  }
  for (const surface of ["ground", "surface"]) {
    for (const ink of ["ink", "muted", "accent", "secondary"]) {
      check(file + " " + ink + "/" + surface, p[ink], p[surface], 4.5);
    }
    check(file + " control edge/" + surface, p.accent, p[surface], 3);
  }
  check(file + " button label/accent", darkButtonInk, p.accent, 4.5);
}

for (const surface of ["bg", "card"]) {
  for (const ink of ["fg", "muted", "accent", "accent-2"]) {
    check("paper " + ink + "/" + surface, paper[ink], paper[surface], 4.5);
  }
  check("paper control edge/" + surface, paper.accent, paper[surface], 3);
}
check("paper button label/accent", paper["accent-ink"], paper.accent, 4.5);

if (failures.length) {
  for (const failure of failures) console.error(failure);
  process.exitCode = 1;
} else {
  console.log("Contrast passed: " + files.length + " book palettes and the paper theme.");
}
