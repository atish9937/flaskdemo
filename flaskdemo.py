from flask import Flask, redirect, request

app = Flask(__name__)

from urllib.parse import urlparse, urlunparse

FROM_DOMAIN = "example.com"
TO_DOMAIN = "www.example.com"

@app.before_request
def redirect_to_new_domain():
    urlparts = urlparse(request.url)
    if urlparts.netloc == FROM_DOMAIN:
        urlparts_list = list(urlparts)
        urlparts_list[1] = TO_DOMAIN
        return redirect(urlunparse(urlparts_list), code=301)
