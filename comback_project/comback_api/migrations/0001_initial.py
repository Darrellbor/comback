# Generated by Django 2.0.7 on 2018-09-22 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(error_messages={'non_field_errors': ['Invalid email address']}, max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('linked_to', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('linked_to', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('customer', 'Regular'), ('staff', 'Inhouse')], default='customer', max_length=2)),
                ('date_made', models.DateField(auto_now_add=True)),
                ('anonymous', models.BooleanField(default=False)),
                ('made_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comback_api.Business')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('date_made', models.DateField(auto_now_add=True)),
                ('anonymous', models.BooleanField(default=False)),
                ('made_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comback_api.Business')),
            ],
        ),
        migrations.CreateModel(
            name='AdminBusProfile',
            fields=[
                ('user', models.OneToOneField(limit_choices_to={'is_admin': True}, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='admin_bus_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=2)),
                ('verified', models.BooleanField(default=False)),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comback_api.Business')),
            ],
            options={
                'abstract': False,
            },
            bases=('comback_api.user',),
        ),
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('user', models.OneToOneField(limit_choices_to={'is_superuser': True}, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='comback_admin_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=2)),
                ('verified', models.BooleanField(default=False)),
                ('date_registered', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('comback_api.user',),
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('user', models.OneToOneField(limit_choices_to={'is_customer': True}, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='customer_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=2)),
                ('verified', models.BooleanField(default=False)),
                ('date_registered', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('comback_api.user',),
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('user', models.OneToOneField(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='staff_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=2)),
                ('verified', models.BooleanField(default=False)),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comback_api.Business')),
            ],
            options={
                'abstract': False,
            },
            bases=('comback_api.user',),
        ),
        migrations.AddField(
            model_name='appeal',
            name='complain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comback_api.Complain'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='made_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comback_api.CustomerProfile'),
        ),
        migrations.AddField(
            model_name='complain',
            name='made_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comback_api.CustomerProfile'),
        ),
    ]
