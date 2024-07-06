from django.contrib import admin
from .models import Video_model, User, Comment

admin.site.register(Video_model)
admin.site.register(User)
admin.site.register(Comment)