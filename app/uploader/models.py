from django.db import models

import uuid
import os
# Create your models here.

def upload_file_path(instance, filename):
    """Generate file path for new recipe image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'document', filename)

class Upload(models.Model):
    upload_file = models.FileField(upload_to=upload_file_path)
    upload_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.upload_file