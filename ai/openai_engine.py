from openai import OpenAI
from config import OPENAI_API_KEY
import random

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_emotional_quote():
    prompt = """
Write ONE deeply emotional, romantic, poetic sentence.
Human-like, touching, intimate, soulful.
Maximum 16 words.
"""

    try:
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.95,
        )
        return r.choices[0].message.content.strip()
    except:
        return random.choice([
            "You stayed in my silence long after your voice left.",
            "My heart learned your name before it learned fear.",
            "Even distance whispers your memory into my soul."
        ])
