# Generated by Django 4.0.1 on 2022-01-25 13:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20, null=True)),
                ('maximum_number_of_students', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'school',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('registration_number', models.CharField(default=uuid.uuid4, max_length=20, null=True, unique=True)),
                ('school', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='student_school.school')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
