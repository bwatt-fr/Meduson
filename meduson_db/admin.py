from django.contrib import admin
from meduson_db.models import Materiel
from meduson_db.models import Domaine
from meduson_db.models import Personne
from meduson_db.models import Type
from meduson_db.models import Accessoire
from meduson_db.models import Client
from meduson_db.models import Periode
from meduson_db.models import Periode_Projet
from meduson_db.models import Projet
from meduson_db.models import Liste_Materiel
from meduson_db.models import Location_Materiel
from meduson_db.models import Prestation
from meduson_db.models import Location_Prestation
from meduson_db.models import Devis_Societe
from meduson_db.models import Devis_Association
from meduson_db.models import Facture_Societe
from meduson_db.models import Facture_Association
from meduson_db.models import Reparation

admin.site.register(Domaine)
admin.site.register(Type)
admin.site.register(Personne)

class AccessoireInline(admin.StackedInline):
    model = Accessoire
    extra = 5

class MaterielAdmin(admin.ModelAdmin):
    inlines = [AccessoireInline]

admin.site.register(Materiel,MaterielAdmin)
admin.site.register(Reparation)
admin.site.register(Client)

class PeriodeProjetInline(admin.StackedInline):
    model = Periode_Projet
    extra = 5

class ProjetAdmin(admin.ModelAdmin):
    inlines = [PeriodeProjetInline]

admin.site.register(Projet,ProjetAdmin)
admin.site.register(Liste_Materiel)
admin.site.register(Prestation)

class LocationMaterielInline(admin.StackedInline):
    model = Location_Materiel
    extra = 5

class LocationPrestationInline(admin.StackedInline):
    model = Location_Prestation
    extra = 3

class DevisFactureAdmin(admin.ModelAdmin):
    inlines = [LocationMaterielInline,LocationPrestationInline]

admin.site.register(Devis_Societe,DevisFactureAdmin)
admin.site.register(Devis_Association,DevisFactureAdmin)
admin.site.register(Facture_Societe,DevisFactureAdmin)
admin.site.register(Facture_Association,DevisFactureAdmin)

