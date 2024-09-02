# Generated by Django 5.0.8 on 2024-08-29 19:20

import django.db.models.deletion
import model_utils.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exchanges', '0002_alter_exchange_city_alter_exchange_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('uuid', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', model_utils.fields.StatusField(choices=[('active', 'active'), ('disabled', 'disabled')], default='active', max_length=100, no_check_for_status=True)),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchanges.exchange')),
            ],
        ),
    ]
