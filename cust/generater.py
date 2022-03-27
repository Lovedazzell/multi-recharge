from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# this function generate random pdf
def render_to_pdf(template_src,content_dict ={}):
    # getting template 
    template = get_template(template_src)
    # passing data to templates
    html = template.render(content_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type = 'application/pdf')
    return None