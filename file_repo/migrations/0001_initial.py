# Generated by Django 4.2.6 on 2023-10-30 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=7)),
                ('course_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('100', 'One'), ('200', 'Two'), ('300', 'Three'), ('400', 'Four')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Uploader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=128)),
                ('file_size', models.DecimalField(decimal_places=2, max_digits=4)),
                ('document_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_repo.course')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_repo.uploader')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_repo.level'),
        ),
    ]