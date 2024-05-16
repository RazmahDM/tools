# Generated by Django 5.0.4 on 2024-05-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_alter_tool_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tool',
            options={'ordering': ['id']},
        ),
        migrations.AddIndex(
            model_name='tool',
            index=models.Index(fields=['id'], name='shop_app_to_id_a489c6_idx'),
        ),
    ]