# Generated by Django 4.2.15 on 2024-08-16 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_property_location_property_property_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='image',
            new_name='main_image',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='video',
            new_name='main_video',
        ),
        migrations.CreateModel(
            name='PropertyVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='property_videos/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='properties.property')),
            ],
        ),
    ]
