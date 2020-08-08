from django.contrib import admin
from yogenapp.models import Topic,AccessRecord,WebPage,Users,UserProfileInfo
# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(Users)
admin.site.register(UserProfileInfo)
