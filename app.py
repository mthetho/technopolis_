from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Tutor Position in Mathematics',
    'location': 'Steve Biko Campus',
    'salary': 'R1500.00'
    
  },
  {
    'id': 2,
    'title': 'Tutor Position in Cornerstone',
    'locatiion': 'ML Sultan Campus',
    'salary': 'R1500.00'
  },
  {
    'id': 3,
    'title': 'Assistant Teacher',
    'location': 'Ritson Campus',
    'salary': 'R2000.00'
  }

]

@app.route("/")
def hello_jovian():
  return render_template('home.html',
                        jobs=JOBS, company_name = "Tutor++")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/login/")
def login_page():
  return render_template('login.html')

@app.route("/documents/")
def documents_page():
  return render_template('doc.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)