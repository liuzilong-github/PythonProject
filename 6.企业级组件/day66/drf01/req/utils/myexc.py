
from rest_framework.views import exception_handler
from req.views import AA
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    ret = exception_handler(exc, context)
    print('>>>>>>', exc, context)
    if not ret:
        if isinstance(exc, AA):
            return Response({'error': '大A错误'}, status=500)
        else:
            return None