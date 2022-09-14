# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Inscription(models.Model):
    email = models.CharField(max_length=45)
    username = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'inscription'


class Message(models.Model):
    idmsg = models.AutoField(db_column='idMsg', primary_key=True)  # Field name made lowercase.
    messagef = models.CharField(db_column='MessageF', max_length=500)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=45)
    name = models.CharField(max_length=45)
    phone = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'message'


class Mode(models.Model):
    typemode = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'mode'


class Niveau(models.Model):
    nomniv = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'niveau'


class Personne(models.Model):
    age = models.IntegerField()
    mdp = models.CharField(max_length=45)
    nom = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    sexe = models.CharField(max_length=45)
    username = models.CharField(db_column='Username', primary_key=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personne'


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=16)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'