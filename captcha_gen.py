from captcha.image import ImageCaptcha
import random
import string

image = ImageCaptcha(width=160, height=60)

for i in range(100):
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    image.write(text, f"data/{text}.png")
