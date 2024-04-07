import datetime
from django.http import Http404

from .render import render_to_pdf

def advanced_pdf_view(request):
    invoice_number = "007cae"
    context = {
        "passenger": "Jaloliddin Murodullaev",
        "flight_number": f"TK-122",
        "amount": "100 USD",
        "seat_number": "A15",
        "pdf_title": f"Invoice #{invoice_number}",
    }
    response = render_to_pdf("invoice.html", context)
    if response.status_code == 404:
        raise Http404("Invoice not found")

    filename = f"Invoice_{invoice_number}.pdf"
    # filename.save()
    """
    Tell browser to view inline (default)
    """
    content = f"inline; filename={filename}"
    download = request.GET.get("download")
    if download:
        """
        Tells browser to initiate download
        """
        content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response
