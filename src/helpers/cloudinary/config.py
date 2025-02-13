import cloudinary
from django.conf import settings

CLOUDINARY_CLOUD_NAME = settings.CLOUDINARY_CLOUD_NAME
CLOUDINARY_API_KEY = settings.CLOUDINARY_API_KEY
CLOUDINARY_SECRET_API_KEY =settings.CLOUDINARY_SECRET_API_KEY


# Configuration  
def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME, 
        api_key = CLOUDINARY_API_KEY, # Click 'Create' in the Cloudinary dashboard to copy your API key
        api_secret = CLOUDINARY_SECRET_API_KEY, # Click 'View API Keys' above to copy your API secret
        secure=True
    )