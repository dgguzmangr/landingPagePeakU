import os

from django.conf import settings
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse, FileResponse, HttpResponseNotFound

from authApp.models.articles import Articles
from authApp.models.customers import Customers
from authApp.models.destinations import Destinations
from authApp.models.opinions import Opinions
from authApp.models.promotions import Promotions

from authApp.serializers.articlesSerializer import ArticlesSerializer
from authApp.serializers.customersSerializer import CustomersSerializer
from authApp.serializers.destinationsSerializer import DestinationsSerializer
from authApp.serializers.opinionsSerializer import OpinionsSerializer
from authApp.serializers.promotionsSerializer import PromotionsSerializer


@api_view(['GET', 'POST'])
def show_destinations(request):
    if request.method == 'GET':
        destinations = Destinations.objects.all()
        return JsonResponse([DestinationsSerializer(destination).data for destination in destinations], status=200,
                            safe=False)


def show_articles(request):
    if request.method == 'GET':
        articles = Articles.objects.all()
        return JsonResponse([ArticlesSerializer(article).data for article in articles], status=200,
                            safe=False)


def show_promotions(request):
    if request.method == 'GET':
        promotions = Promotions.objects.all()
        return JsonResponse([PromotionsSerializer(promotion).data for promotion in promotions], status=200,
                            safe=False)


def show_opinions(request):
    if request.method == 'GET':
        opinions = Opinions.objects.all()
        return JsonResponse([OpinionsSerializer(opinion).data for opinion in opinions], status=200,
                            safe=False)


def collect_email(request):
    if request.method == 'POST':
        customers = Customers.objects.all()
        return JsonResponse([CustomersSerializer(customer).data for customer in customers], status=200,
                            safe=False)


def get_image(request, image_path):
    image_full_path = os.path.join(settings.MEDIA_ROOT, image_path)

    if os.path.exists(image_full_path):
        return FileResponse(open(image_full_path, 'rb'), content_type='image/png')
    else:
        return HttpResponseNotFound()











class LandingPageView(generics.ListAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestinationsSerializer

    def get(self, request):
        base_url = request.build_absolute_uri('/')
        return Response([
            {'destination_id': destination.destination_id,
             'destination_img_url': request.build_absolute_uri(destination.destination_img.url),
             'city': destination.city,
             'country': destination.country,
             'average_mark': destination.average_mark,
             'cost': destination.cost,
             'discount_price': destination.discount_price
             } for destination in self.get_queryset()
        ])

    def put(self, request):
        # Escribir lógica para el método "put" aquí
        return Response({'message': 'Método PUT ejecutado correctamente'})
