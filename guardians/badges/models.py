from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Badge(models.Model):
    """
    A user badge model.
    """
    name = models.TextField(default='', max_length=50)
    description = models.TextField(default='', max_length=250)
    image = models.ImageField(upload_to='/badges/')

    def __str__(self):
        return str(self.name)
