import random
import string

def generate_password(length=12):
    """Generate a random password of specified length using lowercase letters, uppercase letters, and digits."""
    password_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(password_chars) for i in range(length))
    return password
