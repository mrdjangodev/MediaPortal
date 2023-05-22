# Generated by Django 4.2.1 on 2023-05-22 08:37

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nomi')),
                ('shortly_description', models.TextField(max_length=200, verbose_name='qisqacha izoh')),
                ('image', models.ImageField(upload_to='chances/', verbose_name='rasm')),
                ('responsible_person', models.CharField(max_length=60, verbose_name='Masul shaxs')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Izoh')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Imkoniyat',
                'verbose_name_plural': 'Imkoniyatlar',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='nomi')),
                ('shortly_description', models.TextField(max_length=200, verbose_name='qisqacha izoh')),
                ('image', models.ImageField(upload_to='chances/', verbose_name='rasm')),
                ('responsible_person', models.CharField(max_length=60, verbose_name='Masul shaxs')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Izoh')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('viewers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name="Ko'ruvchilar")),
            ],
            options={
                'verbose_name': 'Loyiha',
                'verbose_name_plural': 'Loyihalar',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nomi')),
                ('image', models.ImageField(upload_to='news/', verbose_name='rasm')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Izoh')),
                ('uploaded_by', models.CharField(max_length=60, verbose_name='Yuklovchi shaxs')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('viewers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name="Ko'ruvchilar")),
            ],
            options={
                'verbose_name': 'Yangilik',
                'verbose_name_plural': 'Yangiliklar',
            },
        ),
    ]