# Generated by Django 4.0 on 2024-03-30 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_enquiryform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courier',
            name='serviceArea',
        ),
        migrations.AddField(
            model_name='courier',
            name='serviceArea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='couriers', to='MyApp.servicearea'),
            preserve_default=False,
        ),
    ]
