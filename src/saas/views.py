import pathlib
from django.http import HttpResponse
from django.shortcuts import render

curr_dir = pathlib.Path(__file__).resolve().parent

def home_page_view_using_template(request, *args, **kwargs):
    """
    use template engine.
    `mkdir templates`
    added the path in `settings.py` so django knows where to find the file
    """
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_template = "home.html"     #   file moved to templates
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