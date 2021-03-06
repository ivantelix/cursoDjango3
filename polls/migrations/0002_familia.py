# Generated by Django 3.0.4 on 2020-04-19 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('parentesco', models.CharField(blank=True, max_length=50, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Persona')),
            ],
        ),
    ]
