# Generated by Django 3.0 on 2020-01-03 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_class'),
        ('teacher', '0003_classes_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('close_time', models.DateTimeField()),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Classes')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=10)),
                ('difficulty', models.IntegerField()),
                ('location', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question_bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('question', models.ManyToManyField(to='teacher.Question')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Homework_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Homework')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.AddField(
            model_name='homework',
            name='question',
            field=models.ManyToManyField(to='teacher.Question'),
        ),
        migrations.AddField(
            model_name='homework',
            name='student',
            field=models.ManyToManyField(through='teacher.Homework_score', to='student.Student'),
        ),
    ]
