from django.db import models

from django.utils.text import slugify
from django.urls import reverse

class Service(models.Model):
    title = models.CharField("Titre", max_length=100)
    short_description = models.CharField("Description courte", max_length=200, blank=True)
    long_description = models.TextField("Description longue", blank=True)
    icon_class = models.CharField("Classe d'icône", max_length=50, blank=True, 
                                 help_text="Ex: fa fa-laptop-code")
    image = models.ImageField("Image", upload_to='services/')
    slug = models.SlugField(unique=True, blank=True)
    is_featured = models.BooleanField("Mettre en avant", default=False,
                                    help_text="Cocher pour afficher ce service en page d'accueil")
    display_order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['display_order', 'title']
        ordering = ['-is_featured', 'display_order']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

class TeamMember(models.Model):
    POSITION_CHOICES = [
        ('management', 'Management'),
        ('technical', 'Technique'),
        ('design', 'Design'),
        ('training', 'Formation'),
    ]
    
    name = models.CharField("Nom complet", max_length=100)
    position = models.CharField("Poste", max_length=100)
    position_type = models.CharField("Type de poste", max_length=20, 
                                    choices=POSITION_CHOICES, default='technical')
    bio = models.TextField("Biographie", blank=True)
    image = models.ImageField("Photo", upload_to='team/')
    facebook = models.URLField("Facebook", blank=True)
    twitter = models.URLField("Twitter", blank=True)
    linkedin = models.URLField("LinkedIn", blank=True)
    instagram = models.URLField("Instagram", blank=True)
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Téléphone", max_length=20, blank=True)
    display_order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    is_active = models.BooleanField("Actif", default=True)
    
    class Meta:
        verbose_name = "Membre d'équipe"
        verbose_name_plural = "Membres d'équipe"
        ordering = ['display_order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"

class Project(models.Model):
    PROJECT_CATEGORIES = [
        ('web', 'Développement Web'),
        ('mobile', 'Application Mobile'),
        ('system', 'Système de Gestion'),
        ('training', 'Formation'),
        ('consulting', 'Consulting'),
    ]
    
    title = models.CharField("Titre", max_length=100)
    short_description = models.CharField("Description courte", max_length=200)
    long_description = models.TextField("Description détaillée")
    image = models.ImageField("Image principale", upload_to='projects/')
    category = models.CharField("Catégorie", max_length=20, choices=PROJECT_CATEGORIES)
    client_name = models.CharField("Client", max_length=100, blank=True)
    project_date = models.DateField("Date du projet", blank=True, null=True)
    project_url = models.URLField("URL du projet", blank=True)
    is_featured = models.BooleanField("En vedette", default=False)
    display_order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-is_featured', 'display_order']
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.pk)])

class Testimonial(models.Model):
    client_name = models.CharField("Nom du client", max_length=100)
    company = models.CharField("Entreprise", max_length=100, blank=True)
    profession = models.CharField("Profession", max_length=100)
    content = models.TextField("Témoignage")
    image = models.ImageField("Photo", upload_to='testimonials/', blank=True)
    rating = models.PositiveSmallIntegerField("Note (1-5)", default=5)
    is_featured = models.BooleanField("En vedette", default=False)
    display_order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    created_at = models.DateTimeField("Date de création", auto_now_add=True)
    
    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['-is_featured', 'display_order']
    
    def __str__(self):
        return f"{self.client_name} - {self.profession}"

class Fact(models.Model):
    ICON_CHOICES = [
        ('certificate', 'Certificat'),
        ('users-cog', 'Utilisateurs'),
        ('users', 'Clients'),
        ('check', 'Validation'),
        ('project', 'Projet'),
    ]
    
    title = models.CharField("Titre", max_length=100)
    value = models.IntegerField("Valeur")
    icon = models.CharField("Icône", max_length=20, choices=ICON_CHOICES, default='certificate')
    suffix = models.CharField("Suffixe", max_length=5, blank=True, default='+',
                             help_text="Ex: +, %, etc.")
    display_order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    
    class Meta:
        verbose_name = "Fait marquant"
        verbose_name_plural = "Faits marquants"
        ordering = ['display_order']
    
    def __str__(self):
        return self.title
    
    def get_icon_class(self):
        return f"fa fa-{self.icon}"
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email