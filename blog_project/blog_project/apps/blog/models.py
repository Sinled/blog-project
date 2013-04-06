from django.db import models


class PostType(models.Model):
    post_type = models.CharField(max_length=30)

    def __unicode__(self):
        return self.post_type


class Blog(models.Model):
    post_type = models.ForeignKey(PostType, blank=True, null=True)
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_illustration = models.ImageField(upload_to='img', blank=True, null=True)

    def __unicode__(self):
        return "[{0}]".format(self.post_title)
