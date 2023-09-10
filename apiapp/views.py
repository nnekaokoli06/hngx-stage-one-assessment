from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from datetime import datetime
import pytz  # For working with timezones

def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    
    if not slack_name or not track:
            return JsonResponse({'error': 'Missing parameters'}, status=400)
    
    # Get the current day
    current_day = datetime.now(pytz.utc).strftime('%A')
    
    # Get the current UTC time
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"  # Replace with your GitHub URL
    github_repo_url = "https://github.com/username/repo"  # Replace with your GitHub URL

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
from django.http import JsonResponse
from datetime import datetime
import pytz  # For working with timezones

def get_jsondata(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    
    # Get the current day
    current_day = datetime.now(pytz.utc).strftime('%A')
    
    # Get the current UTC time
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = "https://github.com/nnekaokoli06/hngx-stage-one-assessment/blob/main/apiapp.ext"  #My GitHub file url
    github_repo_url = "https://github.com/nnekaokoli06/hngx-stage-one-assessment"  # My GitHub url

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
