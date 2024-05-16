# Generated by Django 5.0.4 on 2024-05-15 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0009_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='oldPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='tool',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tools', to='shop_app.category'),
        ),
    ]