# Generated by Django 3.0.5 on 2020-06-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200610_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='pages',
            field=models.ManyToManyField(blank=True, null=True, to='main.pages'),
        ),
    ]
