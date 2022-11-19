from django.contrib import admin

# Register your models here.
from .models import Operations, Categories, Keywords

admin.site.register(Operations)
admin.site.register(Categories)
admin.site.register(Keywords)
