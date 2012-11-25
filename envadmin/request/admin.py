from django.contrib import admin
from models import *

class DictionaryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(Request)
admin.site.register(RequestFactor)
