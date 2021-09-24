from django.contrib import admin
from .models import Tab_bords

 



class Tab_bordsAdmin(admin.ModelAdmin):
    list_display = ('date', 'num_mission', 'direction', 'Heure_depart', 'compteur_depart','compteur_arriver','mission','Nom_chauffeur','Accompagnant','Materiels','Lieu_carburant','Quantite_carbu','Num','Heure_retour','validation')
    list_filter = ('num_mission', )
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('num_mission', )
    
    


admin.site.register(Tab_bords, Tab_bordsAdmin)