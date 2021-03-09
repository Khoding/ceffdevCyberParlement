# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Candidat(models.Model):
    idcandidat = models.AutoField(db_column='idCandidat', primary_key=True)  # Field name made lowercase.
    election = models.ForeignKey('Election', models.DO_NOTHING, db_column='idElection')  # Field name made lowercase.
    personne = models.ForeignKey('Personne', models.DO_NOTHING, db_column='idPersonne')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'candidat'
        unique_together = (('election', 'personne'),)


class Choixinitiative(models.Model):
    idchoixinitiative = models.AutoField(db_column='idChoixInitiative', primary_key=True)  # Field name made lowercase.
    initiative = models.ForeignKey('Initiative', models.DO_NOTHING, db_column='idInitiative')  # Field name made lowercase.
    choix = models.CharField(db_column='Choix', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ordre = models.IntegerField(db_column='Ordre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'choixinitiative'


VISIBILITY_PUBLIC_KEY = 'PU'
VISIBILITY_PUBLIC_VALUE = 'Public'

VISIBILITY_PRIVATE_KEY = 'PR'
VISIBILITY_PRIVATE_VALUE = 'Privé'

VISIBILITY_CHOICES = [
    (VISIBILITY_PUBLIC_KEY, VISIBILITY_PUBLIC_VALUE),
    (VISIBILITY_PRIVATE_KEY, VISIBILITY_PRIVATE_VALUE),
]

STATUS_DRAFT_VALUE = 'Brouillon'
STATUS_DRAFT_KEY = 'BR'

STATUS_POSTED_KEY = 'PU'
STATUS_POSTED_VALUE = 'Publié'

STATUS_CHOICES = [
    (STATUS_DRAFT_KEY, STATUS_DRAFT_VALUE),
    (STATUS_POSTED_KEY, STATUS_POSTED_VALUE)
]


class Cyberparlement(models.Model):
    idcyberparlement = models.AutoField(db_column='idCyberParlement', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=45)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # visibilite = models.CharField(db_column='Visibilite', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # statut = models.ForeignKey('Statutensemble', models.DO_NOTHING, db_column='Statut', blank=True, null=True)  # Field name made lowercase.
    visibilite = models.CharField(db_column='Visibilite', max_length=200, choices=VISIBILITY_CHOICES, default=VISIBILITY_PUBLIC_KEY)
    statut = models.CharField(db_column='Statutensemble', max_length=200, choices=STATUS_CHOICES, default=STATUS_DRAFT_KEY)
    cyberparlementparent = models.ForeignKey('self', models.DO_NOTHING, db_column='CPParent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cyberparlement'


class Election(models.Model):
    idelection = models.AutoField(db_column='idElection', primary_key=True)  # Field name made lowercase.
    echeance = models.DateTimeField(db_column='Echeance', blank=True, null=True)  # Field name made lowercase.
    sujet = models.CharField(db_column='Sujet', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'election'


class Forum(models.Model):
    idforum = models.OneToOneField(Cyberparlement, models.DO_NOTHING, db_column='idForum', primary_key=True)  # Field name made lowercase.
    idensemble = models.IntegerField(db_column='idEnsemble', blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    statut = models.CharField(db_column='Statut', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'forum'


class Genrepersonne(models.Model):
    genre = models.CharField(db_column='Genre', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'genrepersonne'


class Initiative(models.Model):
    idinitiative = models.AutoField(db_column='idInitiative', primary_key=True)  # Field name made lowercase.
    cyberparlement = models.ForeignKey(Cyberparlement, models.DO_NOTHING, db_column='idCP')  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000)  # Field name made lowercase.
    echeance = models.DateTimeField(db_column='Echeance')  # Field name made lowercase.
    initiateur = models.ForeignKey('Personne', models.DO_NOTHING, db_column='idInitiateur', blank=True, null=True)  # Field name made lowercase.
    statut = models.ForeignKey('Statutinitiative', models.DO_NOTHING, db_column='Statut', blank=True, null=True)  # Field name made lowercase.
    modevalidation = models.ForeignKey('Modevalidation', models.DO_NOTHING, db_column='ModeValidation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'initiative'


ROLE_CYBERCHANCELIER_KEY = 'CC'
ROLE_CYBERCHANCELIER_VALUE = 'CyberChancelier'

ROLE_MEMBER_KEY = 'ME'
ROLE_MEMBER_VALUE = 'Membre'

ROLE_CHOICES = [
    (ROLE_CYBERCHANCELIER_KEY, ROLE_CYBERCHANCELIER_VALUE),
    (ROLE_MEMBER_KEY, ROLE_MEMBER_VALUE)
]


class Membrecp(models.Model):
    idmembrecyberparlement = models.AutoField(db_column='idMembreCP', primary_key=True)  # Field name made lowercase.
    personne = models.ForeignKey('Personne', models.DO_NOTHING, db_column='idPersonne')  # Field name made lowercase.
    cyberparlement = models.ForeignKey(Cyberparlement, models.DO_NOTHING, db_column='idCyberParlement')  # Field name made lowercase.
    # rolemembrecyberparlement = models.ForeignKey('Rolemembrecp', models.DO_NOTHING, db_column='RoleCP')  # Field name made lowercase.
    rolemembrecyberparlement = models.CharField(db_column='RoleCP', max_length=200, choices=ROLE_CHOICES, default=ROLE_MEMBER_KEY)

    class Meta:
        managed = True
        db_table = 'membrecp'
        unique_together = (('idmembrecyberparlement', 'personne'),)


class Message(models.Model):
    idmessage = models.AutoField(db_column='idMessage', primary_key=True)  # Field name made lowercase.
    forum = models.ForeignKey(Forum, models.DO_NOTHING, db_column='idForum', blank=True, null=True)  # Field name made lowercase.
    auteur = models.ForeignKey('Personne', models.DO_NOTHING, db_column='idAuteur', blank=True, null=True)  # Field name made lowercase.
    contenu = models.CharField(db_column='Contenu', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'message'


class Modevalidation(models.Model):
    modevaltexte = models.CharField(db_column='ModeValTexte', primary_key=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'modevalidation'


class Personne(models.Model):
    idpersonne = models.AutoField(db_column='idPersonne', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=45)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=45)  # Field name made lowercase.
    genre = models.ForeignKey(Genrepersonne, models.DO_NOTHING, db_column='Genre', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=45, blank=True, null=True)  # Field name made lowercase.
    npa = models.IntegerField(db_column='NPA', blank=True, null=True)  # Field name made lowercase.
    localite = models.CharField(db_column='Localite', max_length=45)  # Field name made lowercase.
    statut = models.ForeignKey('Statutpersonne', models.DO_NOTHING, db_column='Statut', blank=True, null=True)  # Field name made lowercase.
    datenaissance = models.DateField(db_column='DateNaissance', blank=True, null=True)  # Field name made lowercase.
    notel = models.CharField(db_column='NoTel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'personne'


# class Rolemembrecp(models.Model):
#     rolecyberparlement = models.CharField(db_column='RoleCP', primary_key=True, max_length=45)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'rolemembrecp'


# class Statutensemble(models.Model):
#     statuttexte = models.CharField(db_column='StatutTexte', primary_key=True, max_length=45)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'statutensemble'


class Statutinitiative(models.Model):
    statuttexte = models.CharField(db_column='StatutTexte', primary_key=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'statutinitiative'


class Statutpersonne(models.Model):
    statuttexte = models.CharField(db_column='StatutTexte', primary_key=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'statutpersonne'


class Voteelection(models.Model):
    idelection = models.OneToOneField(Election, models.DO_NOTHING, db_column='idElection', primary_key=True)  # Field name made lowercase.
    personne = models.ForeignKey(Personne, models.DO_NOTHING, db_column='idPersonne')  # Field name made lowercase.
    candidat = models.ForeignKey(Candidat, models.DO_NOTHING, db_column='idCandidat', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'voteelection'
        unique_together = (('idelection', 'personne'),)


class Voteinitiative(models.Model):
    idvoteinitiative = models.AutoField(db_column='idVoteInitiative', primary_key=True)  # Field name made lowercase.
    personne = models.ForeignKey(Personne, models.DO_NOTHING, db_column='idPersonne')  # Field name made lowercase.
    choixinitiative = models.ForeignKey(Choixinitiative, models.DO_NOTHING, db_column='idChoixInitiative', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    initiative = models.ForeignKey(Initiative, models.DO_NOTHING, db_column='idInitiative')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'voteinitiative'
        unique_together = (('personne', 'initiative'),)
