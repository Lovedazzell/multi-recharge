# Generated by Django 4.0.3 on 2022-03-27 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0012_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='profile.jpg', upload_to=''),
        ),
    ]
