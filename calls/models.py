from django.db import models


class Persons(models.Model):
    personid = models.IntegerField(db_column='PersonID', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Persons'


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


class CallsCall(models.Model):
    id = models.BigAutoField(primary_key=True)
    calling_number = models.BigIntegerField()
    called_number = models.BigIntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'calls_call'


class CallsData(models.Model):
    called_number = models.CharField(max_length=15, blank=True, null=True)
    caller_number = models.CharField(max_length=15, blank=True, null=True)
    call_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls_data'


class CbTable(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    queue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cb_table'


class Cdr(models.Model):
    calldate = models.DateTimeField()
    callback = models.IntegerField(blank=True, null=True)
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    userfield = models.CharField(max_length=255)
    cnum = models.CharField(max_length=80, blank=True, null=True)
    recordingfile = models.CharField(max_length=255, blank=True, null=True)
    uniqueid = models.CharField(max_length=80, blank=True, null=True)
    extra = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdr'


class Cel(models.Model):
    eventtype = models.CharField(max_length=30)
    eventtime = models.DateTimeField()
    exten = models.CharField(max_length=80)
    context = models.CharField(max_length=80)
    channame = models.CharField(max_length=80)
    appname = models.CharField(max_length=80)
    appdata = models.CharField(max_length=80)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    peer = models.CharField(max_length=80)
    userfield = models.CharField(max_length=255)
    clid = models.CharField(max_length=80, blank=True, null=True)
    cid_num = models.CharField(max_length=80, blank=True, null=True)
    linkedid = models.CharField(max_length=80, blank=True, null=True)
    cid_name = models.CharField(max_length=80, blank=True, null=True)
    cid_dani = models.CharField(max_length=80, blank=True, null=True)
    cid_dnid = models.CharField(max_length=80, blank=True, null=True)
    cid_rdnis = models.CharField(max_length=80, blank=True, null=True)
    cid_ani = models.CharField(max_length=80, blank=True, null=True)
    extra = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cel'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

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


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TblServicenetNums(models.Model):
    personid = models.AutoField(db_column='Personid', primary_key=True)  # Field name made lowercase.
    saxeli = models.CharField(max_length=200)
    gvari = models.CharField(max_length=200)
    piradi_nomeri = models.CharField(max_length=200)
    kompania = models.CharField(max_length=200)
    pozicia = models.CharField(max_length=200)
    regioni = models.CharField(max_length=200)
    numbers = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_servicenet_nums'


class UsersCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=50)
    allowed_ip = models.CharField(max_length=39, blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_customuser'


class UsersCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_customuser_groups'
        unique_together = (('customuser', 'group'),)


class UsersCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class UssdIvr(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ussd = models.CharField(db_column='USSD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ivr = models.CharField(db_column='IVR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ussd_ivr'