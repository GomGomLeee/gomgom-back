from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect,render
from accounts.forms import signupForm
from posts.models import Post, Comment
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

# 최종 완성

# 회원가입
def signup_view(request):
    #GET 요청시, 회원 가입 HTML render
    if request.method=='GET':
        form = signupForm
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
    #POST 요청으로 정보 가져옴 & 회원 생성    
        form = signupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            #회원가입이 실패하면 다시 회원가입 페이지로 이동
            return redirect('accounts:signup')
    
            
# 로그인
def login_view(request):
    if request.method=='GET':
        #GET 요청시 로그인 페이지 내보냄
        return render(request,'accounts/login.html',{'form':CustomAuthenticationForm()})
    else:
        #개인정보는 post 요청으로 받아옴 (CustomAuthenticationForm으로..)
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
                login(request, form.user_cache)
                return redirect('gomgom:home')

        else: #비지니스 로직 실패 ( 로그인 실패 )
            print(form.error_messages)
            return render(request,'accounts/login.html',{'form':CustomAuthenticationForm()})

# 로그아웃
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('gomgom:home')

# 마이페이지 (1. 내가 작성한 글, 2. 내가 공감한 글, 3. 내가 답변한 글)
@login_required
def mypage_view(request):
    if request.method == 'GET':
        post = Post
        name = request.GET.get("mypage")
        
        my_post_list = Post.objects.filter(writer = request.user).order_by('-created_at') 
        my_heart_list = Post.objects.filter(like = request.user).order_by('-created_at')
        
        comment_list = Comment.objects.filter(writer=request.user)
        post_ids = comment_list.values_list('post_id', flat=True) 
        my_comment_list = Post.objects.filter(id__in=post_ids).order_by('-created_at')
        
        if name is None:    #name 디폴트 값 설정 
            name = "mypost"
            
        # Post.writer 가 현재 로그인인 것 조회 (1. 내가 작성한 글 )
        if name =="mypost":
            print("내가 작성한 글 출력")
            context = {
                'main_list':my_post_list,
                'post_list':my_post_list,
                'heart_list':my_heart_list,
                'comment_list':my_comment_list,
            }
        elif name =="myheart":
            print("내가 공감한 글 출력")
            context = {
                'main_list':my_heart_list,
                'post_list':my_post_list,
                'heart_list':my_heart_list,
                'comment_list':my_comment_list,
            }
        
        elif name =="mycomment":
            print("내가 답변한 글 출력")
            context = {
                'main_list':my_comment_list,
                'post_list':my_post_list,
                'heart_list':my_heart_list,
                'comment_list':my_comment_list,
            }

        return render(request, 'accounts/mypage.html', context)