# Generated by Django 2.2.4 on 2019-08-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='area',
            field=models.CharField(choices=[('서울', '서울'), ('부산', '부산'), ('대구', '대구'), ('인천', '인천'), ('광주', '광주'), ('대전', '대전'), ('울산', '울산'), ('세종', '세종'), ('경기도', '경기도'), ('강원도', '강원도'), ('충청북도', '충청북도'), ('충청남도', '충청남도'), ('전라북도', '전라북도'), ('전라남도', '전라남도'), ('경상북도', '경상북도'), ('경상남도', '경상남도'), ('제주도', '제주도')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]
