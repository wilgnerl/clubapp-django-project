# Generated by Django 4.2.2 on 2023-07-01 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_venue_owner_venue_venue_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Aprroved'),
        ),
    ]
