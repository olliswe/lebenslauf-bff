from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework import status
from weasyprint import HTML, CSS


def render_to_pdf(template_src, context_dict={}):
    try:
        template = get_template(template_src)
        html_string = template.render(context_dict)
        html = HTML(string=html_string)
        pdf = html.write_pdf(
            stylesheets=["http://127.0.0.1:8000/static/css/cv_template.css"]
        )
        return HttpResponse(pdf, content_type="application/pdf")
    except:
        return HttpResponse(
            "Unable to get PDF", status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
