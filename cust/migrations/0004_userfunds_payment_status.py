# Generated by Django 4.0.3 on 2022-03-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0003_userfunds_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfunds',
            name='payment_status',
            field=models.BooleanField(default=True),
        ),
    ]
