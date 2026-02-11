import requests
from config import GRAPH_URL, IG_USER_ID, ACCESS_TOKEN


def post_instagram(image_url, caption):
    """
    Upload image to Instagram using Graph API
    """

    if not IG_USER_ID or not ACCESS_TOKEN:
        print("❌ Missing Instagram credentials")
        return False

    try:
        # STEP 1 — Create Media Container
        create_url = f"{GRAPH_URL}/{IG_USER_ID}/media"

        response = requests.post(
            create_url,
            data={
                "image_url": image_url,
                "caption": caption,
                "access_token": ACCESS_TOKEN,
            },
            timeout=30,
        ).json()

        if "id" not in response:
            print("❌ Media creation failed:", response)
            return False

        creation_id = response["id"]
        print("📦 Media container created")

        # STEP 2 — Publish Media
        publish_url = f"{GRAPH_URL}/{IG_USER_ID}/media_publish"

        response = requests.post(
            publish_url,
            data={
                "creation_id": creation_id,
                "access_token": ACCESS_TOKEN,
            },
            timeout=30,
        ).json()

        if "id" in response:
            print("✅ Instagram Post Successful")
            return True

        print("❌ Publish failed:", response)
        return False

    except Exception as e:
        print("❌ Instagram exception:", e)
        return False
