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
            stylesheets=[
                "https://unpkg.com/basscss@8.0.2/css/basscss.min.css",
                "http://127.0.0.1:8000/static/css/cv_template.css",
                "https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css",
            ]
        )
        return HttpResponse(pdf, content_type="application/pdf")
    except Exception as e:
        print(e)
        return HttpResponse(
            "Unable to get PDF", status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
