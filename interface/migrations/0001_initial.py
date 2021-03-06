# Generated by Django 3.1.5 on 2021-01-20 08:33

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/data'), upload_to='')),
                ('dataset_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_edge_length', models.FloatField()),
                ('homology', models.CharField(max_length=200)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.data')),
            ],
        ),
    ]
