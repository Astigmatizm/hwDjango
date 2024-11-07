# Generated by Django 5.0.6 on 2024-10-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0009_bb__content_rendered_alter_bb_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to=' images/%Y/%m/%d/', verbose_name='Изображение')),
                ('decs', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.AddField(
            model_name='bb',
            name='img',
            field=models.ImageField(blank=True, upload_to=' images/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]
