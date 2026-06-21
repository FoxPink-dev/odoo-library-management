from PIL import Image, ImageDraw, ImageFont
import os

BASE = os.path.join(os.path.dirname(__file__), "addons", "stock_card_report", "static", "description")
os.makedirs(BASE, exist_ok=True)
os.makedirs(os.path.join(BASE, "images"), exist_ok=True)

FONT = "C:/Windows/Fonts/arial.ttf"
FONT_BD = "C:/Windows/Fonts/arialbd.ttf"

# === ICON: 512x512 ===
icon = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
draw = ImageDraw.Draw(icon)

draw.rounded_rectangle([(20, 20), (492, 492)], radius=60, fill=(41, 128, 185))

bar_colors = [(255, 255, 255, 200), (255, 255, 255, 230), (255, 255, 255, 255)]
bar_x = [100, 200, 300]
bar_w = [60, 60, 60]
bar_h = [160, 220, 280]
bar_bottom = 420

for i in range(3):
    draw.rounded_rectangle(
        [(bar_x[i], bar_bottom - bar_h[i]), (bar_x[i] + bar_w[i], bar_bottom)],
        radius=8, fill=bar_colors[i]
    )

icon.save(os.path.join(BASE, "icon.png"))
print("icon.png created (512x512)")

# === COVER: 1280x640 ===
cover = Image.new("RGB", (1280, 640), (41, 128, 185))
draw = ImageDraw.Draw(cover)

for i in range(640):
    alpha = int(40 * (1 - i / 640))
    draw.rectangle([(0, i), (1280, i+1)], fill=(52, 152, 219, alpha))

draw.ellipse([(-80, -80), (200, 200)], fill=(52, 152, 219, 80))
draw.ellipse([(1000, 400), (1280, 680)], fill=(46, 204, 113, 60))
draw.ellipse([(600, -40), (800, 160)], fill=(255, 255, 255, 30))

chart_x, chart_y = 700, 150
chart_w, chart_h = 500, 370
draw.rectangle([(chart_x, chart_y), (chart_x + chart_w, chart_y + chart_h)],
               fill=(255, 255, 255, 25), outline=(255, 255, 255, 60), width=2)

for i in range(8):
    bx = chart_x + 30 + i * 55
    bh = [180, 220, 140, 200, 250, 120, 210, 160][i]
    draw.rounded_rectangle([(bx, chart_y + chart_h - bh - 20), (bx + 35, chart_y + chart_h - 20)],
                           radius=4, fill=(46, 204, 113, 200))

title_font = ImageFont.truetype(FONT_BD, 48)
sub_font = ImageFont.truetype(FONT, 24)
small_font = ImageFont.truetype(FONT, 18)

draw.text((60, 80), "Enhanced Stock Card Report", fill=(255, 255, 255, 255), font=title_font)
draw.text((60, 150), "Multi-Warehouse  |  Running Balance with Valuation  |  PDF & Excel Export  |  Charts",
          fill=(255, 255, 255, 200), font=sub_font)
draw.text((60, 200), "For Odoo Community Edition 18.0 & 19.0",
          fill=(255, 255, 255, 150), font=small_font)

draw.text((60, 260), "Features:", fill=(255, 255, 255, 220), font=sub_font)
features = [
    "Filter by date, product, category, warehouse, or location",
    "Real-time running balance with FIFO/Average valuation",
    "Interactive bar charts and pivot tables",
    "Printable PDF report per product",
    "Zero dependencies: works on clean Odoo CE 18.0/19.0",
]
for i, f in enumerate(features):
    draw.text((80, 300 + i * 32), f"  \u2713  {f}", fill=(255, 255, 255, 190), font=small_font)

footer_font = ImageFont.truetype(FONT, 14)
draw.text((60, 600), "100% Open Source  |  AGPL-3  |  Free Module  |  github.com/FoxPink-dev",
          fill=(255, 255, 255, 100), font=footer_font)

cover.save(os.path.join(BASE, "images", "main_screenshot.png"))
print("main_screenshot.png created (1280x640)")
