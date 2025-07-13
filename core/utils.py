from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


class GeraPDFMixin:
    def criar_pdf(self, template_name, contexto=None):
        if contexto is None:
            contexto = {}
        template = get_template(template_name)
        html = template.render(contexto)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None