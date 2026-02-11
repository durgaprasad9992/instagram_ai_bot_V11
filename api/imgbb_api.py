import requests
import base64
from config import IMGBB_API_KEY


def upload_imgbb(filename):
    """
    Upload image to ImgBB and return public URL
    """

    if not IMGBB_API_KEY:
        print("❌ Missing ImgBB API key")
        return None

    try:
        with open(filename, "rb") as f:
            encoded = base64.b64encode(f.read())

        response = requests.post(
            "https://api.imgbb.com/1/upload",
            data={
                "key": IMGBB_API_KEY,
                "image": encoded,
            },
            timeout=30,
        )

        data = response.json()

        if data.get("success"):
            url = data["data"]["url"]
            print("🌐 ImgBB Upload Success")
            return url

        print("❌ ImgBB failed:", data)
        return None

    except Exception as e:
        print("❌ ImgBB exception:", e)
        return None
