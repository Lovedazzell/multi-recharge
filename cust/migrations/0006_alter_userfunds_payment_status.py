# Generated by Django 4.0.3 on 2022-03-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0005_alter_userfunds_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfunds',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
