from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


# Create your models here.
class Profile(models.Model):
    image = models.ImageField(default='profile_pics/defaultpic.png', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 168:
            output_size = (168, 168)
            img.thumbnail(output_size)
            img.save(self.image.path)


def create_profile(sender, **kwarg):
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])


post_save.connect(create_profile, sender=User)
