from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Article)
admin.site.register(sportArticle)
admin.site.register(applicationUser)
admin.site.register(articleLikes)
admin.site.register(articleComments)