# Generated by Django 4.2.5 on 2023-10-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_abstructfield_required_document_rendered_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]
