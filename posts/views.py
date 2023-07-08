from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Selection, Comment
from .forms import PostCreateForm, CommentForm
from django import forms

# Create your views here.


@login_required(login_url='/accounts/login/')
def post_create_form_view(request,selection_count=2):
    if request.method=='GET':
        selection_count+=1
        form = PostCreateForm()
        context = {'form':form}
        return render(request,'posts/post-create-form-view.html',context)
    if request.method=='POST':
        if 'post' in request.POST:
            form = PostCreateForm(request.POST,request.FILES)
            if form.is_valid():
                post = Post.objects.create(
                    title = form.cleaned_data['title'],
                    content=form.cleaned_data['content'],
                    writer=request.user,
                    category = form.cleaned_data['category'],
                )
                post.save()
                Selection.objects.create(
                    image = form.cleaned_data['image1'],
                    content = form.cleaned_data['selection_content1'],
                    post=post
                )
                Selection.objects.create(
                    image = form.cleaned_data['image2'],
                    content = form.cleaned_data['selection_content2'],
                    post=post
                )
            else:
                # return redirect('/admin')
                return render(request, 'posts/post-create-complete.html')
            return render(request, 'posts/post-create-complete.html')
            # return redirect('/admin')

@login_required
def post_list_view(request):
    if request.method == 'GET':
        selected_category = request.GET.get('category') 
        post_list = Post.objects.all() # Post 전체 데이터 조회
        if selected_category is None: # 처음에 버튼 선택 안할시, queryset 데이터에 아무것도 없음.
            selected_category = '대인관계'  # 그래서 디폴트 값은 대인관계로 설정
            
        print(selected_category)
        filter_list = Post.objects.filter(category=selected_category) # 사용자가 선택한 카테고리와 같은것만 필터링
        selection_list = Selection.objects.all()
        context = {
            'post_list': post_list,
            'selection_list': selection_list,
            'filter_list': filter_list,
            'selected_category': selected_category
        }
        return render(request, 'posts/post-list-all.html', context)
    
# 상세 목록 보기
@login_required
def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    
    # 요청이 GET인 경우
    if request.method == 'GET':
        # 로그인이 안된 상태라면
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        # 로그인이 된 상태라면
        else:
            context = {
            'post' : post,
            'comment_form' : CommentForm(),
        }
        return render(request, 'posts/post-detail.html', context)
    # 요청이 POST인 경우
    if request.method == 'POST':
        # 댓글 작성
        # 로그인이 안된 상태라면
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        # 로그인이 된 상태라면
        else:
            comment_form = CommentForm(request.POST,request.FILES)
            if comment_form.is_valid():
                comment_form = Comment.objects.create(
                    content = comment_form.cleaned_data['content'],
                    writer = request.user,
                    image = comment_form.cleaned_data['image'],
                    post = post
                )
                context = {
                'post' : post,
                'comment_form' : comment_form,
                }
                return render(request, 'posts/post-detail.html', context)
            else:
                context = {
                'post' : post,
                'comment_form' : CommentForm(),
                }
            return render(request, 'posts/post-detail.html', context)
@login_required
def post_create_complete(request):
    return redirect('posts:post-create-complete')

