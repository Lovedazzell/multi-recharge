# Generated by Django 4.0.3 on 2022-03-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0006_alter_userfunds_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfunds',
            name='certificate_status',
            field=models.CharField(default='Regular', max_length=80),
        ),
    ]
