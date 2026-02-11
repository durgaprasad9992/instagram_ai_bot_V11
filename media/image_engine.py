import random
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

IMG_SIZE = (1080, 1080)

# ---------- FONT LOADER (WITH FALLBACK) ----------
def load_font(size):
    try:
        return ImageFont.truetype("fonts/DejaVuSans-Bold.ttf", size)
    except:
        return ImageFont.load_default()


# ---------- DOWNLOAD DYNAMIC BACKGROUND ----------
def download_background():
    sources = [
        "https://picsum.photos/1080/1080",
        "https://source.unsplash.com/1080x1080/?romantic",
        "https://source.unsplash.com/1080x1080/?love",
        "https://source.unsplash.com/1080x1080/?sunset",
        "https://source.unsplash.com/1080x1080/?couple",
    ]

    for _ in range(5):
        try:
            r = requests.get(random.choice(sources), timeout=10)
            return Image.open(BytesIO(r.content)).convert("RGB")
        except:
            continue

    # fallback plain background
    return Image.new("RGB", IMG_SIZE, (20, 20, 35))


# ---------- MAIN IMAGE CREATOR ----------
def create_quote_image(text):
    img = download_background().resize(IMG_SIZE)

    # dark overlay for readability
    overlay = Image.new("RGBA", IMG_SIZE, (0, 0, 0, 140))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

    draw = ImageDraw.Draw(img)
    font = load_font(70)

    # wrap text
    words = text.split()
    lines, line = [], ""

    for word in words:
        test = line + word + " "
        w, _ = draw.textsize(test, font=font)
        if w < 900:
            line = test
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    # vertical center
    total_h = sum(draw.textsize(l, font=font)[1] for l in lines) + (len(lines) * 10)
    y = (1080 - total_h) // 2

    for l in lines:
        w, h = draw.textsize(l, font=font)
        x = (1080 - w) // 2

        # white text with subtle shadow
        draw.text((x+2, y+2), l, font=font, fill=(0,0,0))
        draw.text((x, y), l, font=font, fill=(255,255,255))

        y += h + 10

    filename = "quote.jpg"
    img.save(filename, "JPEG", quality=95)

    return filename
