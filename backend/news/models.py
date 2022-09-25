import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from parler.models import TranslatableModel, TranslatedFields
from account.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(_('Category Name'), max_length=64)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def number_of_news(self):
        return self.category_news.all().count()

    @property
    def get_category_news(self):
        return self.category_news.all()

    class Meta:
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


# ! TAG
class Tag(models.Model):
    name = models.CharField(_('Tag Name'), max_length=32)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def number_of_news(self):
        return self.tag_news.all().count()

    @property
    def get_tag_news(self):
        return self.tag_news.all()

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


# ! NEWS
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)

def upload_news_image(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    return '{}/{}.{}'.format('news', instance.id, extension)

class NewsItem(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name=_('User')
    )
    slug = models.CharField(_('Slug'), max_length=255, unique=True)
    image = models.ImageField(
        upload_to=upload_news_image,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_news',
        verbose_name=_('Category')
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='tag_news',
        verbose_name=_('Tags')
    )
    translations = TranslatedFields(
        title = models.CharField(_('News Title'), max_length=255),
        summary_text = models.TextField(_('Summary Text'), null=True, blank=True),
        content = models.TextField(_("Content"), null=True, blank=True)
    )
    status = models.IntegerField(choices=STATUS, default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # DE
    @property
    def title_de(self):
        self.set_current_language('de')
        return self.title

    @property
    def summary_text_de(self):
        self.set_current_language('de')
        return self.summary_text

    # FR
    @property
    def title_fr(self):
        self.set_current_language('fr')
        return self.title

    @property
    def summary_text_fr(self):
        self.set_current_language('fr')
        return self.summary_text

    # EN
    @property
    def title_en(self):
        self.set_current_language('en')
        return self.title

    @property
    def summary_text_en(self):
        self.set_current_language('en')
        return self.summary_text

    class Meta:
        verbose_name = _('News Item')
        verbose_name_plural = _('News')
    


    
