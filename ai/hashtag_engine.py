import random

TAGS = [
    "#love", "#deep", "#heart", "#soul", "#romantic",
    "#emotional", "#writers", "#poetry", "#feelings",
    "#relationship", "#couple", "#mindset", "#viral"
]

def get_hashtags():
    return " ".join(random.sample(TAGS, 8))
