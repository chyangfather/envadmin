from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import *
class ResourceTypeAdmin(admin.ModelAdmin):
	pass

admin.site.register(ResourceType, MPTTModelAdmin)
admin.site.register(AttributeDef, admin.ModelAdmin)
admin.site.register(Resource, MPTTModelAdmin)