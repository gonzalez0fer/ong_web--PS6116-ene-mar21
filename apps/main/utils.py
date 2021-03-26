from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa

import requests

def get_exchange_rate():
    r = requests.get('https://s3.amazonaws.com/dolartoday/data.json')
    return r.json()['USD']['sicad2']

def render_pdf_view(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None