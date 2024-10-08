# Generated by Django 5.0.8 on 2024-09-02 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchanges', '0002_alter_exchange_city_alter_exchange_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='description',
            field=models.CharField(blank=True, help_text='MARKET NAME-INSTITUTION DESCRIPTION', max_length=50),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='mic',
            field=models.CharField(blank=True, help_text='Market Identifier Code', max_length=50, verbose_name='Market Identifier Code'),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='website',
            field=models.URLField(blank=True, help_text='Website'),
        ),
    ]
