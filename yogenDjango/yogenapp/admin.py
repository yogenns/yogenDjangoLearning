from django.contrib import admin
from yogenapp.models import Topic,AccessRecord,WebPage
# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
