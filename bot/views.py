from django.shortcuts import render
from django.http import JsonResponse
from gradio_client import Client

client = Client("Edwardhuero/DOJ_Chatbot")

def index(request):
    return render(request, 'chat.html')

def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        system_message = "You are a friendly Chatbot that is used for department of justice india website."
        result = client.predict(
            message=message,
            system_message=system_message,
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
        )
        return JsonResponse({'response': result})
    return JsonResponse({'error': 'Invalid request'}, status=400)
