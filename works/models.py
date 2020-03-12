from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

class WorksIndexPage(Page):
    template = 'works/works_page.html'

    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['works'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class WorksPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'WorkPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class WorkPage(Page):
    catergories = [
        ('dt', 'Downloadable Templates'),
        ('il', 'Illustrations'),
        ('cp', 'Client Projects'),
    ]
    description = models.TextField(null=True, blank=True)
    category = models.CharField(
        max_length=2,
        choices=catergories,
        default='DOWNLOADABLE',
    )
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=WorksPageTag, blank=True)


    def thumbnail_img(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        FieldPanel('category'),
        FieldPanel('tags'),
        FieldPanel('date'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class WorkPageGalleryImage(Orderable):
    page = ParentalKey(WorkPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
