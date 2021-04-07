from django.contrib import admin
from .models import Problems
# Register your models here.

admin.site.site_header = 'PyJudge Admin Panel'

admin.site.register(Problems)