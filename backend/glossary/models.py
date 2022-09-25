from django.db import models
from django.core.validators import FileExtensionValidator
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _

# Create your models here.
class GlossaryCategory(models.Model):
    name = models.CharField(_('Category Name'), max_length=32)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _ ('Categories')
    
def upload_term_image(instance, filename):
    filebase, extension = filename.rpslit('.', 1)
    return '{}/{}.{}'.format('glossary', instance.slug, extension)

class GlossaryTerm(TranslatableModel):
    short_name = models.CharField(_('Short Name'), max_length=16, null=True, blank=True)
    long_name = models.CharField(_('Long Name'), max_length=32)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(GlossaryCategory, on_delete=models.CASCADE, verbose_name=_('Category'), related_name="terms")
    image = models.ImageField(
        upload_to=upload_term_image,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        null=True,
        blank=True
    )
    image_url = models.URLField(null=True, blank=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)

    detail_url = models.URLField(null=True, blank=True)
    source_site = models.URLField(_('Source Website'), null=True, blank=True)

    translations = TranslatedFields(
        description=models.TextField(_("Description"), null=True, blank=True)
    )

    def __str__(self):
        return self.long_name

    class Meta:
        verbose_name = _('Term')
        verbose_name_plural = _('Terms')
    
