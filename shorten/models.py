from django.conf import settings
from django.db import models
from .utils import *


class Link(models.Model):
    id = models.AutoField(primary_key=True)
    og = models.TextField()
    last_accessed = models.DateTimeField()

    def isExists(self, og_link):
        try:
            check_url = Link.objects.get(og=og_link)
            self.id = check_url.id
            return False
        except Link.DoesNotExist:
            return True

    def transform(self, url):
        global idx_id
        result = self.isExists(url)
        if result:
            if idx_id < DATA_MAX:
                self.id = idx_id
                idx_id += 1
                self.og = url
                self.last_accessed = timezone.now()
                self.save()
            else:
                check_set = Link.objects.order_by('last_accessed')
                check_url = Link.objects.get(id=check_set[0].id)
                if not isLinkValid(check_url.last_accessed):
                    check_url.og = url
                    check_url.last_accessed = timezone.now()
                    check_url.save()
                    return toBase62(check_url.id)
                else:
                    return None

        return toBase62(self.id)

    def __str__(self):
        return str(self.og)


idx_id = Link.objects.count()
