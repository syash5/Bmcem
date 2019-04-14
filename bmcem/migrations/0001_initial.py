# Generated by Django 2.1 on 2019-04-14 16:22

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(default='username Should be more than 6 letters,alphanumeric and first letter should be alphabet', max_length=100, unique=True, verbose_name='username')),
                ('full_name', models.CharField(default='', max_length=50)),
                ('dob', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('password', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_no', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50)),
                ('dob', models.DateField(auto_now_add=True)),
                ('last_edu_qualification', models.CharField(default='Please Mention Your Last Educational Qualification', max_length=150)),
                ('applying_for', models.CharField(default='Which Programme You Want To Apply For', max_length=150)),
                ('branch', models.CharField(default='Mention The Branch You Want To Apply For', max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=100)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=254)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Alumini',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('graduation_year', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=100)),
                ('current_org', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('enterpreneur', models.CharField(default='If yes, Please Mention the details about your organisation.', max_length=100)),
                ('other_detail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(default='Body')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desciption', models.TextField()),
                ('created_at', models.TimeField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50)),
                ('contact_no', models.CharField(max_length=100)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=254)),
                ('detail', models.TextField()),
            ],
        ),
    ]
