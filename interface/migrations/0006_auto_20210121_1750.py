# Generated by Django 3.1.5 on 2021-01-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0005_auto_20210120_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.TextField(),
        ),
    ]
