from django.http import  HttpResponse
from django.template import loader
def index(requst):
    tp=loader.get_template("template/index.html")
    html=tp.render({"a":1})
    return html