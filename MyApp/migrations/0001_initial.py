# Generated by Django 5.0.3 on 2024-03-16 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TravelBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='courier_images/')),
                ('branch', models.CharField(max_length=100)),
                ('serviceArea', models.ManyToManyField(related_name='couriers', to='MyApp.servicearea')),
            ],
        ),
        migrations.CreateModel(
            name='EnquiryForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('courierService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.courier')),
                ('serviceType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.servicetype')),
            ],
        ),
        migrations.CreateModel(
            name='CostTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_wait_per_gram', models.DecimalField(decimal_places=2, max_digits=10)),
                ('from_wait_per_gram', models.DecimalField(decimal_places=2, max_digits=10)),
                ('localRate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cityRate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stateRate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.courier')),
                ('serviceType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.servicetype')),
                ('shipmentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.shipmenttype')),
                ('travelBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.travelby')),
            ],
        ),
    ]