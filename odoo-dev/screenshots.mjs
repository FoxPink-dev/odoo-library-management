import puppeteer from 'puppeteer-core';
import path from 'path';
import fs from 'fs';

const ODOO_URL = 'http://localhost:8069';
const EDGE_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const OUT_DIR = path.resolve('C:\\Users\\Admin\\AppData\\Local\\Temp\\odoo_screenshots');
const USER = 'admin';
const PASS = 'admin';

let browser;

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function snap(page, name) {
  await sleep(2000);
  const fp = path.join(OUT_DIR, `${name}.png`);
  await page.screenshot({ path: fp, fullPage: false });
  const s = fs.statSync(fp);
  console.log(`  ${name}.png (${(s.size / 1024).toFixed(0)} KB)`);
}

try {
  fs.mkdirSync(OUT_DIR, { recursive: true });

  browser = await puppeteer.launch({
    executablePath: EDGE_PATH,
    headless: 'new',
    args: ['--no-sandbox', '--disable-gpu', '--window-size=1920,1080'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });

  // === LOGIN ===
  console.log('=== Login ===');
  await page.goto(`${ODOO_URL}/web/login`, { waitUntil: 'networkidle0', timeout: 30000 });
  await sleep(1500);
  await page.type('input[name="login"]', USER);
  await page.type('input[name="password"]', PASS);
  await page.click('button[type="submit"]');
  await page.waitForNavigation({ waitUntil: 'networkidle0', timeout: 15000 });
  await sleep(2000);
  console.log(`  Logged in: "${await page.title()}"`);

  // === Generate report via JSONRPC ===
  console.log('\n=== Generate report ===');
  const wizId = await page.evaluate(async () => {
    const r = await fetch('/jsonrpc', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'call', params: { service: 'object', method: 'execute_kw', args: ['stock_card_dev', 2, 'admin', 'stock.card.wizard', 'create', [{ date_from: '2026-01-01', date_to: '2026-12-31' }]] } })
    });
    return (await r.json()).result;
  });
  console.log(`  Wizard: ${wizId}`);

  const action = await page.evaluate(async (wid) => {
    const r = await fetch('/jsonrpc', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ jsonrpc: '2.0', id: 2, method: 'call', params: { service: 'object', method: 'execute_kw', args: ['stock_card_dev', 2, 'admin', 'stock.card.wizard', 'action_generate_report', [wid]] } })
    });
    return (await r.json()).result;
  }, wizId);
  console.log(`  Report ready: ${action.res_model}, lines domain=${JSON.stringify(action.domain)}`);

  const domainEnc = encodeURIComponent(JSON.stringify(action.domain));

  // === SCREENSHOTS (use hash navigation for SPA) ===
  console.log('\n=== Screenshots ===');

  // Navigate to web root first so SPA is loaded
  await page.goto(`${ODOO_URL}/web`, { waitUntil: 'networkidle0', timeout: 30000 });
  await sleep(2000);

  // 1. Wizard form
  console.log('1. Wizard form');
  await page.evaluate(() => { window.location.hash = 'action=stock_card_report.action_stock_card_wizard'; });
  await sleep(4000);
  await snap(page, '01_wizard_form');

  // 2. List view
  console.log('2. List view');
  await page.evaluate((m, d) => { window.location.hash = `model=${m}&view_type=list&domain=${d}`; }, action.res_model, domainEnc);
  await sleep(4000);
  await snap(page, '02_list_view');

  // 3. Graph view
  console.log('3. Graph view');
  await page.evaluate((m, d) => { window.location.hash = `model=${m}&view_type=graph&domain=${d}`; }, action.res_model, domainEnc);
  await sleep(4000);
  await snap(page, '03_graph_view');

  // 4. Pivot view
  console.log('4. Pivot view');
  await page.evaluate((m, d) => { window.location.hash = `model=${m}&view_type=pivot&domain=${d}`; }, action.res_model, domainEnc);
  await sleep(4000);
  await snap(page, '04_pivot_view');

  // 5. Menu location
  console.log('5. Menu location');
  await page.evaluate(() => { window.location.hash = 'menu_id=stock.menu_warehouse_report'; });
  await sleep(3000);
  await snap(page, '05_menu_location');

  console.log('\n=== DONE ===');
  console.log('Files:', fs.readdirSync(OUT_DIR).filter(f => f.endsWith('.png') && !f.startsWith('00')).join(', '));

} catch (err) {
  console.error('ERROR:', err.message);
} finally {
  if (browser) await browser.close();
}
