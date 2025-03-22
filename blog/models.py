from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
      name = models.CharField(max_length=120)
      def __str__(self):
            return self.name

class BlogPost(models.Model):
      title = models.CharField(max_length=100) # Titre de l'article
      author= models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
      category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True)
     # slug = models.SlugField() # Slug pour l'URL
      published = models.BooleanField(default=False) # Statut depublication
      date = models.DateField( auto_now_add=True, blank=True, null=True) # Date de publication
      content = models.TextField() # Contenu de l'article
     # description = models.TextField(blank=True, null=True)
      #price = models.FloatField(blank=True, null=True)
      image = models.ImageField( upload_to="" )

def __str__(self):
 return self.title