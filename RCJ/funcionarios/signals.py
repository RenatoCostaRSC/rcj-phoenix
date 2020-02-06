# signals.py
# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify
 
def create_slug(sender, instance, signal, *args, **kwargs):
    # check for id and attributes
    if instance.id and hasattr(instance, 'slug') and hasattr(instance, 'name'):
        # get slug information
        slug_name = instance.slug
        slug_from = instance.name
        # save slug if empty
        if not getattr(instance, slug_name, None):
            # create slug
            slug = '%s-' % instance.id + slugify(getattr(instance, slug_from))
            # set slug
            setattr(instance, slug_name, slug)
            # save instance
            instance.save()