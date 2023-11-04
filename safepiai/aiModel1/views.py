from django.shortcuts import render
from .models import OCRModel

def process_photos(request):
    if request.method == 'POST':
        uploaded_photos = request.FILES.getlist('photos')
        ocr_model = OCRModel()
        results = []

        for photo in uploaded_photos:
            result = ocr_model.process_image(photo)
            results.append(result)

        return render(request, 'aiModel1/results.html', {'results': results})
    return render(request, 'aiModel1/upload.html')
