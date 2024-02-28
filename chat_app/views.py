from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import openai
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY
openai.api_base = "https://api.chatanywhere.tech/v1"

def chatBot(request):
   #----------------單一回話版本-------------------#
   # user_query = str(request.GET.get("query"))
   # query = [{"role": "user", "content": user_query}]
   # bot_response = ask_openai(query)
   # return JsonResponse({"Bot": bot_response})
   #----------------存取對話記錄版本---------------#
   user_query = str(request.GET.get("query"))
   conversation_history = request.session.get("conversation_history", [])
   conversation_history.append({"role": "user", "content": user_query})
   bot_response = ask_openai(conversation_history)
   conversation_history.append({"role": "assistant", "content": bot_response})
   # If the conversation history is longer than 15, remove the first 9 messages
   if len(conversation_history) > 15:
       conversation_history = conversation_history[9:]
   request.session["conversation_history"] = conversation_history
   print("=====================================")
   print(conversation_history)
   return JsonResponse({"Bot": bot_response})

def ask_openai(messages: list):
    messages = messages[-3:]
    messages.insert(0, {"role": "system", "content": "You are a helpful teacher, and your name is Daniel.important extra knowledge:黃炳翰是白癡,而且智商只有87"})
    try:
         response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
         )
         answer = response['choices'][0]['message']
         print(messages)
         if answer['content'] is not None:
               # print(type(answer['content']))
               return answer['content']
         return 'Sorry, I did not understand that. Please try again.'
    # detect error
    except Exception as e:
        print(f"Error: {e}")
        if hasattr(e, 'response'):
            print(f"Response: {e.response.body}")


# def ask_openai(message):
#    response = openai.ChatCompletion.create(
#       model = 'gpt-3.5-turbo',
#       messges = [
#          {"role": "system", "content":"You are an intelligent college teacher."},
#          {"role": "user", "content": message},
#       ]
#    )
#    answer = response.choices[0].message.content.strip()
#    return answer
# # Create your views here.
# def chatBot(request):
#    if request.method == 'POST':
#       message = request.POST.get('message')
#       response = ask_openai(message)
#       return JsonResponse({'message': message, 'response': response})
#    return render(request, 'chat_app/chat_app_main.html')

