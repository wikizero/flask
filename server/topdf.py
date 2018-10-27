# coding: utf-8
import pdfkit
import weasyprint
import ssl
from faker import Faker

# ssl._create_default_https_context = ssl._create_unverified_context
options = {
    'page-size': 'Letter',  # A3 A4  Letter
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
    # 'animation': False
    # 'redirect-delay': 1000
    'custom-header': [
        ('User-Agent', Faker().firefox())
    ]
}

# url = 'https://www.yiibai.com/pandas/python_pandas_panel.html'
url = 'https://segmentfault.com/a/1190000003962806'
# pdfkit.from_file('html/home.html', 'out.pdf', options=options)
pdfkit.from_url(url, 'out.pdf', options=options)

# weasyprint.HTML(url=url).write_pdf('out1.pdf')
# print(type(pdf))
# open('out.pdf', 'w').write(str(pdf))
