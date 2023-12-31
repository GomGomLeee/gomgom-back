from django import forms
from .models import Selection,Post, Comment

# 게시글 작성 폼
class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateForm(PostBaseForm):
    CATEGORY_CHOICES=[
        ('대인관계','대인관계'),
        ('연애','연애'),
        ('교육','교육'),
        ('생활','생활'),
        ('건강','건강'),
        ('반려동물','반려동물'),
        ('여행','여행'),
        ('쇼핑','쇼핑'),
        ('기타','기타'),
    ]
    #선택지1
    image1=forms.ImageField(label = '이미지', required = False)
    selection_content1=forms.CharField(label = '선택지 내용',max_length=20)
    #선택지2
    image2=forms.ImageField(label = '이미지', required = False)
    selection_content2=forms.CharField(label = '선택지 내용',max_length=20)
    
    category = forms.ChoiceField(label='카테고리',choices= CATEGORY_CHOICES)
    class Meta(PostBaseForm.Meta):
        fields = ['title','content']

# 댓글 작성 폼
class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreationForm(CommentBaseForm):
    class Meta(CommentBaseForm.Meta):
        fields = ['image', 'content']
        
class CommentForm(CommentCreationForm):
    content = forms.CharField(
        label = '내용',
        initial = '',
        widget = forms.TextInput(attrs = {
            'class' : 'form-content',
            'placeholder' : '내용을 입력하세요',
        })
    )
    image = forms.ImageField(
        label = '이미지',
        required = False,
        widget = forms.FileInput(attrs = {
            'class' : 'form-image',
            'placeholder' : '댓글 이미지 업로드'
        }),
    )
