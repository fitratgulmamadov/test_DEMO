from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewset)
router.register(r'document_types', DocumentTypeViewset)
router.register(r'fields', FieldViewset)

urlpatterns = [
    path('', include(router.urls)),
]
