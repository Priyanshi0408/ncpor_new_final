# Generated by Django 4.0.6 on 2022-07-28 07:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nsidc_app', '0017_auto_20220723_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='archiveclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.CharField(max_length=2)),
                ('tenderno', models.CharField(max_length=200)),
                ('download', models.URLField(blank=True)),
                ('downloadname', models.CharField(blank=True, max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('releasedate', models.DateTimeField(default=django.utils.timezone.now)),
                ('closingdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='myclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.CharField(max_length=2)),
                ('tenderno', models.CharField(max_length=200)),
                ('download', models.URLField(blank=True)),
                ('downloadname', models.CharField(blank=True, max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('releasedate', models.DateTimeField(default=django.utils.timezone.now)),
                ('closingdate', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='informationresearch',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='research',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='research_example_down_resgran',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='research_example_down_scientists',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='research_example_down_sp',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='researchgrant',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='researchscientist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='scientificexpedition',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='scientificpublication',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
