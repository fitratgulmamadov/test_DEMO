from django.contrib import admin
from .models import *


admin.site.register([AbstructField])

# @admin.register(DocumentType)
# class DocumentTypeAdmin(admin.ModelAdmin):
#     list_display = ['doc_name', 'get_fields']
#     # pass

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('doc_name', )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
   readonly_fields = ('rendered_template', )