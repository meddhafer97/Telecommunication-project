from django.db import models
from django.utils.text import slugify 



class Tab_bords(models.Model):
    date = models.DateTimeField(auto_now_add=True, 
                                verbose_name="Date ")
    num_mission = models.IntegerField(default=0, 
                                   verbose_name="num_mission")
    direction = models.CharField(max_length=42)
    Heure_depart = models.DateTimeField(auto_now_add=True, 
                                verbose_name="Heure_depart")
    compteur_depart = models.IntegerField(default=0, 
                                   verbose_name="compteur_depart")
    compteur_arriver = models.IntegerField(default=0, 
                                   verbose_name="compteur_arriver")
    mission = models.CharField(max_length=42)
    Nom_chauffeur= models.CharField(max_length=42)
    Accompagnant= models.CharField(max_length=42)
    Materiels= models.CharField(max_length=42)
    Lieu_carburant= models.CharField(max_length=42)
    Quantite_carbu= models.IntegerField(default=0, 
                                   verbose_name="quantite_carbu")
    Num= models.IntegerField(default=0, 
                                   verbose_name="Nombre ")
    Heure_retour = models.DateTimeField(auto_now_add=True, 
                                verbose_name="Heure_retour")

    validation = models.BooleanField(default=False)
    
    def __str__(self):
        return "[{0}] {1}".format(self.date, self.direction)
    
    def save(self, *args, **kwargs):
        super(Tab_bords, self).save(*args, **kwargs)

    