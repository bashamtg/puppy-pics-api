# Generated by Django 4.0.5 on 2022-07-12 05:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('puppy_pics', '0008_pet_breed_pet_owner_alter_puppypic_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='puppypic',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 12, 5, 56, 14, 220171, tzinfo=utc)),
        ),
    ]
