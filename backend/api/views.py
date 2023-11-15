import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializer import ProductSerializer
from products.models import Product


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return JsonResponse(data)
