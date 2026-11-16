from django.db import models
import os
# Create your models here.

# Project Module
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    proposal_file = models.FileField(upload_to='proposals/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return os.path.basename(self.proposal_file.name)
