from django.contrib import admin
from .models import Blog
from django.db import models


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/Author", {"fields":["blog_title","blog_author"]}),
		("Content/Date",{"fields":["blog_content","blog_published"]})
	]

admin.site.register(Blog, BlogAdmin)