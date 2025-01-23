from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.

def home(request):
    response = requests.get('https://api.restful-api.dev/objects').json()
    return render(request, 'home.html', {'response': response})

def get_object(request):
    
    api_url = 'https://api.restful-api.dev/objects/6'

    
    response = requests.get(api_url)

    
    if response.status_code == 200: 
        object_data = response.json()
        return render(request, 'get_object.html', {'object_data': object_data})
    else:
        return JsonResponse({'message': 'Failed to fetch object', 'error': response.text}, status=response.status_code)


def create_object(request):
    if request.method == "POST":
        data = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }

        api_url = 'https://api.restful-api.dev/objects'
        response = requests.post(api_url, json=data)

        if response.status_code == 200:  
            return JsonResponse({'message': 'Object created successfully!', 'data': response.json()})
        else:
            return JsonResponse({'message': 'Failed to create object', 'error': response.text}, status=response.status_code)

    
    return render(request, 'create_object.html')



def update_object(request):
    if request.method == "POST":
        data = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 2049.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }

        api_url = 'https://api.restful-api.dev/objects/7'

        response = requests.put(api_url, json=data)

        if response.status_code == 405:  
            return JsonResponse({'message': 'Object updated successfully!', 'data': response.json()})
        else:
            return JsonResponse({'message': 'Failed to update object', 'error': response.text}, status=response.status_code)

    
    return render(request, 'update_object.html')

def delete_object(request):
    if request.method == "POST":
        
        api_url = 'https://api.restful-api.dev/objects/6'

        
        response = requests.delete(api_url)

        
        if response.status_code == 405: 
            return JsonResponse({'message': 'Object deleted successfully!'})
        else:
            return JsonResponse({'message': 'Failed to delete object', 'error': response.text}, status=response.status_code)

    
    return render(request, 'delete_object.html')