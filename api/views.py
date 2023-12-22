from django.shortcuts import render
from django.http import JsonResponse
import requests

from urllib.parse import urlparse, parse_qs

def verCharacteres(request):
    # Obtiene la URL de la página de la solicitud, o usa la URL de la primera página si no se proporciona ninguna
    page_url = request.GET.get('page', 'https://rickandmortyapi.com/api/character')

    # Extrae el número de página de la URL
    page_number = parse_qs(urlparse(page_url).query).get('page', [1])[0]

    # Realiza la solicitud GET a la API de Rick and Morty
    response = requests.get(page_url)

    # Comprueba si la solicitud tuvo éxito
    if response.status_code == 200:
        # Devuelve la respuesta JSON como un objeto JSON
        data = response.json()
        context = {
            'characters': data['results'],
            'info': data['info'],
            'page': page_number  # Añade el número de página al contexto
        }
        return render(request, 'index.html', context)
    else:
        return JsonResponse({'error': 'Something went wrong'}, status=response.status_code)


def getApi(request):
    response = requests.get('https://rickandmortyapi.com/api/')

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Something went wrong'}, status=response.status_code)
    
# def getApi(request):
#     response = requests.get('https://rickandmortyapi.com/api/')

#     if response.status_code == 200:
#         data = response.json()
#         return render(request, 'api.html', data)
#     else:
#         return JsonResponse({'error': 'Something went wrong'}, status=response.status_code)