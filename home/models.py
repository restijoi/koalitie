from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    description = models.TextField(null=True, blank=True)
    date = models.DateField("Post date")

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        FieldPanel('date'),
    ]
