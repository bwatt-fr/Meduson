from django.contrib import admin
from medusonApp.models import Materiel
from medusonApp.models import Domaine
from medusonApp.models import Personne
from medusonApp.models import Type
from medusonApp.models import Accessoire
from medusonApp.models import Client
from medusonApp.models import Periode
from medusonApp.models import Periode_Projet
from medusonApp.models import Projet
from medusonApp.models import Liste_Materiel
from medusonApp.models import Location_Materiel
from medusonApp.models import Prestation
from medusonApp.models import Location_Prestation
from medusonApp.models import Devis_Societe
from medusonApp.models import Devis_Association
from medusonApp.models import Facture_Societe
from medusonApp.models import Facture_Association
from medusonApp.models import Reparation

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



class DevisAdmin(admin.ModelAdmin):
    inlines = [LocationMaterielInline,LocationPrestationInline]

class FactureAdmin(admin.ModelAdmin) :
    inlines = [LocationMaterielInline,LocationPrestationInline]

admin.site.register(Devis_Societe,DevisAdmin)
admin.site.register(Devis_Association,DevisAdmin)
admin.site.register(Facture_Societe,FactureAdmin)
admin.site.register(Facture_Association,FactureAdmin)

