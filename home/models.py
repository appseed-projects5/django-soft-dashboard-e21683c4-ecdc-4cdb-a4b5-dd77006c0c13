# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    login = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    lieu-travail = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cyberattaque(models.Model):

    #__Cyberattaque_FIELDS__
    nom-att = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    impact = models.CharField(max_length=255, null=True, blank=True)
    statut = models.CharField(max_length=255, null=True, blank=True)
    zone_attaquee = models.CharField(max_length=255, null=True, blank=True)
    type_attaque = models.CharField(max_length=255, null=True, blank=True)
    secteur_attaque = models.CharField(max_length=255, null=True, blank=True)
    lieu = models.CharField(max_length=255, null=True, blank=True)
    origine = models.CharField(max_length=255, null=True, blank=True)

    #__Cyberattaque_FIELDS__END

    class Meta:
        verbose_name        = _("Cyberattaque")
        verbose_name_plural = _("Cyberattaque")



#__MODELS__END
