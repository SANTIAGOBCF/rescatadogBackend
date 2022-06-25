# Generated by Django 4.0.4 on 2022-06-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adopter_id', models.IntegerField()),
                ('pet_id', models.IntegerField()),
                ('rescuer_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField()),
                ('deleted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AdoptionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adoption_id', models.IntegerField()),
                ('rescuer_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField()),
                ('deleted', models.BooleanField()),
            ],
        ),
    ]
