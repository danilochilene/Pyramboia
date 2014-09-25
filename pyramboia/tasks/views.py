import time
import requests
import xml.dom.minidom
from lxml import etree
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import RequestContext, loader
from .models import Project, Target, Header, Argument, Task, History
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import TaskForm, ProjectForm, ArgumentForm, HeaderForm, TargetForm
from django.views.generic.edit import FormView
from django.db.models import Count
from jsonrpc import jsonrpc_method
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def home(request):
    return render_to_response('base.html', locals(), context_instance=RequestContext(request))


@jsonrpc_method('tasks.queueTask')
def queueTask(id=None, arguments={}):
    '''Roda a task'''
    if id:
        argument = None
        tasks = Task.objects.get(id=id)
        if tasks.requires:
            result, time_total, text, headers_full, required_tasks, arguments = queueTask(
                tasks.requires.id, arguments)
        start = time.time()
        headers = Header.objects.get(task=tasks.id)
        target = Target.objects.get(task=tasks.id)
        headers_full = {'Content-Type': '0', 'SOAPAction': '0'}
        headers_full['Content-Type'] = '%s;%s' % (
            headers.contenttype, headers.charset,)
        headers_full['SOAPAction'] = tasks.header.soapaction
        data = tasks.request % arguments
        response = requests.post(
            str(target.url), data=data, headers=headers_full).content
        #tree = etree.XML(response.decode('utf-8', 'ignore'))
        tree = etree.XML(response)
        result = (etree.tostring(tree, pretty_print=True, encoding='utf-8'))
        end = time.time()
        time_total = end - start
        if time_total > tasks.threshold:
            text = 'Alert'
        else:
            text = 'OK'
        args = arguments
        for argument in Argument.objects.filter(argument=tasks.arguments.argument):
            valor = ''
            try:
                tree = etree.XML(response)
                valor = tree.xpath("//*[local-name() = '{0}']".format(tasks.arguments.argument))[0].text
            except:
                valor = ''
            args.setdefault(argument.value, valor)
        return result, time_total, text, headers_full, tasks, args


@jsonrpc_method('tasks.run')
def runTask(request, id):
    '''Apresenta a task'''
    result, time_total, text, headers_full, tasks, args = queueTask(id, {})
    return render_to_response('task_result.html', locals(), context_instance=RequestContext(request))


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Project {} Successfully Deleted'.format(self.get_object()))
        return super(ProjectDeleteView, self).delete(self, request, *args, **kwargs)


class ProjectListView(ListView):
    model = Project
    template_name_suffix = '_list'


class ProjectCreateView(CreateView):
    template_name_suffix = '_create'
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        messages.success(
            self.request, 'Project {} Successfully Created'.format(self.object))
        return super(ProjectCreateView, self).form_valid(form)


class ProjectDetailView(DetailView):
    model = Project


class ProjectUpdateView(UpdateView):
    template_name_suffix = '_create'
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        messages.success(self.request, u'Project updated.')
        return super(ProjectUpdateView, self).form_valid(form)


def all_projects(request):
    projects = Project.objects.all()
    return render_to_response('all_projects.html', locals(), context_instance=RequestContext(request))


def addTask(request):
    form = TasksForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        message = 'Add a new task'
        messages.success(request, 'Your task has been added.')
        return HttpResponseRedirect('/')
    return render_to_response('addtask.html', locals(), context_instance=RequestContext(request))


def addArguments(request):
    form = ArgumentsForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        message = 'Add a new argument'
        messages.success(request, 'Your argument has been added.')
        return HttpResponseRedirect('/')
    return render_to_response('addargs.html', locals(), context_instance=RequestContext(request))


class HeaderDeleteView(DeleteView):
    model = Header
    success_url = reverse_lazy('header-list')

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Header {} Successfully Deleted'.format(self.get_object()))
        return super(HeaderDeleteView, self).delete(self, request, *args, **kwargs)


class HeaderListView(ListView):
    model = Header
    template_name_suffix = '_list'


class HeaderCreateView(CreateView):
    template_name_suffix = '_create'
    model = Header
    form_class = HeaderForm

    def form_valid(self, form):
        messages.success(
            self.request, 'Project {} Successfully Created'.format(self.object))
        return super(HeaderCreateView, self).form_valid(form)


class HeaderDetailView(DetailView):
    model = Header


class HeaderUpdateView(UpdateView):
    template_name_suffix = '_create'
    model = Header
    form_class = HeaderForm

    def form_valid(self, form):
        messages.success(self.request, u'Project updated.')
        return super(HeaderUpdateView, self).form_valid(form)


# Target Views
class TargetDeleteView(DeleteView):
    model = Target
    success_url = reverse_lazy('target-list')

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Target {} Successfully Deleted'.format(self.get_object()))
        return super(TargetDeleteView, self).delete(self, request, *args, **kwargs)


class TargetListView(ListView):
    model = Target
    template_name_suffix = '_list'


class TargetCreateView(CreateView):
    template_name_suffix = '_create'
    model = Target
    form_class = TargetForm

    def form_valid(self, form):
        messages.success(
            self.request, 'Target {} Successfully Created'.format(self.object))
        return super(TargetCreateView, self).form_valid(form)


class TargetDetailView(DetailView):
    model = Target


class TargetUpdateView(UpdateView):
    template_name_suffix = '_create'
    model = Target
    form_class = TargetForm

    def form_valid(self, form):
        messages.success(self.request, u'Project updated.')
        return super(TargetUpdateView, self).form_valid(form)

# Argument Views


class ArgumentDeleteView(DeleteView):
    model = Argument
    success_url = reverse_lazy('argument-list')

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Argument {} Successfully Deleted'.format(self.get_object()))
        return super(ArgumentDeleteView, self).delete(self, request, *args, **kwargs)


class ArgumentListView(ListView):
    model = Argument
    template_name_suffix = '_list'


class ArgumentCreateView(CreateView):
    template_name_suffix = '_create'
    model = Argument
    form_class = ArgumentForm

    def form_valid(self, form):
        messages.success(
            self.request, 'Argument {} Successfully Created'.format(self.object))
        return super(ArgumentCreateView, self).form_valid(form)


class ArgumentDetailView(DetailView):
    model = Argument


class ArgumentUpdateView(UpdateView):
    template_name_suffix = '_create'
    model = Argument
    form_class = ArgumentForm

    def form_valid(self, form):
        messages.success(self.request, u'Argument updated.')
        return super(ArgumentUpdateView, self).form_valid(form)


# Task Views


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Task {} Successfully Deleted'.format(self.get_object()))
        return super(TaskDeleteView, self).delete(self, request, *args, **kwargs)


class TaskListView(ListView):
    model = Task
    template_name_suffix = '_list'


class TaskCreateView(CreateView):
    template_name_suffix = '_create'
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        messages.success(
            self.request, 'Task {} Successfully Created'.format(self.object))
        return super(TaskCreateView, self).form_valid(form)


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    template_name_suffix = '_create'
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        messages.success(self.request, u'Argument updated.')
        return super(TaskUpdateView, self).form_valid(form)
