# Generated by Django 4.2.7 on 2023-12-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDisfraces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(max_length=30)),
                ('talle', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='disfraces',
            old_name='disfraces',
            new_name='nombre',
        ),
    ]