from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from streamingapp.models import StreamHelper


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def updateCount(request):
    # print(request.user.get_all_permissions())

    if request.user.has_perm('randoPerm'):
        print("has permission")
    else:
        print("has no permission")

    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
        "perm": str(request.user.get_all_permissions())
    }

    stream, _ = StreamHelper.objects.get_or_create(user=request.user)
    if _ is False:
        stream.count = stream.count + 1
        stream.save()
    count = stream.count
    return Response({
        "message": "Updated count, current count is " + str(count),
        "content": content})


@api_view(['POST'])
def viewCount(request):
    count = 0
    return Response({"message": "Updated count, current count is "+str(count)})


@api_view(['POST'])
def dropCount(request):
    count = 0
    return Response({"message": "Updated count, current count is "+str(count)})
