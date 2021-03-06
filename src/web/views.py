#
# The MIT License (MIT)
#
# Copyright (c) 2022 Wonoly
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from . import scrapers

def home(request):
    return render(request, 'web/home.html')

def search(request):

    query = request.GET.get('q', '')
    if query.strip() == "":
        return redirect("/")

    results = []
    options = dict(
        query=query,
        start=0
    )

    for scraper in scrapers.get_scrapers():
        instance = scraper(options)
        results.append(instance.search())

    return render(request, "web/search.html", dict(results=results[0], options=options))
