# Generated by Django 5.0.4 on 2024-05-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_consumables_parts_saletool'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время измененния')),
                ('published', models.BooleanField(choices=[(False, 'Не опубликовано'), (True, 'Опубликовано')], default=0, verbose_name='Статус публикации')),
            ],
        ),
        migrations.DeleteModel(
            name='consumables',
        ),
        migrations.DeleteModel(
            name='parts',
        ),
        migrations.DeleteModel(
            name='rentTool',
        ),
        migrations.DeleteModel(
            name='saleTool',
        ),
    ]
