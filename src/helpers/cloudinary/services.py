from django.template.loader import get_template
from django.conf import settings





def get_cloudinary_image_object(instance,
                          as_html=False,
                          width=500,
                          filed_name = 'image'):
    if not hasattr(instance, filed_name):
          return ""
    image_object = getattr(instance,filed_name)
    if not image_object:
          return ""
    image_options ={
            "width":width
    }
    if as_html:
          return instance.image.image(**image_options)
    url = image_object.build_url(**image_options)
    return url
    
video_html = """


"""

def get_cloudinary_video_object(instance,
                          as_html=False,    
                          height=None,
                          width=None,
                          quality="auto",
                          fetch_format="auto",
                          signal_url=False,
                          filed_name = 'video',
                          controls = True,
                          autoplay = True,
                          
                          ):
    
    if not hasattr(instance, filed_name):
          return ""
    video_object = getattr(instance,filed_name)
    if not video_object:
          return ""
    video_options ={
           'fetch_format':fetch_format,
           'signal_url': signal_url,
           'quality':quality,  
           "controls" : controls,
           "autoplay ":  autoplay,
    }
    if height is not None:
          video_options['height']=height
    if width is not None:
          video_options['width']=width
    if height and width:
          video_options['crop'] = 'limit'
    url = video_object.build_url(**video_options)
    if as_html:
          template_name ="videos/snippets/embed.html"
          template = get_template(template_name)
          cloud_name = settings.CLOUDINARY_CLOUD_NAME
          _html = template.render({'video_url': url, 'cloud_name': cloud_name  })
          return _html
    return url
    
    