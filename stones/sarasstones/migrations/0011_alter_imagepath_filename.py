# Generated by Django 3.2.6 on 2021-08-31 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarasstones', '0010_auto_20210831_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepath',
            name='filename',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
