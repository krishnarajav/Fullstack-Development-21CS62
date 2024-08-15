from reportlab.pdfgen import canvas
import csv
from exp10.models import Book
from django.http import HttpResponse

def export_books_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    #This initializes a CSV writer object that will write to the HttpResponse object
    writer = csv.writer(response) 
    # Write the header row
    writer.writerow(['Title', 'Publication Date', 'Publisher'])
    # Write data rows
    books = Book.objects.all()
    for book in books:
        writer.writerow([book.title, book.publication_date, book.publisher])
    return response

def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hello.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 800, "Hello world.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
