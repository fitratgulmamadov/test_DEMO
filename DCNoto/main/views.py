from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS 
from .models import *
from .serializers import *
import json
from .validators import *


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def create(self, request, *args, **kwargs):
        post_payloads = request.POST
        doc_type = DocumentType.objects.get(pk=int(post_payloads["doc_type"]))
        # check "data" field for valid json
        try:
            
            doc_fields = doc_type.get_fields()
            
            data = json.loads(post_payloads['data'] if post_payloads['data'] else '{}')
            data_keys = []
            if data: data_keys = data.keys()
            send_fields = match_fields(get_fields=data_keys, has_fields=doc_fields)

            if send_fields:
                return Response(data={'Fields are required!': [{'data': send_fields}]}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'Errors': [{"data": str(e)}]}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)
    
class DocumentTypeViewset(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumetTypeSerializer

class FieldViewset(viewsets.ModelViewSet):
    queryset = AbstructField.objects.all()
    serializer_class = FieldSerializer