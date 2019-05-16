from django import forms
from .models import Shout

# shout 모델에 기반하여, django가 만들어주는 form
class ShoutForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(max_length=200)
    
# ModelForm
class ShoutModelForm(forms.ModelForm):
    
    class Meta:
        model = Shout
        fields = ['title','content']
        widgets = {
            'title': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '제목을 입력해주세영',
                }
            ),
            'content': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '제목을 입력해주세영',
                }
            )
        }
    
    