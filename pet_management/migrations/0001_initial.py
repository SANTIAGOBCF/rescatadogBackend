# Generated by Django 4.0.4 on 2022-06-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=180)),
                ('description', models.TextField()),
                ('url', models.URLField(null=True)),
                ('is_adopted', models.BooleanField(default=False)),
            ],
        ),
    ]