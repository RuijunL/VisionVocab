from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .core.processor import ImageProcessModel

model = ImageProcessModel("Salesforce/blip-image-captioning-base")

@csrf_exempt
def generate_caption(request):
    if request.method == "POST" and request.FILES.get("image"):
        caption = model.process_image(request.FILES["image"])
        return JsonResponse({"caption": caption})
    return JsonResponse({"error": "no image uploaded"}, status = 400)


