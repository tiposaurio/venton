# _*_ coding: utf-8 _*_
"""
@copyright   Copyright (c) 2014 Submit Consulting
@author      Angel Sullon (@asullom)
@package     auth
@Descripcion Definición de los modelos
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

# models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
# others


class User(AbstractUser):

    """
    Tabla para usuarios
    """

    class Meta:
        # swappable = 'AUTH_USER_MODEL' #ver django-angular-seed
        verbose_name = capfirst(_('user'))
        verbose_name_plural = capfirst(_('users'))
        permissions = (
            ('user', 'Can ALL user'),
        )
        db_table = 'auth_user'

    # comentar desde aqui
