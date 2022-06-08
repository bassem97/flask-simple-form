import asyncio
import json
import logging
from concurrent.futures import ThreadPoolExecutor

import requests as requests
from flask import render_template, request, redirect
from app import app, db
from app.models import Site

jedi = "of the jedi"


@app.route('/')
@app.route('/index')
def index():
    # entries = [
    #     {
    #         'id' : 1,
    #         'title': 'test title 1',
    #         'url' : 'test desc 1',
    #         'status' : True
    #     },
    #     {
    #         'id': 2,
    #         'title': 'test title 2',
    #         'url': 'test desc 2',
    #         'status': False
    #     }
    # ]
    entries = Site.query.all()
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        url = form.get('url')
        if not title or url:
            entry = Site(title=title, url=url)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"


@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Site.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return "of the jedi"


@app.route('/update', methods=['POST'])
def update():
    if not id or id != 0:
        entry = Site.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"


@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Site.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"


def scrape_url():
    uri = "http://127.0.0.1:9000/crawl"
    response = requests.request("GET",uri)
    return response.text


def get_results():
    uri = "http://127.0.0.1:9000/results"
    response = requests.get(uri)
    return response.json()




# @app.route('/turn/<int:id>')
@app.route('/scrape/')
def turn():
    response = scrape_url()
    while response != "SCRAPE COMPLETE":
        response = scrape_url()
    data = get_results()
    with open('json/immoland.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return redirect('/')
    # if response == "SCRAPE COMPLETE":
    #     return get_results()
    #     return
    # return ('', 204)
    # if Jresponse == "SCRAPE COMPLETE":
    #     return "C bn"

    # data = json.loads(Jresponse)
    #
    # displayName = data['link'][0]['display_name']  # <-- The display name
    # reputation = data['title'][0]['reputation']  # <-- The reputation
    #

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"
