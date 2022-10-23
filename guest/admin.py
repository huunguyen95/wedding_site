from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.

class guest_list(admin.ModelAdmin):
    list_display = models.guest_list

admin.site.register(models.Guest, guest_list)