from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import *
class ResourceTypeAdmin(admin.ModelAdmin):
	pass

admin.site.register(Resource, MPTTModelAdmin)
admin.site.register(ResourceType, admin.ModelAdmin)