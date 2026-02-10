import time
from config import POST_INTERVAL
from ai.openai_engine import generate_emotional_quote
from ai.caption_engine import generate_caption
from ai.hashtag_engine import get_hashtags
from media.image_engine import create_quote_image
from api.imgbb_api import upload_imgbb
from api.instagram_api import post_instagram

def run_bot():
    print("🚀 V11 GOD MODE Bot Started")

    while True:
        try:
            quote = generate_emotional_quote()
            print("📝", quote)

            img_file = create_quote_image(quote)
            print("🎨 Image ready")

            img_url = upload_imgbb(img_file)
            if not img_url:
                print("Img upload failed")
                time.sleep(60)
                continue

            caption = generate_caption(quote) + "\n\n" + get_hashtags()
            post_instagram(img_url, caption)

        except Exception as e:
            print("Error:", e)

        print("⏳ Next post in 3 hours")
        time.sleep(POST_INTERVAL)
