from collections.abc import Iterable
from django.db import models
from docxtpl import DocxTemplate
from django.core.files.base import ContentFile, File
from datetime import datetime

class AbstructField(models.Model):
    field_name = models.CharField(max_length=150)
    type_choice = [
        ('int', 'int'),
        ('str', 'str'),
        ('date', 'date'),
        ('float', 'float'),
        ]
    required = models.BooleanField(default=True)
    field_type = models.CharField(max_length=100, choices=type_choice)

    def __str__(self) -> str:
        return self.field_name
    

class DocumentType(models.Model):
    doc_name = models.CharField(max_length=150)
    fields1 = models.ManyToManyField(AbstructField, related_name='abs_field')
    template = models.FileField(upload_to='uploads/templates/')
    
    def get_fields(self) -> dict:
        return [{'name': f.field_name, 'type': f.field_type, 'required': f.required} for f in self.fields1.all()]

    def __str__(self) -> str:
        return self.doc_name



class Document(models.Model):
    doc_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    data = models.JSONField()
    rendered_template = models.FileField(upload_to='uploads/rendered/', blank=True, null=True)
    
    
    def save(self, *args, **kwargs) -> None:
        # template create
        doc = DocxTemplate(self.doc_type.template)
        context = self.data
        doc.render(context)
        path_to_save = f'uploads/uploads/rendered/{int(datetime.now().timestamp())}.docx'
        doc.save(path_to_save)
        self.rendered_template = path_to_save

        return super().save(*args, **kwargs)

    
