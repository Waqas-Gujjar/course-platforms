import helpers
import uuid
from django.db import models
from cloudinary.models import CloudinaryField 
from django.utils.text import slugify

helpers.cloudinary_init()


# Create your models here.
class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

def handle_upload(instance, filename):
    return f"{filename}"

def generate_public_id(instance, *args, **kwargs):
    title = instance.title
    unique_id = str(uuid.uuid4()).replace("-", "")
    if not title:
        return unique_id
    slug = slugify(title)
    unique_id_short = unique_id[:5]
    return f"{slug}-{unique_id_short}"


def get_public_id_prefix(instance, *args, **kwargs):
    if hasattr(instance, 'path'):
        path = instance.path
        if path.startswith("/"):
            path = path[1:]
        if path.endswith('/'):
            path = path[:-1]
        return path
    public_id = instance.public_id
    model_class = instance.__class__
    model_name = model_class.__name__
    model_name_slug = slugify(model_name)
    if not public_id:
        return f"{model_name_slug}"
    return f"{model_name_slug}/{public_id}"
    
    

def get_display_name(instance , *args, **kwargs):
    if hasattr(instance,'get_display_name'):
        return instance.get_display_name()
    if hasattr(instance,'title'):
        return instance.title
    model_class = instance.__class__
    model_name = model_class.__name__
    return f"{model_name} Uploade"



class Course(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField( null=True, blank=True, )
    # image = models.ImageField(upload_to=handle_upload, null=True, blank=True)
    image = CloudinaryField(
        "image",
        null=True,
        public_id_prefix = get_public_id_prefix,
        display_name = get_display_name,
        tags = ['Course','thumbnail'],
        resource_type='image'
    )  # CloudinaryField for storing images in cloud storage.  # Add 'Pillow' and 'cloudinary' in installed apps.  # Pillow is for image processing, cloudinary is for image storage.  
     
    access = models.CharField(
        max_length=5, 
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    timestamp = models.DateTimeField(auto_now_add=True)  # automatically set when object is created.
    updated = models.DateTimeField(auto_now=True)  # automatically set when object is updated.
    public_id = models.CharField(max_length=130,null=True,blank=True,db_index = True)

    def get_absolute_url(self):
        return self.path
    
    @property
    def path(self):
        return f"/courses/{self.public_id}"
    def get_display_name(self):
        return f"{self.title}-Course"
    
    @property
    def is_published(self):
           return self.status == PublishStatus.PUBLISHED
    
    def save(self,*args, **kwargs):
        if self.public_id == "" or self.public_id is None:
            self.public_id = generate_public_id(self)
        super().save(*args, **kwargs)
    @property
    def admin_image_url(self):
        return helpers.get_cloudinary_image_object(
            self,
            as_html = False,
            width = 500,
            filed_name = 'image'
        )
    

    def get_image_thumbnail(self,as_html=False,width=500):
        return helpers.get_cloudinary_image_object(
            self,
            as_html = as_html,
            width = width,
            filed_name = 'image'
        )
    
    def get_detail_image(self,as_html=False,width=700):
        return helpers.get_cloudinary_image_object(
            self,
            as_html = as_html,
            width = width,
            filed_name = 'image'
        )
    
    


class Lesson(models.Model):
    public_id = models.CharField(max_length=130,null=True,blank=True)
    title = models.CharField(max_length=200)
    discription = models.TextField(null=True, blank=True)
    thumbnail = CloudinaryField("image",
                null=True,
                public_id_prefix = get_public_id_prefix,
                display_name = get_display_name, 
                tags = ["thumbnail",'lesson'],
                blank=True,
                resource_type='image'
    )  # CloudinaryField for storing images in cloud storage.  # Add 'Pillow' and 'cloudinary'
    video = CloudinaryField("video",
            null=True,
            public_id_prefix = get_public_id_prefix,
            display_name = get_display_name,
            type = 'private',
            tags = ['video','lesson'],
            blank=True,
            resource_type='video'
    )  # CloudinaryField for storing videos in cloud storage.  # Add 'Pillow' and 'cloudinary'
    course = models.ForeignKey(Course, on_delete=models.CASCADE )
    status = models.CharField(max_length=20, choices=PublishStatus.choices, default=PublishStatus.PUBLISHED)
    can_preview = models.BooleanField(default=False,help_text="If user cannot access to course, can they seen this? ")
    order = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)  # automatically set when object is created.
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-update_date"]


    def save(self,*args, **kwargs):
        if self.public_id == "" or self.public_id is None:
            self.public_id = generate_public_id(self)
        super().save(*args, **kwargs)

    @property
    def path(self):
        course_path = self.course.path
        if course_path.endswith("/"):
             course_path = course_path[:-1]
        return f"{course_path}/lessons/{self.public_id}"
    def get_display_name(self):
        return f"{self.title}-{self.course.get_display_name()}"
    

    def get_image_thumbnail(self,as_html=False,width=500):
        return helpers.get_cloudinary_image_object(
            self,
            as_html = as_html,
            width = width,
            filed_name = 'image'
        )

