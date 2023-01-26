from django import forms


class UploadFileForm(forms.Form):
    file_cnab = forms.FileField(label="Arquivo:")