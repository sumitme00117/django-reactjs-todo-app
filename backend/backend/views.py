import requests



def home(request):
    response = requests.get('https://api.restful-api.dev/objects').json()
    return render(request, 'home.html', {'response': response})