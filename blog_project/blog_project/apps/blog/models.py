from django.db import models


class Blog(models.Model):
    post_title = models.CharField(max_length=200)
    # post_text = models.TextField()

    def __unicode__(self):
        return "[%s]" % (self.post_title)
