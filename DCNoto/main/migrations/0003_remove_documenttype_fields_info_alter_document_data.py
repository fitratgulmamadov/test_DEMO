# Generated by Django 4.2.5 on 2023-10-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_fields_documenttype_fields1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documenttype',
            name='fields_info',
        ),
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
