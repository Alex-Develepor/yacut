import random
import string

from settings import MAX_RANDOM_LENGTH

from .models import URLMap


def get_uniq_short_id():
    link = ''
    random_list = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.randint(0, 9)
    ]
    for _ in range(MAX_RANDOM_LENGTH):
        link = link + str(random_list[(random.randint(0, 2))])
    if URLMap.query.filter_by(short=link).first():
        return get_uniq_short_id()
    return link
