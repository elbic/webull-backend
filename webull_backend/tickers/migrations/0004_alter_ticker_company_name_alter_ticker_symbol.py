# Generated by Django 5.0.8 on 2024-09-02 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0003_rename_company_ticker_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='company_name',
            field=models.CharField(blank=True, help_text='Company Name', max_length=50, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='symbol',
            field=models.CharField(blank=True, help_text='Symbol', max_length=50),
        ),
    ]
