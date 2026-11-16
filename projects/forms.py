import os
from django import forms
from django.core.exceptions import ValidationError
from .models import Project
# lets create our form here
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'budget', 'proposal_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'budget': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'proposal_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_budget(self):
        budget = self.cleaned_data.get('budget')
        if budget is not None and budget <= 0:
            raise ValidationError("Budget must be greater than zero.")
        return budget

    def clean_proposal_file(self):
        file = self.cleaned_data.get('proposal_file')
        if file:
            # 1. file size (Limit to 5 MB)
            max_size = 5 * 1024 * 1024  # 5MB in bytes
            if file.size > max_size:
                raise ValidationError("File size cannot exceed 5 MB.")

            # 2. check file ext
            ext = os.path.splitext(file.name)[1].lower()
            valid_extensions = ['.pdf', '.docx', '.png', '.jpg', '.jpeg']
            if ext not in valid_extensions:
                raise ValidationError(
                    f"Unsupported file type '{ext}'. Allowed: {', '.join(valid_extensions)}"
                )
        return file

    def clean(self):
        cleaned_data = super().clean()
        budget = cleaned_data.get('budget')
        description = cleaned_data.get('description')

        # Cross-field validation
        if budget and budget > 10000 and (not description or len(description.strip()) < 20):
            self.add_error(
                'description',
                "Projects with a budget over $10,000 require a description of at least 20 characters."
            )
        return cleaned_data