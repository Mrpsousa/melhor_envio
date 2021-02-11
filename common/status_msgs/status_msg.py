from rest_framework import status
from rest_framework.response import Response


def error_data_format_400():
    return Response('Error: data format',
                    status=status.HTTP_400_BAD_REQUEST)


def error_500(err):
    return Response(f'Error: {err}',
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def sucess_201(data):
    return Response(data, status=status.HTTP_201_CREATED)


def sucess_data_200(data):
    return Response(data, status=status.HTTP_200_OK)


def sucess_200():
    return Response(status=status.HTTP_200_OK)