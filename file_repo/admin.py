from django.contrib import admin
from .models import Course, Document, Level, Uploader

# Register your models here.
app_models = [Course, Document, Level, Uploader]
admin.site.register(model_or_iterable=app_models)