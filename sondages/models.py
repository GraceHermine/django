from django.db import models

class Service(models.Model):  # Utilisation de 'Service' avec une majuscule
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10000, decimal_places=2)
    images = models.ImageField(upload_to='service_images', null=True, blank=True)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    
class avis(models.Model):
    class Meta:
        verbose_name = ("Avis")
        verbose_name_plural = ("Avis")

    service = models.ForeignKey(Service ,on_delete= models.CASCADE)
    name = models.CharField(max_length= 200, unique= True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class rendez_vous(models.Model):
    class Meta:
        verbose_name = ("Rendez-Vous")
        verbose_name_plural = ("Rendez-Vous")

    service = models.ForeignKey(Service, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)
    statut = models

    def __str__(self):
        return self.date
    
class About_models(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length= 200)
    title_about = models.CharField(max_length= 200)
    logo = models.ImageField()
    adresse = models.CharField(max_length= 200)
    email = models.EmailField()
    image = models.ImageField()
    description = models.TextField()


    def __str__(self):
        return self.title_about
    
class contact(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    nom = models.CharField(max_length= 200)
    email = models.EmailField()
    adresse = models.TextField()
    
    def __str__(self):
        return self.nom

# Create your models here.
