from django.contrib import admin

# Register your models here.
# Register your models here.
from . import models
admin.site.register(models.Visitor)
admin.site.register(models.Visitee)
admin.site.register(models.Organization)
