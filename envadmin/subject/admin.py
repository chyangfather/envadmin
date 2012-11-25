from django.contrib import admin
#from mptt.admin import MPTTModelAdmin
from models import *

admin.site.register(Subject, admin.ModelAdmin)
admin.site.register(Person, admin.ModelAdmin)
admin.site.register(OrgUnit, admin.ModelAdmin)