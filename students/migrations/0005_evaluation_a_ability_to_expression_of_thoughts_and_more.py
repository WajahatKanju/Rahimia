# Generated by Django 4.1.4 on 2023-03-12 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrative_divisions', '0002_responsibility'),
        ('students', '0004_student_active_evaluation_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation_a',
            name='ability_to_expression_of_thoughts',
            field=models.CharField(default='deafult', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation_a',
            name='discussion',
            field=models.CharField(default='default', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation_a',
            name='hold_of_ideology',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation_a',
            name='interest_study',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation_a',
            name='punctuality',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation_a',
            name='questioning',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation_a',
            name='social_behaviour',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation_a',
            name='understanding_stubborn',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Evaluation_C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_study', models.CharField(max_length=100)),
                ('social_behaviour', models.CharField(max_length=100)),
                ('general_behaviour', models.CharField(max_length=100)),
                ('participation_in_preaching', models.CharField(max_length=100)),
                ('project', models.CharField(max_length=100)),
                ('resullt', models.BooleanField(default=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='???????? ??')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation_B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('management_performance', models.CharField(max_length=100)),
                ('project', models.CharField(max_length=100)),
                ('discussion', models.CharField(max_length=500)),
                ('responsibility', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrative_divisions.responsibility')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='???????? ??')),
            ],
        ),
    ]
