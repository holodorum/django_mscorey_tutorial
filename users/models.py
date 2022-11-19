from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    #For s3 this will give some issue. We can do it with an AWS lambda function. 
    #TODO
    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs) #This is the method that will be run from model.Models, however we want to slim the saved photo down with pillow
        
    #     img =  Image.open(self.image.path)

    #     if img.height > 300 or  img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)