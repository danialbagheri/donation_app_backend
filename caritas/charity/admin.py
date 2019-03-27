from django.contrib import admin
from .models import Charity
# Register your models here.
admin.site.site_header = 'Caritas'

admin.site.register(Charity)