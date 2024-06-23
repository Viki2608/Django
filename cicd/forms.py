from django import forms

class PipelineForm(forms.Form):
    organization = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Organization', 'id': 'organization'})
    )
    repository = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Repository', 'id': 'repository'})
    )
    BRANCH_CHOICES = [
        ('dev', 'DEV'),
        ('uat', 'UAT'),
        ('preprod', 'PreProd'),
        ('prod', 'Prod'),
    ]
    branch = forms.ChoiceField(
        label='Branch', 
        choices=BRANCH_CHOICES, 
        widget=forms.Select(attrs={'placeholder': 'Select Branch', 'id': 'branch'})
    )

class GroupDeploy(forms.Form):
    organization = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Organization', 'id': 'organization'})
    )
    repository = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Repository', 'id': 'repository'})
    )
    BRANCH_CHOICES = [
        ('dev', 'DEV'),
        ('uat', 'UAT'),
        ('preprod', 'PreProd'),
        ('prod', 'Prod'),
    ]
    branch = forms.ChoiceField(
        label='Branch', 
        choices=BRANCH_CHOICES, 
        widget=forms.Select(attrs={'placeholder': 'Select Branch', 'id': 'branch'})
    )
