from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru,India',
    'Salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi,India',
    'Salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Ahmedabad,India',
    'Salary': 'Rs. 12,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'Salary': 'Rs. 10,00,000'
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
