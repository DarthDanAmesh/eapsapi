from django.contrib import admin

# Register your models here.

from .models import FooModel

admin.site.register(FooModel)
