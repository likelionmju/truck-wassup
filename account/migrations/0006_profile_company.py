# Generated by Django 2.2.4 on 2019-08-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
