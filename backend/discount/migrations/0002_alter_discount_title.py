# Generated by Django 4.0.5 on 2022-06-23 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название акции или скидки'),
        ),
    ]
