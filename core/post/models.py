from django.db import models

from core.abstract.models import AbstractModel, AbstractManager

def post_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/post_<id>/<filename>
    return "user_{0}/{1}".format(instance.public_id, filename)

class PostManager(AbstractManager):
    pass


class Post(AbstractModel):
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to=post_directory_path)
    
    objects = PostManager()

    def __str__(self):
        return f"{self.author.name}"