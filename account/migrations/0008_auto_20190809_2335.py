# Generated by Django 2.2.4 on 2019-08-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190809_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
