from django.shortcuts import render
from django.http import JsonResponse
import requests

from urllib.parse import urlparse, parse_qs

def verCharacteres(request):
    # Obtiene el número de página de la solicitud, o usa '1' si no se proporciona ninguno
    page_number = request.GET.get('page', '1')

    # Construye la URL de la página
    page_url = f'https://rickandmortyapi.com/api/character?page={page_number}'

    # Realiza la solicitud GET a la API de Rick and Morty
    response = requests.get(page_url)

    # Comprueba si la solicitud tuvo éxito
    if response.status_code == 200:
        # Devuelve la respuesta JSON como un objeto JSON
        data = response.json()
        # Extrae los números de página de las URLs prev y next
        prev_page = data['info']['prev'].split('=')[-1] if data['info']['prev'] else None
        next_page = data['info']['next'].split('=')[-1] if data['info']['next'] else None

        # Calcula los números de las páginas que quieres mostrar
        pages_to_show = list(range(max(1, int(page_number) - 3), min(data['info']['pages'], int(page_number) + 3) + 1))

        context = {
            'characters': data['results'],
            'info': data['info'],
            'page': int(page_number),  # Añade el número de página al contexto
            'pages_to_show': pages_to_show, # Añade los números de las páginas a mostrar al contexto
            'prev_page': prev_page,  # Añade el número de la página previa al contexto
            'next_page': next_page   # Añade el número de la página siguiente al contexto
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