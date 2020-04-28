from django.contrib import admin

from .models import BookImage, Writer, Book

admin.site.register(BookImage)
admin.site.register(Writer)
admin.site.register(Book)
