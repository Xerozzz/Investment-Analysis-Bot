from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from datetime import date
today = date.today().strftime("%d%m%y")

def pdf(indicators, objects,dirname):
    doc = SimpleDocTemplate(f"{dirname}\\Daily_Stock_Report\\Reports\\report_{today}.pdf", pagesize=letter)

    # container for the 'Flowable' objects
    elements = []

    for i in objects.keys():
        stock = Paragraph(f"<b>{i}</b>")

        values = indicators.loc[i]
        stock_data = objects[i]

        data= [[stock],
               ['Signal', stock_data['signal'], '+PLACEHOLDER%'],
               ['Debt To Equity', stock_data["d/e"], values["debtToEquity"]],
               ['Beta', stock_data["beta"], values["beta"]],
               ['Return on Equity', stock_data["roe"], values["returnOnEquity"]],
               ['PEG Ratio', stock_data["peg"], values["pegRatio"]],
               ['Price To Book Ratio', stock_data['pb'], values["priceToBook"]],
               ]

        t=Table(data,3*[2*inch], 7*[0.4*inch])

        t.setStyle(TableStyle([
            ('SPAN', (0,0),(-1,0)),
            ('GRID', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN', (1,1), (-1,-1), 'CENTER'),
            ]))

        elements.append(t)

    # write the document to disk
    doc.build(elements)
