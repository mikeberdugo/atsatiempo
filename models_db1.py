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


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Can101Candidato(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    ciudad_id_004 = models.ForeignKey('Cat004Ciudad', models.DO_NOTHING, db_column='ciudad_id_004', blank=True, null=True)
    estado_id_001 = models.ForeignKey('Cat001Estado', models.DO_NOTHING, db_column='estado_id_001')
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'can_101_candidato'


class Can101CandidatoSkills(models.Model):
    candidato_id_101 = models.ForeignKey(Can101Candidato, models.DO_NOTHING, db_column='candidato_id_101')
    skill_id_104 = models.ForeignKey('Can104Skill', models.DO_NOTHING, db_column='skill_id_104')
    nivel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'can_101_candidato_skills'


class Can102Experiencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    entidad = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField(blank=True, null=True)
    activo = models.BooleanField()
    logro = models.TextField(blank=True, null=True)
    candidato_id_101 = models.ForeignKey(Can101Candidato, models.DO_NOTHING, db_column='candidato_id_101', blank=True, null=True)
    estado_id_001 = models.ForeignKey('Cat001Estado', models.DO_NOTHING, db_column='estado_id_001')
    cargo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'can_102_experiencia'


class Can103Educacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    institucion = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicial = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    grado_en = models.BooleanField(blank=True, null=True)
    titulo = models.CharField(max_length=100)
    candidato_id_101 = models.ForeignKey(Can101Candidato, models.DO_NOTHING, db_column='candidato_id_101', blank=True, null=True)
    estado_id_001 = models.ForeignKey('Cat001Estado', models.DO_NOTHING, db_column='estado_id_001')
    carrera = models.CharField(max_length=100)
    ciudad_id_004 = models.ForeignKey('Cat004Ciudad', models.DO_NOTHING, db_column='ciudad_id_004', blank=True, null=True)
    fortaleza_adquiridas = models.TextField()

    class Meta:
        managed = False
        db_table = 'can_103_educacion'


class Can104Skill(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado_id_004 = models.ForeignKey('Cat001Estado', models.DO_NOTHING, db_column='estado_id_004')

    class Meta:
        managed = False
        db_table = 'can_104_skill'


class Cat001Estado(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    sigla = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_001_estado'


class Cat004Ciudad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    departamento_id_003 = models.IntegerField(blank=True, null=True)
    estado_id_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING, db_column='estado_id_001')

    class Meta:
        managed = False
        db_table = 'cat_004_ciudad'


class Cli051Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nit = models.IntegerField()
    razon_social = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=254)
    contacto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    ciudad_id_004 = models.ForeignKey(Cat004Ciudad, models.DO_NOTHING, db_column='ciudad_id_004')
    estado_id_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING, db_column='estado_id_001')
    logo = models.CharField(max_length=100, blank=True, null=True)
    perfil_empresarial = models.TextField()

    class Meta:
        managed = False
        db_table = 'cli_051_cliente'


class Cli052Vacante(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    numero_posiciones = models.IntegerField()
    experiencia_requerida = models.IntegerField()
    funciones_responsabilidades = models.TextField()
    salario = models.IntegerField(blank=True, null=True)
    estado_vacante = models.IntegerField()
    ciudad = models.ForeignKey(Cat004Ciudad, models.DO_NOTHING)
    cliente_id_051 = models.ForeignKey(Cli051Cliente, models.DO_NOTHING)
    estado_id_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    profesion_estudio_id_055 = models.ForeignKey('Cli055ProfesionEstudio', models.DO_NOTHING)
    fecha_creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cli_052_vacante'


class Cli052VacanteHardSkillsId054(models.Model):
    id = models.BigAutoField(primary_key=True)
    cli052vacante = models.ForeignKey(Cli052Vacante, models.DO_NOTHING)
    cli054hardskill = models.ForeignKey('Cli054HardSkill', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cli_052_vacante_hard_skills_id_054'
        unique_together = (('cli052vacante', 'cli054hardskill'),)


class Cli052VacanteSoftSkillsId053(models.Model):
    id = models.BigAutoField(primary_key=True)
    cli052vacante = models.ForeignKey(Cli052Vacante, models.DO_NOTHING)
    cli053softskill = models.ForeignKey('Cli053SoftSkill', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cli_052_vacante_soft_skills_id_053'
        unique_together = (('cli052vacante', 'cli053softskill'),)


class Cli053SoftSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    estado_id_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cli_053_soft_skill'


class Cli054HardSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    estado_id_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cli_054_hard_skill'


class Cli055ProfesionEstudio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    estado_id_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cli_055_profesion_estudio'


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


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Grupo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    activate = models.BooleanField()
    date = models.DateTimeField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupo'


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    primer_nombre = models.CharField(max_length=15, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=15, blank=True, null=True)
    primer_apellido = models.CharField(max_length=15, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    is_verificado = models.BooleanField(blank=True, null=True)
    group = models.ForeignKey(Grupo, models.DO_NOTHING, blank=True, null=True)
    cliente_id_051 = models.ForeignKey(Cli051Cliente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuariobase = models.ForeignKey(Usuario, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario_groups'
        unique_together = (('usuariobase', 'group'),)


class UsuarioUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuariobase = models.ForeignKey(Usuario, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario_user_permissions'
        unique_together = (('usuariobase', 'permission'),)
