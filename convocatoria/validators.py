from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat

def file_size(value):
    limit = 10 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('No aceptamos archivos de más de 10MB, tu archivo pesa %s bytes' % filesizeformat(value.size))