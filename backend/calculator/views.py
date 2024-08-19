from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add(request):
    try:
        a = request.data.get('a')
        b = request.data.get('b')
        if a is None or b is None:
            raise ValueError("Missing input values for 'a' or 'b'")
        a = float(a)
        b = float(b)
        result = a + b
        return Response({'result': result})
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def subtract(request):
    try:
        a = request.data.get('a')
        b = request.data.get('b')
        if a is None or b is None:
            raise ValueError("Missing input values for 'a' or 'b'")
        a = float(a)
        b = float(b)
        result = a - b
        return Response({'result': result})
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def multiply(request):
    try:
        a = request.data.get('a')
        b = request.data.get('b')
        if a is None or b is None:
            raise ValueError("Missing input values for 'a' or 'b'")
        a = float(a)
        b = float(b)
        result = a * b
        return Response({'result': result})
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def divide(request):
    try:
        a = request.data.get('a')
        b = request.data.get('b')
        if a is None or b is None:
            raise ValueError("Missing input values for 'a' or 'b'")
        a = float(a)
        b = float(b)
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        return Response({'result': result})
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
