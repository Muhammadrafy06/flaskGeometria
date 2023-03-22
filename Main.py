from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("uno_1.html")

@app.route('/areaRettangolo', methods=['POST'])
def area_rettangolo():
    base = int(request.values.get("base"))
    altezza = int(request.values.get("altezza"))
    totale = base * altezza
    return render_template("uno_2.html", totale= totale)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)