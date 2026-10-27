import json
from pathlib import Path

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

STATIC = Path(__file__).resolve().parent.parent / 'frontend' / 'static'
LOCATIONS = [
    ('El Paso', 'Texas', 'TX'), ('San Francisco', 'California', 'CA'),
    ('Topeka', 'Kansas', 'KS'), ('Wichita', 'Kansas', 'KS'),
    ('Kansas City', 'Kansas', 'KS'), ('Tampa', 'Florida', 'FL'),
    ('Clearwater', 'Florida', 'FL'), ('St Pete Beach', 'Florida', 'FL'),
    ('Orlando', 'Florida', 'FL'), ('West Palm Beach', 'Florida', 'FL'),
    ('Miami', 'Florida', 'FL'), ('Austin', 'Texas', 'TX'),
    ('Dallas', 'Texas', 'TX'), ('Houston', 'Texas', 'TX'),
    ('Phoenix', 'Arizona', 'AZ'), ('Tucson', 'Arizona', 'AZ'),
    ('Los Angeles', 'California', 'CA'), ('San Diego', 'California', 'CA'),
    ('Sacramento', 'California', 'CA'), ('Seattle', 'Washington', 'WA'),
    ('Tacoma', 'Washington', 'WA'), ('Portland', 'Oregon', 'OR'),
    ('Salem', 'Oregon', 'OR'), ('Denver', 'Colorado', 'CO'),
    ('Boulder', 'Colorado', 'CO'), ('Chicago', 'Illinois', 'IL'),
    ('Springfield', 'Illinois', 'IL'), ('Indianapolis', 'Indiana', 'IN'),
    ('Columbus', 'Ohio', 'OH'), ('Cleveland', 'Ohio', 'OH'),
    ('Detroit', 'Michigan', 'MI'), ('Ann Arbor', 'Michigan', 'MI'),
    ('Nashville', 'Tennessee', 'TN'), ('Memphis', 'Tennessee', 'TN'),
    ('Atlanta', 'Georgia', 'GA'), ('Savannah', 'Georgia', 'GA'),
    ('Charlotte', 'North Carolina', 'NC'), ('Raleigh', 'North Carolina', 'NC'),
    ('Richmond', 'Virginia', 'VA'), ('Norfolk', 'Virginia', 'VA'),
    ('Baltimore', 'Maryland', 'MD'), ('Boston', 'Massachusetts', 'MA'),
    ('Buffalo', 'New York', 'NY'), ('New York', 'New York', 'NY'),
    ('Newark', 'New Jersey', 'NJ'), ('Philadelphia', 'Pennsylvania', 'PA'),
    ('Pittsburgh', 'Pennsylvania', 'PA'), ('Minneapolis', 'Minnesota', 'MN'),
    ('Omaha', 'Nebraska', 'NE'), ('Las Vegas', 'Nevada', 'NV'),
]
DEALERS = [
    {'id': i, 'city': city, 'state': state, 'st': code,
     'address': f'{100 + i} Main Street', 'zip': f'{70000 + i:05d}',
     'lat': 30 + i / 10, 'long': -110 + i / 10,
     'short_name': f'{city} Auto', 'full_name': f'{city} Best Cars Dealership'}
    for i, (city, state, code) in enumerate(LOCATIONS, 1)
]
CAR_MODELS = [('NISSAN', 'Pathfinder'), ('NISSAN', 'Qashqai'),
              ('NISSAN', 'XTRAIL'), ('Mercedes', 'A-Class'),
              ('Mercedes', 'C-Class'), ('Mercedes', 'E-Class'),
              ('Audi', 'A4'), ('Audi', 'A5'), ('Audi', 'A6'),
              ('Kia', 'Sorrento'), ('Kia', 'Carnival'), ('Kia', 'Cerato'),
              ('Toyota', 'Corolla'), ('Toyota', 'Camry'), ('Toyota', 'Kluger')]
REVIEWS = [{'id': 1, 'name': 'Taylor Reed', 'dealership': 3,
            'review': 'Fantastic services', 'purchase': True,
            'purchase_date': '10/27/2026', 'car_make': 'Audi',
            'car_model': 'A6', 'car_year': 2023}]


def home(request):
    return render(request, 'home.html', {'dealers': DEALERS,
                                         'logged_out': request.GET.get('logged_out') == '1'})


def signup(request):
    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('/?logged_out=1')


def about(request):
    return FileResponse((STATIC / 'About.html').open('rb'), content_type='text/html')


def contact(request):
    return FileResponse((STATIC / 'Contact.html').open('rb'), content_type='text/html')


def get_dealers(request):
    return JsonResponse(DEALERS, safe=False)


def get_dealer(request, dealer_id):
    return JsonResponse([x for x in DEALERS if x['id'] == dealer_id], safe=False)


def get_dealers_by_state(request, state):
    return JsonResponse([x for x in DEALERS if x['state'].lower() == state.lower()], safe=False)


def get_reviews(request, dealer_id):
    return JsonResponse([x for x in REVIEWS if x['dealership'] == dealer_id], safe=False)


def analyze_review(request, review_text):
    positive = {'fantastic', 'great', 'excellent', 'friendly', 'good', 'helpful'}
    negative = {'bad', 'poor', 'awful', 'terrible', 'rude'}
    tokens = set(review_text.lower().split())
    score = len(tokens & positive) - len(tokens & negative)
    return JsonResponse({'sentiment': 'positive' if score > 0 else 'negative' if score < 0 else 'neutral'})


def get_cars(request):
    return JsonResponse({'CarModels': [{'CarModel': model, 'CarMake': make}
                                       for make, model in CAR_MODELS]})


@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    data = json.loads(request.body or '{}')
    required = ('userName', 'firstName', 'lastName', 'email', 'password')
    if any(not data.get(key) for key in required):
        return JsonResponse({'error': 'All fields are required'}, status=400)
    if User.objects.filter(username=data['userName']).exists():
        return JsonResponse({'error': 'Username already exists'}, status=409)
    User.objects.create_user(username=data['userName'], password=data['password'],
                             first_name=data['firstName'], last_name=data['lastName'],
                             email=data['email'])
    return JsonResponse({'userName': data['userName'], 'status': 'Registered'}, status=201)


@csrf_exempt
def login_user(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    data = json.loads(request.body or '{}')
    user = authenticate(request, username=data.get('userName'), password=data.get('password'))
    if user is None:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
    login(request, user)
    return JsonResponse({'userName': user.username, 'status': 'Authenticated'})


def logout_user(request):
    logout(request)
    return JsonResponse({'userName': ''})
