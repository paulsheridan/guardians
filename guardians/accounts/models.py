from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings


@python_2_unicode_compatible
class Profile(models.Model):
    """
    Profile model attached to Django's
    built-in User model
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    bio = models.TextField(default='')
    image = models.ImageField(upload_to='/photos/')

    def __str__(self):
        return str(self.user)
