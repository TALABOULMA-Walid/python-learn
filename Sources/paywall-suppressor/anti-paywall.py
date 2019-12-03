from urllib import request
from bs4 import BeautifulSoup
from flask import Flask

# Or use navigator console F12:
# x = document.getElementsByClassName("content")
# for (var i = 0; i < x.length; i++){ x[i].style.filter = "";}  Removes Blur(5px)
# y = document.getElementsByClassName("piano-paywall")[0]
# y.parentNode.removeChild(y)                                   Removes Pay-wall sticker

PARISIAN_URL = "http://www.leparisien.fr/economie/" \
             "greve-du-5-decembre-nos-conseils-pour-se-deplacer-malgre-tout-02-12-2019-8207643.php"


app = Flask(__name__)


@app.route("/test")
def page_without_pay():
    u = request.urlopen(PARISIAN_URL)
    data = u.read()
    soup = BeautifulSoup(data, 'html.parser')
    soup.find('div', class_='piano-paywall').decompose()
    return str(soup.html)


if __name__ == "__main__":
    app.run(debug=True)
