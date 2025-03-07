# Generated by Django 5.1.5 on 2025-02-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CallsCall',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('calling_number', models.BigIntegerField()),
                ('called_number', models.BigIntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'calls_call',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CallsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('called_number', models.CharField(blank=True, max_length=15, null=True)),
                ('caller_number', models.CharField(blank=True, max_length=15, null=True)),
                ('call_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'calls_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CbTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('queue', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personid', models.IntegerField(blank=True, db_column='PersonID', null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=255, null=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Persons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersCustomuser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('username', models.CharField(max_length=50, unique=True)),
                ('allowed_ip', models.CharField(blank=True, max_length=39, null=True)),
                ('is_active', models.IntegerField()),
            ],
            options={
                'db_table': 'users_customuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersCustomuserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'users_customuser_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersCustomuserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'users_customuser_user_permissions',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='cdr',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='cel',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tblservicenetnums',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ussdivr',
            options={'managed': False},
        ),
    ]
