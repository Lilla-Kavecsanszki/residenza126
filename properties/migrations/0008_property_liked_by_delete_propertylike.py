# Generated by Django 4.2.15 on 2024-08-18 13:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0007_alter_property_options_propertylike'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_properties', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='PropertyLike',
        ),
    ]
