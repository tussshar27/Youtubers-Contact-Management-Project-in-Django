# Generated by Django 3.1.7 on 2021-03-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
