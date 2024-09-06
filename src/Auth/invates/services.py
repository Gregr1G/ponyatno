import random
import string


def generate_code():
    return "".join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(25))