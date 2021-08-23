from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    # Basically extending attributes to the default User from django
    # Impportant to use the OneToOneField
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Additional attributes to the form

    # If someone wants to post their website they can and if not
    # then they have the option to leave it blank
    portfolio_site = models.URLField(blank=True)

    # blank=True they won't get an error if they don't want to upload a pic right now
    # 'profile_pics' - the pic will be uploaded and saved to that directory under the media directory
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
        # username is a default of User
