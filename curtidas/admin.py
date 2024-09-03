from django.contrib import admin
from .models import Curtida
# Register your models here.
@admin.register(Curtida)
class CurtidaAdmin(admin.ModelAdmin):      
    list_display = ('publicacao', 'usuario','data_criacao')
    search_fields = ('usuario','publicacao')
    list_filter = ('data_criacao','usuario')