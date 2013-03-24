from django.db import models


class PostType(models.Model):
    post_type = models.CharField(max_length=30)

    def __unicode__(self):
        return self.post_type


class Blog(models.Model):
    post_type = models.ForeignKey(PostType)
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    # post_illustration = models.ImageField(upload_to='')

    def __unicode__(self):
        return "[%s]" % (self.post_title)
