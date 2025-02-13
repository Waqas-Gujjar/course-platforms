# Generated by Django 5.1.5 on 2025-02-13 09:37

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=200)),
                ('discription', models.TextField(blank=True, null=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('access', models.CharField(choices=[('any', 'Anyone'), ('email', 'Email required')], default='email', max_length=5)),
                ('status', models.CharField(choices=[('publish', 'Published'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='draft', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('public_id', models.CharField(blank=True, db_index=True, max_length=130, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(blank=True, max_length=130, null=True)),
                ('tittle', models.CharField(max_length=200)),
                ('discription', models.TextField(blank=True, null=True)),
                ('thumbnail', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('video', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='video')),
                ('status', models.CharField(choices=[('publish', 'Published'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='publish', max_length=20)),
                ('can_preview', models.BooleanField(default=False, help_text='If user cannot access to course, can they seen this? ')),
                ('order', models.PositiveIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'ordering': ['order', '-update_date'],
            },
        ),
    ]
