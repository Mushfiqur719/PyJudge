from django.contrib import admin
from .models import Problems,Submissions
# Register your models here.

admin.site.site_header = 'PyJudge Admin Panel'

admin.site.register(Problems)
admin.site.register(Submissions)