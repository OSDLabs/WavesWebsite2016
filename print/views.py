from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from wavesprofile.models import *
from reportlab.lib.utils import ImageReader
# from reportlab.pdfbase.pdfmetrics import stringWidth
# from reportlab.rl_config import defaultPageSize

MAX_WIDTH = 595.27
MAX_HEIGHT = 841.89


# PAGE_WIDTH  = defaultPageSize[0]
# PAGE_HEIGHT = defaultPageSize[1]

class UsernameBarcode(Drawing):
    def __init__(self, text_value, *args, **kw):
        barcode = createBarcodeDrawing('Code128', value=text_value,  barHeight=100*mm, barWidth=2*mm, humanReadable=True)
        Drawing.__init__(self,barcode.width,barcode.height,*args,**kw)       
        self.add(barcode, name='barcode')
        

if __name__=='__main__':
    #use the standard 'save' method to save barcode.gif, barcode.pdf etc
    #for quick feedback while working.
    UsernameBarcode("HELLO WORLD").save(formats=['gif','pdf'],outDir='.',fnRoot='barcode')

def barcode(request):
    #instantiate a drawing object
    d = UsernameBarcode(request.user.username)
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')

def PassSlip(request):
    profile_obj = Profile.objects.get(user=request.user)
    print()
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="PassSlip.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    p.rect(25, 25, MAX_WIDTH-50, MAX_HEIGHT-50, stroke=1, fill=0)
    # text = "Waves 2016"
    # text_width = stringWidth(text)
    # y = 35
    # pdf_text_object = canvas.beginText((PAGE_WIDTH - text_width) / 2.0, y)
    # pdf_text_object.textOut(text)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    DETAILS_HEIGHT = MAX_HEIGHT-100
    p.drawCentredString(MAX_WIDTH/2, MAX_HEIGHT-45, "Waves 2016")
    p.drawCentredString(MAX_WIDTH/2, MAX_HEIGHT-65, "BITS Pilani K.K. Birla Goa Campus")
    p.drawCentredString(MAX_WIDTH/2, MAX_HEIGHT-95, "Pass Slip")
    p.drawString(45, DETAILS_HEIGHT-115, "Name")
    p.drawString(45, DETAILS_HEIGHT-140, "Mobile")
    p.drawString(45, DETAILS_HEIGHT-165, "Institute")
    p.drawString(95, DETAILS_HEIGHT-115, ":")
    p.drawString(95, DETAILS_HEIGHT-140, ":")
    p.drawString(95, DETAILS_HEIGHT-165, ":")
    p.drawString(115, DETAILS_HEIGHT-115, profile_obj.name)
    p.drawString(115, DETAILS_HEIGHT-140, "+91 " + profile_obj.mobile)
    p.drawString(115, DETAILS_HEIGHT-165, profile_obj.institute)
    # img = ImageReader(profile_obj.pic)
    # p.drawImage(img, MAX_WIDTH-180,MAX_HEIGHT-230, width=100,height=100,mask=None)
    d = UsernameBarcode(request.user.username)
    binaryStuff = d.asString('png')
    newFile = open("barcode.png", "wb")
    newFile.write(binaryStuff)
    newFile.close()
    imgbar = ImageReader("barcode.png")
    p.drawImage(imgbar, -180,MAX_HEIGHT-180, width=None,height=50,mask=None,preserveAspectRatio=True)
    p.line(25,MAX_HEIGHT-300, MAX_WIDTH-25,MAX_HEIGHT-300)
    p.line(25,MAX_HEIGHT-80, MAX_WIDTH-25,MAX_HEIGHT-80)

    ACCO_HEIGHT = MAX_HEIGHT-300

    p.drawCentredString(MAX_WIDTH/2, ACCO_HEIGHT-20, "Accommodation Slip")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response




