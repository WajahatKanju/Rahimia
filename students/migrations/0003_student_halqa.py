# Generated by Django 4.1.4 on 2023-02-15 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrative_divisions', '0001_initial'),
        ('students', '0002_remove_student_halqa'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='halqa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='administrative_divisions.halqa'),
        ),
    ]