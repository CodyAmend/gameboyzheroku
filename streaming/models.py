from django.db import models
from django.urls import reverse
from django.conf import settings
from decimal import Decimal
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
# Create your models here.

class Stream(models.Model):

    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'stream'
        verbose_name_plural = 'streams'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('streaming:streams',
                       args=[self.slug])