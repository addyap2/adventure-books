// Rasterise the app icon (web/icon.svg) to the PNG sizes a PWA manifest needs.
// Committed as static assets; run again with `node scripts/build-icons.mjs` after editing icon.svg.
import { readFile, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { Resvg } from "@resvg/resvg-js";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const svg = await readFile(join(ROOT, "web", "icon.svg"), "utf8");

for (const size of [192, 512]) {
  const png = new Resvg(svg, { fitTo: { mode: "width", value: size } }).render().asPng();
  await writeFile(join(ROOT, "web", `icon-${size}.png`), png);
  console.log(`web/icon-${size}.png  (${(png.length / 1024).toFixed(1)} KB)`);
}
