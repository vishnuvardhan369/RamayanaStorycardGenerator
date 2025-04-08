from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame, Image
from reportlab.lib.colors import lightblue, lightgreen, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_story_pdf(title, story, moral, image1_path, image2_path, output_path="story_card.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    c.setFillColor(lightblue)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    pdfmetrics.registerFont(TTFont('ArchitectsDaughter', 'fonts/ArchitectsDaughter-regular.ttf'))
    c.setFont('ArchitectsDaughter',16)
    c.setFillColor(black)
    c.drawCentredString(width / 2, height - 50, title)

    c.drawImage(image1_path, inch, height - 300, width=3*inch, height=3*inch, preserveAspectRatio=True)

    c.drawImage(image2_path, width - 4*inch, height - 300, width=3*inch, height=3*inch, preserveAspectRatio=True)

    styles = getSampleStyleSheet()
    story_style = ParagraphStyle(
        'story',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        textColor=black,
        spaceAfter=10,
    )
    story_para = Paragraph(story.replace("\n", "<br/>"), style=story_style)

    moral_style = ParagraphStyle(
        'moral',
        parent=styles['Normal'],
        fontSize=14,
        textColor="green",
        alignment=1,
        spaceBefore=10
    )
    moral_para = Paragraph(f"<b>Moral:</b> {moral}", style=moral_style)

    frame = Frame(inch, inch, width - 2*inch, height - 390)
    frame.addFromList([story_para, moral_para], c)

    c.save()
    print("✅ PDF saved as story_card.pdf")
