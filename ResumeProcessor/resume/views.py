# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Candidate
# from .serializers import CandidateSerializer
# from pyresparser import ResumeParser
# import os
# from django.shortcuts import render


# from tempfile import gettempdir
# import os

# @api_view(['POST'])
# def extract_resume(request):
#     if 'resume' in request.FILES:
#         resume = request.FILES['resume']
        
#         # Get the system's temporary directory
#         temp_dir = gettempdir()
#         resume_path = os.path.join(temp_dir, resume.name)
        
#         # Save resume temporarily
#         with open(resume_path, 'wb+') as destination:
#             for chunk in resume.chunks():
#                 destination.write(chunk)

#         # Use ResumeParser to extract data
#         parsed_data = ResumeParser(resume_path).get_extracted_data()

#         # Create Candidate object
#         candidate = Candidate(
#             first_name=parsed_data.get('name', '').split()[0],
#             email=parsed_data.get('email'),
#             mobile_number=parsed_data.get('mobile_number')
#         )
#         candidate.save()

#         # Serialize and return response
#         serializer = CandidateSerializer(candidate)
#         return Response(serializer.data)
#     return Response({'error': 'Resume file not provided'}, status=400)

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from .models import Candidate
from .resume_parser import extract_text_from_pdf, extract_candidate_info

@csrf_exempt
def extract_resume(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        resume_file = request.FILES['resume']
        
        # Save the resume file to the database
        candidate = Candidate(
            first_name="Unknown",  # Placeholder, will update after parsing
            email="Unknown",       # Placeholder, will update after parsing
            mobile_number="Unknown",  # Placeholder, will update after parsing
            resume=resume_file
        )
        candidate.save()
        
        # Get the path of the saved resume
        file_path = candidate.resume.path
        
        # Use your custom parser
        text = extract_text_from_pdf(file_path)
        candidate_info = extract_candidate_info(text)
        
        # Update the candidate with parsed information
        candidate.first_name = candidate_info['first_name']
        candidate.email = candidate_info['email']
        candidate.mobile_number = candidate_info['mobile_number']
        candidate.save()
        
        return JsonResponse(candidate_info)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def home(request):
    return render(request, 'resume/home.html')
