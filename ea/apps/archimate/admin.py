from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import * 
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Resource, MPTTModelAdmin)
admin.site.register(Catalog)
