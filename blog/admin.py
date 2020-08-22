from django.contrib import admin
# Register your models here.
from .models import Post, Comment,Category,SecondCategory
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(SecondCategory)
admin.site.register(Comment)
