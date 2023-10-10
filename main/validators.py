import re
from rest_framework.serializers import ValidationError


class LinkValidator:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        for field in self.fields:
            text = value.get(field, '')
            if self.has_external_links(text):
                raise ValidationError('Недопустимая ссылка на сторонний ресурс!')

    def has_external_links(self, text):

        urls = re.findall(r'(?:https?://|www\.)?([^\s./?#]+)(?:\.[^\s./?#]+)', text)
        for url in urls:
            if 'youtube' not in url:
                return True
        return False
