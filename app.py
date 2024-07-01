from flask import Flask, render_template, request

from client import UserSearchClient
from config import config


app = Flask(__name__)
client = UserSearchClient(config.client_id)


@app.route('/')
def index():
    return render_template(
        "index.html.jinja",
    )


@app.route("/users", methods=["GET"])
def search_users():
    if request.method != "GET":
        return

    city = request.args.get("city")
    page = request.args.get('page', 0, int)
    if city is None:
        return 'город не указан'

    page_limit = 20

    users = client.search_by_place(
        place=city.lower(),
        limit=page_limit,
        offset=page*page_limit,
    )
    return render_template(
        "users.html.jinja",
        users=users,
        page=page
    )


def run():
    app.run()
