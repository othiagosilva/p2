# Generated by Django 4.1.3 on 2022-11-30 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, null=True)),
                ('idade', models.CharField(max_length=20, null=True)),
                ('peso', models.CharField(max_length=20, null=True)),
                ('altura', models.CharField(max_length=20, null=True)),
                ('masculino', models.BooleanField(default=True, null=True)),
                ('subescapular', models.CharField(max_length=20, null=True)),
                ('tricipital', models.CharField(max_length=20, null=True)),
                ('peitoral', models.CharField(max_length=20, null=True)),
                ('axilar_medio', models.CharField(max_length=20, null=True)),
                ('suprailiaca', models.CharField(max_length=20, null=True)),
                ('coxa', models.CharField(max_length=20, null=True)),
                ('abdomen_dobra', models.CharField(max_length=20, null=True)),
                ('torax', models.CharField(max_length=20, null=True)),
                ('braco_relaxado', models.CharField(max_length=20, null=True)),
                ('braco_contraido', models.CharField(max_length=20, null=True)),
                ('antebraco', models.CharField(max_length=20, null=True)),
                ('abdomen_perimetria', models.CharField(max_length=20, null=True)),
                ('cintura', models.CharField(max_length=20, null=True)),
                ('quadril', models.CharField(max_length=20, null=True)),
                ('coxas', models.CharField(max_length=20, null=True)),
                ('panturrilha', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Renda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_renda', models.CharField(max_length=20, null=True)),
                ('valor_renda', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('usuario', models.CharField(max_length=20, null=True)),
                ('senha', models.CharField(max_length=200, null=True)),
                ('treinador', models.BooleanField(null=True)),
            ],
        ),
    ]
