from django.db import models
from mptt.models import MPTTModel

# Create your models here.
#class Product(models.Model):
#     title          = models.CharField(max_length=100)
#     description     = models.TextField()
#     image_url     = models.CharField(max_length=200)
#     price          = models.DecimalField(max_digits=8,decimal_places=2)
class Category(MPTTModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
    def __unicode__(self):
        return self.name

class Resource(MPTTModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
    res_type = models.ForeignKey(Category)
    def __unicode__(self):
        return self.name

class Catalog(models.Model):
    name = models.CharField(max_length=50)
#    resources = mo
