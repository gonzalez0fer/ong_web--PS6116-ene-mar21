from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django import template
from django.contrib.staticfiles import finders

import os.path
import requests



def get_exchange_rate():
    r = requests.get('https://s3.amazonaws.com/dolartoday/data.json')
    return r.json()['USD']['sicad2']

#TODO validar url en linux y luego ver como se hara en Heroku
def fetch_resources(uri, rel):
	local = os.path.join(settings.BASE_DIR, 'ong_web')
	path = os.path.join(local, uri.replace(settings.STATIC_URL, ""))
	return path

def render_pdf_view(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, link_callback=fetch_resources)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

	