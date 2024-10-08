# Generated by Django 4.1 on 2024-09-27 09:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_service_medspa'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(blank=True, choices=[('FACIAL', 'Facial'), ('INJECTABLES', 'Injectables'), ('PEELS', 'Peels')], max_length=20),
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
