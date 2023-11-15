from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Uploader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "<Uploader: %s>" % self.user.get_username()

class Level(models.Model):
    class LevelEnum(models.TextChoices):
        ONE = '100'
        TWO = '200'
        THREE = '300'
        FOUR = '400'

    name = models.CharField(
        max_length=5,
        choices=LevelEnum.choices,
        blank=False
        )

    def __str__(self) -> str:
        return "<Level: %s>" % self.name


class Course(models.Model):
    course_code = models.CharField(max_length=7)
    course_title = models.CharField(max_length=50)

    course_level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "<Course: %s>" % self.course_code


class Document(models.Model):
    file_name = models.CharField(max_length=128)
    file_size = models.DecimalField(max_digits=4, decimal_places=2)

    document_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    uploader = models.ForeignKey(Uploader, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "<Document: %s uploaded by %s>" % (self.file_name, self.uploader)
