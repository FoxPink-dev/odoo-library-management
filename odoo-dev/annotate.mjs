import Jimp from 'jimp';
import path from 'path';

const DIR = 'C:\\Users\\Admin\\AppData\\Local\\Temp\\odoo_screenshots';
const OUT_DIR = 'C:\\Users\\Admin\\AppData\\Local\\Temp\\odoo_screenshots\\annotated';
const fs = await import('fs');

// Annotation definitions: [x, y, w, h, number, label]
const ANNOTATIONS = {
  '01_wizard_form': [
    [250, 110, 280, 35, 1, 'Date From'],
    [550, 110, 280, 35, 2, 'Date To'],
    [250, 180, 600, 35, 3, 'Products'],
    [250, 215, 280, 35, 4, 'Category'],
    [550, 215, 280, 35, 5, 'Warehouse/Location'],
    [300, 300, 140, 35, 6, 'Generate'],
    [460, 300, 140, 35, 7, 'Print PDF'],
  ],
  '02_list_view': [
    [230, 95, 200, 25, 1, 'Product column'],
    [680, 95, 100, 25, 2, 'In/Out Qty'],
    [870, 95, 100, 25, 3, 'Balance Qty'],
    [1050, 95, 120, 25, 4, 'Unit Cost'],
    [1180, 95, 140, 25, 5, 'Valuation'],
  ],
  '03_graph_view': [
    [300, 200, 800, 400, 1, 'Chart area'],
    [250, 550, 600, 80, 2, 'Measure / Group By'],
    [190, 120, 80, 200, 3, 'Date axis (Month)'],
  ],
  '04_pivot_view': [
    [230, 95, 200, 30, 1, 'Row: Product'],
    [600, 95, 400, 30, 2, 'Col: Date (Month)'],
    [500, 150, 400, 300, 3, 'Measures area'],
  ],
  '05_menu_location': [
    [10, 48, 210, 25, 1, 'Inventory menu'],
    [10, 310, 210, 20, 2, 'Reporting section'],
    [10, 330, 210, 25, 3, 'Stock Card Report'],
  ],
};

function setPixel(data, width, x, y, r, g, b, a) {
  if (x < 0 || y < 0 || x >= width || y >= data.length / 4) return;
  const idx = (y * width + x) * 4;
  data[idx] = r;
  data[idx + 1] = g;
  data[idx + 2] = b;
  data[idx + 3] = a;
}

function drawRect(data, width, x, y, w, h, r, g, b, a, thickness = 3) {
  for (let t = 0; t < thickness; t++) {
    for (let px = x - t; px < x + w + t; px++) {
      setPixel(data, width, px, y - t, r, g, b, a);           // top
      setPixel(data, width, px, y + h + t, r, g, b, a);       // bottom
    }
    for (let py = y - t; py < y + h + t; py++) {
      setPixel(data, width, x - t, py, r, g, b, a);           // left
      setPixel(data, width, x + w + t, py, r, g, b, a);       // right
    }
  }
}

function drawCircle(data, width, height, cx, cy, radius, r, g, b, a) {
  for (let dy = -radius; dy <= radius; dy++) {
    for (let dx = -radius; dx <= radius; dx++) {
      if (dx * dx + dy * dy <= radius * radius) {
        setPixel(data, width, cx + dx, cy + dy, r, g, b, a);
      }
    }
  }
}

async function annotate(filename) {
  const base = filename.replace('.png', '');
  const annots = ANNOTATIONS[base];
  if (!annots) return false;

  const img = await Jimp.read(path.join(DIR, filename));
  const { data, width, height } = img.bitmap;
  const font8 = await Jimp.loadFont(Jimp.FONT_SANS_8_BLACK);
  const font12 = await Jimp.loadFont(Jimp.FONT_SANS_12_BLACK);
  const font16 = await Jimp.loadFont(Jimp.FONT_SANS_16_BLACK);

  for (const [x, y, w, h, num, label] of annots) {
    // Red rectangle border
    drawRect(data, width, x, y, w, h, 255, 0, 0, 255, 3);

    // Red circle with white number
    const cx = x - 10;
    const cy = y - 10;
    const rad = 14;
    drawCircle(data, width, height, cx, cy, rad, 255, 0, 0, 255);
    drawCircle(data, width, height, cx, cy, rad - 3, 255, 255, 255, 255);

    // Print number (black on white circle)
    const numStr = String(num);
    img.print(font16, cx - 6, cy - 8, numStr);

    // Print label next to circle
    img.print(font12, cx + rad + 6, cy - 7, label);
  }

  await img.writeAsync(path.join(OUT_DIR, filename));
  return true;
}

// Main
fs.mkdirSync(OUT_DIR, { recursive: true });
const files = fs.readdirSync(DIR).filter(f => f.endsWith('.png') && !f.startsWith('00') && !f.startsWith('debug') && !f.startsWith('test') && f !== 'odoo_discuss.png');

for (const f of files) {
  console.log(`Annotating: ${f}`);
  await annotate(f);
}

console.log(`\nDone! Annotations saved to: ${OUT_DIR}`);
fs.readdirSync(OUT_DIR).forEach(f => console.log(`  ${f}`));
