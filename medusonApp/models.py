from django.db import models
from datetime import timedelta

# Create your models here.

class Personne(models.Model):
    nom = models.CharField(max_length = 80)
    prenom = models.CharField(max_length = 80)
    email = models.EmailField(max_length = 50, blank=True)
    telephone = models.CharField(max_length = 20, blank=True)

    def __unicode__(self):
        return self.prenom + ' ' + self.nom

class Type(models.Model):
    nom = models.CharField(max_length = 50)
    code = models.IntegerField(max_length=3,primary_key=True)
    abreviation = models.CharField(max_length=50,blank=True)

    def __unicode__(self):
        return self.nom


class Domaine(models.Model):
    nom = models.CharField(max_length = 20)
    code = models.CharField(max_length = 1,primary_key=True)
    
    def __unicode__(self):
        return self.nom

class Materiel(models.Model):
    ETAT_CHOICE=(
            ('OK','Ok'),
            ('AR','A reparer'),
            ('EM','En maintenance'),
            ('DO','Douteux'),
            ('MO','Mort'),
            )
    reference_meduson = models.CharField(max_length=8,primary_key=True)
    domaine = models.ManyToManyField(Domaine)
    pays = models.CharField(max_length=50,blank=True)
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50,blank=True)
    numero_serie = models.CharField(max_length=20,blank=True)
    annee = models.CharField(max_length=4)
    proprietaire = models.ForeignKey(Personne)
    valeur = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    prix_location_jour=models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    commentaire = models.CharField(max_length=300,blank=True)
    etat = models.CharField(max_length=2,choices=ETAT_CHOICE)
    type = models.ForeignKey(Type)
    
    def __unicode__(self):
        return self.reference_meduson

class Accessoire(models.Model):
    nom = models.CharField(max_length = 50)
    materiel = models.ForeignKey(Materiel)
    
    def __unicode__(self):
        return self.nom

class Client(models.Model):
    numero = models.CharField(max_length=7,primary_key=True)
    societe = models.CharField(max_length=50)
    nom = models.CharField(max_length=50,blank=True)
    prenom = models.CharField(max_length=50,blank=True)
    adresse_postale = models.CharField(max_length=100,blank=True)
    ville = models.CharField(max_length=100,blank=True)
    code_postal = models.CharField(max_length=10,blank=True)
    pays = models.CharField(max_length=50,blank=True)
    telephone1 = models.CharField(max_length=20,blank=True)
    telephone2 = models.CharField(max_length=20,blank=True)
    abreviation = models.CharField(max_length=50)

    def __unicode__(self):
        return self.societe

class Periode(models.Model):
    debut = models.DateField()
    fin = models.DateField()

    def __unicode__(self):
        return str(self.debut) + ' - ' + str(self.fin)


class Projet(models.Model):
    client = models.ForeignKey(Client)
    referent = models.ForeignKey(Personne)

    def __unicode__(self):
        return self.client.societe + ' - ' + str(self.id)

class Periode_Projet(Periode):
    projet = models.ForeignKey(Projet)

class Liste_Materiel(models.Model):
    projet = models.ForeignKey(Projet)
    materiel = models.ManyToManyField(Materiel)
    periode = models.ForeignKey(Periode)

    def __unicode__(self):
        return self.projet.client.societe + ' - ' + str(self.periode.debut) + '-' +str(self.periode.fin)



class Devis_Facture(models.Model):
    domaine = models.ForeignKey(Domaine)
    projet = models.ForeignKey(Projet)
    date = models.DateField()
    date_paiement = models.DateField()
    totalHT = models.DecimalField(max_digits=10,decimal_places=2)
    acompte = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    paye = models.BooleanField()
   

class Location_Materiel(models.Model):
    materiel = models.ForeignKey(Materiel)
    devis_facture = models.ForeignKey(Devis_Facture)
    remise = models.IntegerField(blank=True,null=True)
    quantite = models.IntegerField()
    nb_jour = models.IntegerField()

class Prestation(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10,decimal_places=2)

class Location_Prestation(models.Model):
    devis_facture = models.ForeignKey(Devis_Facture)
    prestation = models.ForeignKey(Prestation)
    quantite = models.IntegerField()

class Devis_Societe(Devis_Facture):
    id_spec = models.AutoField(unique=True,primary_key=True)

    def __unicode__(self):
        return 'DEVS'+str(self.id_spec)

class Devis_Association(Devis_Facture):
    id_spec = models.AutoField(unique=True,primary_key=True)
    
    def __unicode__(self):
        return 'DEVA'+str(self.id_spec)


class Facture_Societe(Devis_Facture):
    id_spec = models.AutoField(unique=True,primary_key=True)
    
    def __unicode__(self):
        return 'FACS'+str(self.id_spec)

class Facture_Association(Devis_Facture):
    id_spec = models.AutoField(unique=True,primary_key=True)
    
    def __unicode__(self):
        return 'FACA'+str(self.id_spec)

class Reparation(models.Model):
    date = models.DateField()
    commentaire = models.CharField(max_length = 200)
    materiel = models.ForeignKey(Materiel)
