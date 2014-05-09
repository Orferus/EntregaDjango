from django.contrib import admin
from projects.models import proyectos, tareas

class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio')
    search_fields = ('nombre',)

class ProyectoAdmin(admin.ModelAdmin):	
list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
ordering = ('nombre',)
filter_horizontal = ('tareas',)

admin.site.register(tareas, TareaAdmin)
admin.site.register(proyectos, ProyectoAdmin)