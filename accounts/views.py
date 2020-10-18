from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests
from django.conf import settings
from urllib.parse import parse_qsl


@api_view(["POST"])
@permission_classes([AllowAny])
def get_access_token(request):
    code = request.data.get("code")
    state = request.data.get("state")
    response = requests.post(
        f"https://github.com/login/oauth/access_token?client_id={settings.SOCIAL_AUTH_GITHUB_KEY}&client_secret={settings.SOCIAL_AUTH_GITHUB_SECRET}&code={code}&state={state}"
    )
    if response.text:
        parsed_response = dict(parse_qsl(response.text))
        if parsed_response.get("error") and parsed_response.get("error_description"):
            return Response(parsed_response)
        access_token = parsed_response.get("access_token")
        token_type = parsed_response.get("token_type")
        if access_token:
            return Response({"accessToken": access_token, "token_type": token_type})
    return Response({"error": "Unable to login"})


# todo: create /me endpoint
