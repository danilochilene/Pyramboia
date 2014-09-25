from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from .models import Task, Project, Argument, Target, Header


class ProjectForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
                super(ProjectForm, self).__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.form_method = 'POST'
                self.helper.form_class = 'form-horizontal'
                self.helper.label_class = 'col-lg-2'
                self.helper.field_class = 'col-lg-8'
                self.helper.layout = Layout(
                    Field('project_name', css_class="input-sm"),
                    Field('description', css_class="input-lg"),
                    FormActions(
                        Submit('submit', "Submit", css_class='btn'),
                        Submit('cancel', "Cancel", css_class='btn'),
                    )
                )
                #self.helper.layout.append(Submit('save', 'save'))

        class Meta:
                model = Project


class TaskForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
                super(TaskForm, self).__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.form_method = 'POST'
                self.helper.form_class = 'form-horizontal'
                self.helper.label_class = 'col-lg-2'
                self.helper.field_class = 'col-lg-8'
                self.helper.layout = Layout(
                    Field('project_name', css_class="input-sm"),
                    Field('task_name', css_class="input-sm"),
                    Field('target', css_class="input-sm",
                          HTML='<a href="/addtarget"/>a</a>'),
                    Field('request', css_class="input-lg"),
                    Field('requires', css_class="input-sm"),
                    Field('threshold', css_class="input-sm"),
                    Field('header', css_class="input-sm"),
                    Field('arguments', css_class="input-sm"),
                    Field('test', css_class="input-sm"),
                    Field('steps', css_class="input-sm"),
                    FormActions(
                        Submit('submit', "Submit", css_class='btn'),
                        Submit('cancel', "Cancel", css_class='btn'),
                    )
                )

        class Meta:
                model = Task


class ArgumentForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
                super(ArgumentForm, self).__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.form_method = 'POST'
                self.helper.form_class = 'form-horizontal'
                self.helper.label_class = 'col-lg-2'
                self.helper.field_class = 'col-lg-8'
                self.helper.layout = Layout(
                    Field('name', css_class="input-sm"),
                    Field('argument', css_class="input-sm"),
                    Field('value', css_class="input-sm"),
                    FormActions(
                        Submit('submit', "Submit", css_class='btn'),
                        Submit('cancel', "Cancel", css_class='btn'),
                    )
                )
                #self.helper.layout.append(Submit('save', 'save'))

        class Meta:
                model = Argument


class HeaderForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
                super(HeaderForm, self).__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.form_method = 'POST'
                self.helper.form_class = 'form-horizontal'
                self.helper.label_class = 'col-lg-2'
                self.helper.field_class = 'col-lg-8'
                self.helper.layout = Layout(
                    Field('name', css_class="input-sm"),
                    Field('contenttype', css_class="input-sm"),
                    Field('charset', css_class="input-sm"),
                    Field('soapaction', css_class="input-sm"),
                    FormActions(
                        Submit('submit', "Submit", css_class='btn'),
                        Submit('cancel', "Cancel", css_class='btn'),
                    )
                )
                #self.helper.layout.append(Submit('save', 'save'))

        class Meta:
                model = Header


class TargetForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
                super(TargetForm, self).__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.form_method = 'POST'
                self.helper.form_class = 'form-horizontal'
                self.helper.label_class = 'col-lg-2'
                self.helper.field_class = 'col-lg-8'
                self.helper.layout = Layout(
                    Field('name', css_class="input-sm"),
                    Field('url', css_class="input-sm"),
                    FormActions(
                        Submit('submit', "Submit", css_class='btn'),
                        Submit('cancel', "Cancel", css_class='btn'),
                    )
                )
                #self.helper.layout.append(Submit('save', 'save'))

        class Meta:
                model = Target
