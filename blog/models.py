from django.db import models
# added to create blog page
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField

# Create the Blog listing class
class BlogListingPage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        help_text='Header background image',
        on_delete=models.SET_NULL,
    )

    headline_text1 = models.CharField(
        max_length=70,
        blank=True,
        help_text='Blog listing page header text first line.'
    )

    headline_text2 = models.CharField(
        max_length=70,
        blank=True,
        help_text='Blog listing page header text second line.'
    )

    headline_subtitle = models.CharField(
        max_length=150,
        blank=True,
        help_text='Blog listing page header subtitle.'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("background_image"),
        FieldPanel("headline_text1"),
        FieldPanel("headline_text2"),
        FieldPanel("headline_subtitle"),

    ]

class BlogPage(Page):
    date = models.DateField("Article Date")
    intro = models.TextField("Introduction")
    body = RichTextField(
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
