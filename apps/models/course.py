from django.core.validators import FileExtensionValidator
from django.db.models import Model, CharField, FileField, IntegerField, ManyToManyField, ForeignKey, CASCADE, SlugField, \
    TextField
from django.utils.text import slugify

from apps.models.user import User


class Category(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
            while Category.objects.filter(slug=self.slug).exists():
                slugs = self.slug.split('-')
                if slugs and slugs[-1].isdigit():
                    count = int(slugs.pop()) + 1
                    self.slug = '-'.join(slugs) + f"-{count}"
                else:
                    self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Course(Model):
    title = CharField(max_length=255, blank=True)
    video = FileField(upload_to='course/', validators=[FileExtensionValidator(['mp4', 'webm'])])
    description = TextField(blank=True, null=True)
    category = ForeignKey('apps.Category', CASCADE)
    price = IntegerField()
    students = ManyToManyField('apps.User', limit_choices_to={"type": User.Type.STUDENT}, related_name='courses',
                               blank=True)

    def __str__(self):
        return self.title
