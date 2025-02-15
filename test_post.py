import os
from instagram_post_service2 import InstagramPostService
from image_uploader import ImageUploader

script_dir = os.path.dirname(os.path.abspath(__file__))

image = os.path.join(script_dir, 'sandeco.png')

upload = ImageUploader()
image_cloud = upload.upload_from_path(image)

caption = "sandeco"

instagram = InstagramPostService()

url = image_cloud['url']

response = instagram.post_image(url, caption)

i = 0
