from django.db import models

# Create your models here.


class Project(models.Model):

    '''Simple model for a project'''
    project_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    added_on = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return unicode(self.project_name)

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', [self.pk])


class Target(models.Model):

    '''Target model, a task can on N urls'''
    name = models.ForeignKey(Project)
    url = models.URLField(max_length=500)
    status = (
        ('A', 'Active'),
        ('O', 'Offline'),
        ('D', 'Default'),
    )

    def __unicode__(self):
        return unicode(self.url)

    @models.permalink
    def get_absolute_url(self):
        return ('target-detail', [self.pk])


class Header(models.Model):

    '''HTML Headers model, each task can have different headers. Example:
    SOAPAction'''
    name = models.ForeignKey(Project)
    contenttype = models.CharField(max_length=50)
    charset = models.CharField(max_length=50)
    soapaction = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.soapaction)

    @models.permalink
    def get_absolute_url(self):
        return ('header-detail', [self.pk])


class Argument(models.Model):

    '''Arguments model, what you are going use from a XML result or pass'''
    name = models.ForeignKey(Project)
    argument = models.CharField(max_length=100)
    value = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('argument-detail', [self.pk])


class Task(models.Model):

    '''Task model, the operation itself. A task can have N steps'''
    project_name = models.ForeignKey(Project)
    task_name = models.CharField(max_length=100)
    target = models.ForeignKey(Target)
    request = models.TextField(max_length=1000, verbose_name='XML request')
    requires = models.ForeignKey('Task', blank=True, null=True)
    threshold = models.FloatField()
    header = models.ForeignKey(Header)
    test = models.CharField(max_length=100, blank=True, null=True)
    arguments = models.ForeignKey(Argument, blank=True, null=True)
    steps = models.IntegerField()
    added_on = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return unicode(self.task_name)

    @models.permalink
    def get_absolute_url(self):
        return ('task-detail', [self.pk])


class History(models.Model):

        '''History model, save all results from tasks, including the XML response'''
        project_name = models.ForeignKey(Project)
        task_name = models.ForeignKey(Task)
        response = models.TextField()
        time = models.FloatField()
        status = models.BooleanField(default=False)
        added_on = models.DateTimeField(auto_now=True, auto_now_add=True)

        def __unicode__(self):
                return unicode(self.task_name)
