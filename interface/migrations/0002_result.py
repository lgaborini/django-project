# Generated by Django 3.1.5 on 2021-01-20 09:37

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/results'), upload_to='')),
                ('diagram', models.JSONField()),
                ('parameters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.parameters')),
            ],
        ),
    ]
