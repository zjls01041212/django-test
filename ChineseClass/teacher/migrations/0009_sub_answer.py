# Generated by Django 3.0 on 2020-01-07 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200103_1559'),
        ('teacher', '0008_auto_20200107_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(null=True)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Homework')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
