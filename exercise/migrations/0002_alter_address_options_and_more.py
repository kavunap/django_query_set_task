# Generated by Django 4.0 on 2022-04-12 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={},
        ),
        migrations.RemoveField(
            model_name='address',
            name='polymorphic_ctype',
        ),
    ]
