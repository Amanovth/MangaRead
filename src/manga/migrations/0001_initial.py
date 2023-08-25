# Generated by Django 4.2.4 on 2023-08-24 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import src.base.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип манга',
                'verbose_name_plural': 'Типы манга',
            },
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Название манги')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
                ('poster', models.ImageField(upload_to='posters', verbose_name='Постер')),
                ('synopsis', models.TextField(verbose_name='Синопсис')),
                ('genre', models.ManyToManyField(to='manga.genre', verbose_name='Жанры')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Манга',
                'verbose_name_plural': 'Манга',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=src.base.services.get_path_upload_image, validators=[src.base.services.validate_size_image], verbose_name='Изображения')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='manga.manga')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображение',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='manga.manga', verbose_name='Манга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]