from django.shortcuts import render
from django.http import JsonResponse
import openai

open_api_key = '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'
openai.api_key = open_api_key

def ask_openai(message):
   response = openai.ChatCompletion.create(
      model = 'gpt-3.5-turbo',
      messges = [
         {"role": "system", "content":"You are an intelligent college teacher."},
         {"role": "user", "content": message},
      ]
   )
   answer = response.choices[0].message.content.strip()
   return answer
# Create your views here.
def chatBot(request):
   if request.method == 'POST':
      message = request.POST.get('message')
      response = ask_openai(message)
      return JsonResponse({'message': message, 'response': response})
   return render(request, 'chat_app/chat_app_main.html')