from flask import Flask
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def parse_links_file(filename):
    result = []  # Dictionary mapping from address name to details
    with open(filename, 'r', encoding='utf8') as f:
        data = f.read()
        lines = data.splitlines()
        for line in lines:
            fields = line.split('@')
            result.append(fields)

    return result


def toHTMLFormat(element):
    str1 = "<a href=\"".strip() + element[1].strip() + "\" target='_blank'>"
    str1 += element[0]
    str1 += "</a><br>"
    return str1


@app.route("/request-first")
def first():
    result =""
    result += toHTMLFormat(links_list[0])
    return result


@app.route("/request-random")
def request():
    random_list = random.sample(links_list[1:], 1)
    result = ""
    for element in random_list:
        result += toHTMLFormat(element)
    return result


if __name__ == "__main__":
    links_list = parse_links_file("links&q.txt")
    length = len(links_list)
    app.run(debug=True)
