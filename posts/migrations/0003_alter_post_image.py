# Generated by Django 5.1 on 2024-08-15 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_htbmpw.jpg', upload_to='images/'),
        ),
    ]
