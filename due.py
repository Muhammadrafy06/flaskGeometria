from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("due_1.html")

@app.route('/areaRettangolo2', methods=['GET'])
def area_rettangolo():
    try:
        base = int(request.values.get("base"))
        altezza = int(request.values.get("altezza"))
        risultato = base * altezza
        return render_template("due_2.html", risultato= risultato)
    except:
        risultato = "errore"
        return render_template("due_2.html", risultato= risultato)





  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)