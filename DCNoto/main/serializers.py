from rest_framework import serializers
from .models import *
import json




class DocumentSerializer(serializers.ModelSerializer):
    doc_fields = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ('doc_type', 'data', 'doc_fields', 'rendered_template')
        read_only_fields = ('rendered_template', )

    @classmethod
    def get_doc_fields(self, object):
       return object.doc_type.get_fields()



class DocumetTypeSerializer(serializers.ModelSerializer):
    doc_fields = serializers.SerializerMethodField()
    
    class Meta:
        model = DocumentType
        fields = ('doc_name', 'template', 'doc_fields', 'fields1')
        
    @classmethod
    def get_doc_fields(self, object):
       return object.get_fields()
    
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstructField
        fields = '__all__'