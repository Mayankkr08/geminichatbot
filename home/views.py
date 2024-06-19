from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai

genai.configure(api_key="AIzaSyA9iV_K8VizQH3ToB3-AKdUcAUxdfMbiXU")

def home(request):
    return render(request, "index.html")

def About(request):
    return render(request, "About.html")

def ChatAPI(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            try:
                # Create generative model and start chat
                model = genai.GenerativeModel("gemini-1.5-flash")
                chat = model.start_chat()
                response = chat.send_message(prompt)
                
                # Save chat interaction
                user = request.user if request.user.is_authenticated else None
                ChatBot.objects.create(text_input=prompt, gemini_output=response.text, user=user)
                
                # Prepare response data
                response_data = {
                    "text": response.text  # Ensure only the relevant response text is returned
                }
                return JsonResponse(response_data)
            except Exception as e:
                print(f"Error: {e}")
                return JsonResponse({"error": str(e)}, status=500)
        else:
            return JsonResponse({"error": "Invalid input"}, status=400)
    else:
        return HttpResponseRedirect(reverse("home"))
