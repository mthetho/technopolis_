from flask import Flask, render_template, jsonify, request, redirect
import replit
import os

app = Flask(__name__)

message = "Welcome to tutor++, presented to you by Technopolis"  
endpoint = os.environ.get('d503HtSDCDTzLguopDXt')  

if endpoint:
    command = f"curl https://notify.run/{endpoint} -d '{message}'"
    os.system(command)
else:
    print("Endpoint not found. Please set the NOTIFY_ENDPOINT environment variable.")

replit.db["jobs"] = [
  {
    'id': 1,
    'title': 'Tutor Position in Mathematics',
    'location': 'Steve Biko Campus',
    'salary': 'R1500.00'
    
  },
  {
    'id': 2,
    'title': 'Tutor Position in Cornerstone',
    'location': 'ML Sultan Campus',
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
def home():
    jobs = replit.db["jobs"]
    return render_template('home.html', jobs=jobs, company_name="Tutor++")

@app.route("/api/jobs")
def list_jobs():
    jobs = replit.db["jobs"]
    return jsonify(jobs)

@app.route("/admin/edit_job", methods=["GET", "POST"])
def edit_job():
    jobs = replit.db["jobs"]
    if request.method == "POST":
        # Update existing job
        job_id = int(request.form["id"])
        for job in jobs:
            if job["id"] == job_id:
                job["title"] = request.form["title"]
                job["location"] = request.form["location"]
                job["salary"] = request.form["salary"]
                break
        # Add new job
        else:
            job = {
                "id": len(jobs) + 1,
                "title": request.form["title"],
                "location": request.form["location"],
                "salary": request.form["salary"]
            }
            jobs.append(job)
        # Save changes to database
        replit.db["jobs"] = jobs
        return redirect("/")
    else:
        job_id = int(request.args.get("id", "0"))
        if job_id == 0:
            # Render form to add new job
            return render_template("edit_job.html", job=None)
        else:
            # Render form to edit existing job
            for job in jobs:
                if job["id"] == job_id:
                    return render_template("edit_job.html", job=job)
            # Job not found
            return redirect("/")
  
@app.route("/home/")
def home_page():
  return render_template('home.html')
  
@app.route("/login/")
def login_page():
  return render_template('login.html')

@app.route("/dashboard/")
def dashboad_page():
  return render_template('dashboard.html')

@app.route("/admin/")
def admin_page():
  return render_template('admin.html')

@app.route("/documents/")
def documents_page():
  return render_template('doc.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
