# Generated by Django 2.2.16 on 2023-01-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230118_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавить картинку', upload_to='posts/', verbose_name='Картинка'),
        ),
    ]
