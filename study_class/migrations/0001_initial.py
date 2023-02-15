# Generated by Django 4.1.4 on 2023-02-15 18:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
        ('students', '0003_student_halqa'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyClass',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('class no', models.IntegerField()),
                ('name', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=256)),
                ('Semester no', models.IntegerField()),
                ('moderator', models.CharField(max_length=60)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('was_preasent', models.BooleanField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('study_class', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='study_class.studyclass')),
            ],
        ),
    ]
