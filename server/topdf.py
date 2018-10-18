# coding: utf-8
import pdfkit

options = {
    'page-size': 'A4',  # A3 A4
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
    # 'redirect-delay': 1000
}

pdfkit.from_file('html/home.html', 'out.pdf', options=options)