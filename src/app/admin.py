from django.contrib import admin

from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category)
