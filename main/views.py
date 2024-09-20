import requests
from django.views.generic import TemplateView
from django.conf import settings


class AzuraCastAPI():
    def __init__(self, domain, api_key, port=443, secure=True):
        self.domain = domain
        self.port = port
        self.api_key = api_key
        self.secure = secure

    def command(self, command):
        if self.secure:
            url = f'https://{self.domain}:{self.port}/api/{command}'
        else:
            url = f'http://{self.domain}:{self.port}/api/{command}'
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'Failed to fetch data from AzuraCast API'}


class PlayerView(TemplateView):
    template_name = 'main/player.html'
    AzuraCastAPI = AzuraCastAPI(
        settings.API_DOMAIN,
        settings.API_KEY
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        azuracast = self.AzuraCastAPI.command('nowplaying/1')
        elapsed = azuracast['now_playing']['elapsed']
        duration = azuracast['now_playing']['duration']
        azuracast['now_playing']['percent'] = (elapsed / duration) * 100 if duration > 0 else 0
        context['azuracast'] = azuracast
        return context
