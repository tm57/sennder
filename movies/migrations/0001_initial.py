# Generated by Django 3.0.8 on 2020-07-24 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=1000)),
                ('id', models.CharField(max_length=1000, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.Movie')),
            ],
        ),
        migrations.AddConstraint(
            model_name='character',
            constraint=models.UniqueConstraint(fields=('movie_id', 'uuid'), name='u_movie_id_uuid'),
        ),
    ]
