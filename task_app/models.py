from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = [
        ('D', 'Done'),
        ('P', 'In  progress'),
        ('TBD', 'Not done'),
    ]

    title = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='TBD'
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['due_date']

    def __repr__(self) -> str:
        return "<Task: %s>" % self.title[:20]+'...' if len(self.title) > 21 else self.title

    def __str__(self) -> str:
        return "<Task: %s>" % self.title[:20]+'...' if len(self.title) > 21 else self.title

    def get_absolute_url(self):
        return "/task/%i/" % self.id

