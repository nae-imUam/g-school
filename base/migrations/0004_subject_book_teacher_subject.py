# Generated by Django 4.0.3 on 2022-04-14 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_student_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bkno', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=70)),
                ('edition', models.CharField(max_length=10)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.subject')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.subject'),
        ),
    ]