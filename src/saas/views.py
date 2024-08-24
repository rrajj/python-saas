import pathlib
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent
print(this_dir)

def home_page_view(request, *args, **kwargs):
    html_file_path
    html_ = this
    return HttpResponse("<h1>Hello World!</h1>")
