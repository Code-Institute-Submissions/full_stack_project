# Generated by Django 2.0.4 on 2018-05-16 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0009_auto_20180516_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]