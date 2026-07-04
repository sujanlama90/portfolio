from django.db import models
import logging

# module logger
logger = logging.getLogger(__name__)

# Create your models here.
# models for contact
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        logger.debug('Saving Contact: %s <%s>', self.name, self.email)
        super().save(*args, **kwargs)
    
#models for project

class Project(models.Model):
    image = models.ImageField(upload_to='project_Image/')
    title = models.CharField(max_length=30)
    description = models.TextField()
    technologies = models.CharField(
        max_length=255,
        help_text="Separate technologies with commas"
    )
    live_demo= models.URLField(blank=True,null=True)
    github_link = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Journey(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    paragraph3 = models.TextField()
    
    def __str__(self):
        return self.title

class Education(models.Model):
    year = models.CharField(max_length=50)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.degree} ({self.year})"

class SkillCategory(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=20,
        blank=True,
        help_text="Example: 🚀, 🎨, 🗄️"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.title


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name="skills",
        null=True,
        blank=True

    )
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
    
class MyContact(models.Model):
    email = models.EmailField()
    phone = models.CharField()
    location = models.CharField(max_length=100)
    availability = models.CharField()
    
    def __str__(self):
        return self.email
    
