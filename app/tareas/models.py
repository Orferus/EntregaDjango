from django.db import models

class proyectos(models.Model):
	nombre = models.CharField(max_length=100)
    tarea = models.ManyToManyField(tareas)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    responsable_proyecto=models.DateField(blank=True, null=True, max_length=400)
    #se dejan blank en true y null porque puede no tener fecha de fin aun. 
    #Se pueden agregar mas pero estos son los necesarios
    def __unicode__(self):
        return self.name
    #Para el ordenamiento se hace por el nombre debido a que es mas sencillo que buscar por fecha de inicio 
    #y la final no siempre esta definida
    class Meta:
        ordering = ['nombre']

class tareas(models.Model):
	#Las tareas van a ocupar tres campos elementales en la base de datos
    nombre = models.CharField(max_length=150)
    fecha_inicio= models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    responsable_tarea= models.CharField(blank=True, null=True, max_length=400)
    descripcion_tarea= models.CharField(blank=True, null=True, max_length=400)

    #se dejan blank en true y null porque puede no tener fecha de fin aun. 
    #Se pueden agregar mas pero estos son los necesarios

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['nombre']

