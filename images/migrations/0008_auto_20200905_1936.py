# Generated by Django 2.2.15 on 2020-09-05 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_auto_20200905_1933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadimage',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='social_activity',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Количество людей на фотографии'),
        ),
    ]
