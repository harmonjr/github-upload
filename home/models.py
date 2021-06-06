from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Homepage Hero image',
        on_delete=models.SET_NULL,
    )
    hero_title1 = models.CharField(
        max_length=120,
        blank=True,
        help_text="Main text displayed in the hero section over the background."
    )

    hero_title2 = models.CharField(
        max_length=120,
        blank=True,
        help_text="Main text displayed in the hero section over the background."
    )

    hero_subtitle = models.CharField(
        max_length=150,
        blank=True,
        help_text="Subtitle text displayed in the hero section over the background."
    )

    cta_btn_text = models.CharField(
        max_length=20,
        blank=True,
        default="Learn More",
        help_text="Call-To-Action Button Text",
    )

    cta_btn_link = models.ForeignKey(
        'wagtailcore.page',
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Internal page link to send the user to when clicking CTA button."
    )
    # CONFIGURE ADMIN INTERFACE
    content_panels = Page.content_panels + [
        ImageChooserPanel("hero_image"),
        FieldPanel("hero_title1"),
        FieldPanel("hero_title2"),
        FieldPanel("hero_subtitle"),
        FieldPanel("cta_btn_text"),
        PageChooserPanel("cta_btn_link"),
    ]
