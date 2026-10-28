import assert from "node:assert/strict";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { chromium, webkit } = require(process.env.PW_DIR
  ? process.env.PW_DIR + "/node_modules/playwright"
  : "playwright");
const base = process.env.READER_TEST_URL || "http://127.0.0.1:8874/books/read.html";

for (const [engineName, engine] of [["Chromium", chromium], ["WebKit", webkit]]) {
  const browser = await engine.launch();
  for (const width of [375, 1440]) {
    const page = await browser.newPage({ viewport: { width, height: 812 } });
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    await page.goto(base + "?book=episode-01.json");
    await page.getByRole("button", { name: /Start reading/ }).click();
    await page.locator('.moment-card[data-node="1"]').waitFor();
    assert.equal(await page.locator(".choice-destination").first().textContent(), "§ 2");
    const originalSize = parseFloat(await page.locator(".para").evaluate(el => getComputedStyle(el).fontSize));

    await page.locator(".choices button").first().click();
    await page.locator('.moment-card[data-node="2"]').waitFor();
    await page.getByRole("button", { name: "Turn back to the previous page" }).click();
    await page.locator('.moment-card[data-node="1"]').waitFor();
    await page.getByRole("button", { name: "Settings" }).click();
    await page.getByRole("button", { name: "Make story text larger" }).click();
    await page.getByRole("button", { name: "Close settings" }).click();
    const largerSize = parseFloat(await page.locator(".para").evaluate(el => getComputedStyle(el).fontSize));
    assert.ok(largerSize > originalSize, "text control enlarges the story");

    await page.locator(".choices button").first().click();
    await page.locator('.moment-card[data-node="2"]').waitFor();
    const progress = await page.evaluate(() => JSON.parse(localStorage.getItem("ab:prefs")).progress["new-city:1"]);
    assert.equal(progress.n, 2);
    assert.equal(progress.trail.at(-1).n, 1);
    await page.goto(base);
    await page.locator('.book[data-file="episode-01.json"]').click();
    await page.locator('.moment-card[data-node="2"]').waitFor();
    assert.equal(await page.getByRole("button", { name: "Turn back to the previous page" }).isEnabled(), true);
    await page.locator(".choices button").nth(2).click();
    await page.locator('.moment-card[data-node="43"]').waitFor();
    await page.locator(".choices button").nth(1).click();
    await page.locator('.moment-card[data-node="4"]').waitFor();
    const flagged = await page.evaluate(() => JSON.parse(localStorage.getItem("ab:prefs")).progress["new-city:1"].f);
    assert.ok(flagged.includes("knows_river"));
    await page.getByRole("button", { name: "Turn back to the previous page" }).click();
    await page.locator('.moment-card[data-node="43"]').waitFor();
    const restored = await page.evaluate(() => JSON.parse(localStorage.getItem("ab:prefs")).progress["new-city:1"].f);
    assert.ok(!restored.includes("knows_river"), "turning back restores story flags");
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth - innerWidth), 0);
    assert.deepEqual(errors, []);
    console.log(`${engineName} ${width}px: page turn, back, resume, text size, layout OK`);
    await page.close();
  }
  await browser.close();
}
