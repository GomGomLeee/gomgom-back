from django.shortcuts import render, redirect
from googletrans import Translator
import os
import openai
from posts.models import Post

# 실제 시연 여기 풀기
# openai.api_key = os.environ['OPENAI_API_KEY']

# 곰곰AI 페이지 접속 시
def ai_view(request):
    
    # 질문 받기
    question_ko = request.GET.get('question', '')
    
    # 번역기 객체 선언
    # translator = Translator()
    
    # 질문이 있는 경우
    if len(str(question_ko)) >= 1:
        # 로그인이 된 상태에서만 이용 가능함
        if request.user.is_authenticated:
            # question_en = translator.translate(question_ko, src='ko', dest='en')
            # response_en = ask_gpt(str(question_en.text))
            # response_ko = translator.translate(response_en, src='en', dest='ko')
            # 답변이 포함된 페이지로 렌더링 해주기
            # 실제 시연 여기 풀기
            # context = { 'question' : question_ko,
                        # 'response' : response_ko.text,}
            # 테스트
            context = { 'question' : question_ko,
                        'response' : "성공" }
            # print(response_ko.text)
            return render(request, 'gomgom/ai_response.html',context)
        # 로그인이 안 된 상태이면 로그인 화면으로 이동
        else:
            return redirect('accounts:login')
    
    # 질문이 없는 경우
    else:
        # 답변이 포함 안된 페이지로 렌더링 해주기
        return render(request, 'gomgom/ai.html')        

# 곰곰AI에게 질문 보내고 답변 받기
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def home_view(request):
    gomgom_post_list = Post.objects.filter(writer__username='gomgom')
    post_list = Post.objects.exclude(writer__username='gomgom').order_by('-created_at')[:8]
    
    context = {
        'post_list' : post_list,
        'gomgom_post_list' : gomgom_post_list,
    }
    return render(request, 'gomgom/home.html', context)