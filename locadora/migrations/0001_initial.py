# Generated by Django 3.1.7 on 2021-04-08 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('imagem', models.ImageField(blank=True, upload_to='locadora/media')),
                ('descricao', models.TextField()),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('placa', models.CharField(max_length=20)),
                ('data', models.CharField(max_length=20)),
                ('hora', models.CharField(max_length=20)),
                ('periodo', models.IntegerField()),
                ('cliente', models.ManyToManyField(blank=True, to='locadora.Cliente')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.veiculo', verbose_name='Veiculo')),
            ],
        ),
    ]