# Generated by Django 2.2.15 on 2020-09-05 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20200905_1922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadimage',
            options={'ordering': ['-id']},
        ),
    ]
