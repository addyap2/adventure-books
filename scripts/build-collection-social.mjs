// Rebuild the collection's sharing cards from its editable book illustrations.
// npm run build:social (requires npm install and Playwright's Chromium).
import { chromium } from 'playwright';
import { readFile } from 'node:fs/promises';

const web = new URL('../web/', import.meta.url);
const catalog = JSON.parse(await readFile(new URL('illustrations/catalog.json', web), 'utf8'));
const books = await Promise.all(Object.entries(catalog).map(async ([slug, art], index) => {
  const book = JSON.parse(await readFile(new URL(`../content/episode-${String(index + 1).padStart(2, '0')}.json`, web), 'utf8'));
  if (book.slug !== slug) throw new Error(`Book catalog order differs at ${slug}`);
  const svg = await readFile(new URL(art.cover.slice(1), web));
  return { ...book, art, image: 'data:image/svg+xml;base64,' + svg.toString('base64') };
}));
const esc = text => String(text).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');
const browser = await chromium.launch(process.env.CHROME ? { executablePath: process.env.CHROME } : {});
try {
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  const style = `<style>
    *{box-sizing:border-box}body{margin:0;background:#f5f2ee;color:#202622;font-family:Arial,sans-serif}
    main{margin:40px;width:1120px;height:550px;border-radius:26px;overflow:hidden;background:#fffdfa;display:flex;box-shadow:0 20px 40px #17373516}
    .art{width:450px;height:550px;object-fit:cover;flex-shrink:0}
    .copy{padding:56px 52px;display:flex;flex-direction:column;justify-content:center}
    .eyebrow{color:#9c563b;font-size:15px;font-weight:700;letter-spacing:2.4px;text-transform:uppercase}
    h1{font:normal 62px/1.05 Georgia,serif;letter-spacing:-2px;margin:23px 0 25px}
    p{font:24px/1.5 Georgia,serif;color:#586059;margin:0}
    .footer{margin-top:33px;font-size:15px;color:#446e64;font-weight:700;letter-spacing:.4px}
    .collection{padding:44px;display:block}.collection h1{font-size:52px;margin:15px 0 30px}
    .covers{display:flex;gap:13px}.covers img{width:117px;height:177px;object-fit:cover;border-radius:7px}
    .collection .footer{display:flex;justify-content:space-between;margin-top:32px}
  </style>`;
  for (const book of books) {
    await page.setContent(style + `<main><img class="art" src="${book.image}" alt=""><div class="copy"><span class="eyebrow">An adventure in English</span><h1>${esc(book.title)}</h1><p>A story shaped by your choices.</p><div class="footer">A2 · B1 · B2 &nbsp; / &nbsp; Free to read<br><br>English Reading Adventures · Antony Addy</div></div></main>`);
    await page.locator('img').evaluate(img => img.decode());
    await page.screenshot({ path: new URL(book.art.social.slice(1), web).pathname });
  }
  await page.setContent(style + `<main class="collection"><span class="eyebrow">English Reading Adventures</span><h1>Eight stories. Your own way through.</h1><div class="covers">${books.map(book => `<img src="${book.image}" alt="">`).join('')}</div><div class="footer"><span>Learn English. Live a story.</span><span>A2 · B1 · B2 &nbsp; / &nbsp; Free to read</span></div></main>`);
  await page.locator('img').evaluateAll(imgs => Promise.all(imgs.map(img => img.decode())));
  await page.screenshot({ path: new URL('og-collection.png', web).pathname });
  console.log(`Built ${books.length} book sharing cards and the collection card.`);
} finally {
  await browser.close();
}
