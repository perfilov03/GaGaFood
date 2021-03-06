# Generated by Django 4.0.5 on 2022-06-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название акции')),
                ('description', models.TextField(verbose_name='Описание акции')),
                ('percent', models.IntegerField(verbose_name='Процент скидки')),
            ],
            options={
                'verbose_name': 'Скидка / акция',
                'verbose_name_plural': 'Скидки и акции',
            },
        ),
    ]
