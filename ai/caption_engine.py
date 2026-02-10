import random

def generate_caption(quote):
    hooks = [
        "Some feelings never leave...",
        "For the one who understands silence ❤️",
        "If this touched you, it was meant for you.",
        "Not everyone will understand this…",
    ]
    return f"{random.choice(hooks)}\n\n{quote}"
