# Generated by Django 5.1.4 on 2025-06-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('value', models.IntegerField(verbose_name='Valeur')),
                ('icon', models.CharField(choices=[('certificate', 'Certificat'), ('users-cog', 'Utilisateurs'), ('users', 'Clients'), ('check', 'Validation'), ('project', 'Projet')], default='certificate', max_length=20, verbose_name='Icône')),
                ('suffix', models.CharField(blank=True, default='+', help_text='Ex: +, %, etc.', max_length=5, verbose_name='Suffixe')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")),
            ],
            options={
                'verbose_name': 'Fait marquant',
                'verbose_name_plural': 'Faits marquants',
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('short_description', models.CharField(max_length=200, verbose_name='Description courte')),
                ('long_description', models.TextField(verbose_name='Description détaillée')),
                ('image', models.ImageField(upload_to='projects/', verbose_name='Image principale')),
                ('category', models.CharField(choices=[('web', 'Développement Web'), ('mobile', 'Application Mobile'), ('system', 'Système de Gestion'), ('training', 'Formation'), ('consulting', 'Consulting')], max_length=20, verbose_name='Catégorie')),
                ('client_name', models.CharField(blank=True, max_length=100, verbose_name='Client')),
                ('project_date', models.DateField(blank=True, null=True, verbose_name='Date du projet')),
                ('project_url', models.URLField(blank=True, verbose_name='URL du projet')),
                ('is_featured', models.BooleanField(default=False, verbose_name='En vedette')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")),
            ],
            options={
                'verbose_name': 'Projet',
                'verbose_name_plural': 'Projets',
                'ordering': ['-is_featured', 'display_order'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('short_description', models.CharField(blank=True, max_length=200, verbose_name='Description courte')),
                ('long_description', models.TextField(blank=True, verbose_name='Description longue')),
                ('icon_class', models.CharField(blank=True, help_text='Ex: fa fa-laptop-code', max_length=50, verbose_name="Classe d'icône")),
                ('image', models.ImageField(upload_to='services/', verbose_name='Image')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('is_featured', models.BooleanField(default=False, verbose_name='En vedette')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['display_order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom complet')),
                ('position', models.CharField(max_length=100, verbose_name='Poste')),
                ('position_type', models.CharField(choices=[('management', 'Management'), ('technical', 'Technique'), ('design', 'Design'), ('training', 'Formation')], default='technical', max_length=20, verbose_name='Type de poste')),
                ('bio', models.TextField(blank=True, verbose_name='Biographie')),
                ('image', models.ImageField(upload_to='team/', verbose_name='Photo')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, verbose_name='Twitter')),
                ('linkedin', models.URLField(blank=True, verbose_name='LinkedIn')),
                ('instagram', models.URLField(blank=True, verbose_name='Instagram')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Téléphone')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
            ],
            options={
                'verbose_name': "Membre d'équipe",
                'verbose_name_plural': "Membres d'équipe",
                'ordering': ['display_order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name='Nom du client')),
                ('company', models.CharField(blank=True, max_length=100, verbose_name='Entreprise')),
                ('profession', models.CharField(max_length=100, verbose_name='Profession')),
                ('content', models.TextField(verbose_name='Témoignage')),
                ('image', models.ImageField(blank=True, upload_to='testimonials/', verbose_name='Photo')),
                ('rating', models.PositiveSmallIntegerField(default=5, verbose_name='Note (1-5)')),
                ('is_featured', models.BooleanField(default=False, verbose_name='En vedette')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
            ],
            options={
                'verbose_name': 'Témoignage',
                'verbose_name_plural': 'Témoignages',
                'ordering': ['-is_featured', 'display_order'],
            },
        ),
    ]
