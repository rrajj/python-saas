import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
curr_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    """
    use template engine.
    `mkdir templates`
    added the path in `settings.py` so django knows where to find the file
    """
    qs = PageVisit.objects.all()  # query_set
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0

    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        # "query_set": query_set,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent": percent,
    }
    html_template = "home.html"     #   file moved to templates
    # PageVisit.objects.create()
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)

def old_home_page_view(request, *args, **kwargs):
    # html_file_path = curr_dir / "home.html"
    # html_ = html_file_path.read_text()

    # html_ = """
    #         <!DOCTYPE html>
    #         <html lang="en">
    #         <head>
    #             <meta charset="UTF-8">
    #             <title>Title</title>
    #         </head>
    #         <body>
    #             <h1>sample line 2</h1>
    #         </body>
    #         </html>
    #         """

    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
                <h1>Title is: {page_title}</h1>
            </body>
            </html>
            """.format(**my_context)

    return HttpResponse(html_)

    # return HttpResponse("hello world")    # error
    # return HttpResponse("<h1>Hello World!</h1>")