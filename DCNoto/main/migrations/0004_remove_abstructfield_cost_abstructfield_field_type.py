# Generated by Django 4.2.5 on 2023-10-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_documenttype_fields_info_alter_document_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abstructfield',
            name='cost',
        ),
        migrations.AddField(
            model_name='abstructfield',
            name='field_type',
            field=models.CharField(choices=[('int', 'int'), ('str', 'str'), ('date', 'date'), ('float', 'float')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
