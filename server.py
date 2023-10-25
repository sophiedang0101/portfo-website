from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
app.config['DEBUG'] = True  # This line explicitly sets debug mode


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/favicon.ico')
def favicon():
    return '', 204


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except IOError as e:
            print(f"Error writing to database: {e}")
    else:
        return 'Something went wrong. Try again!'


# Add a route for the form page where you can render the form
@app.route('/form', methods=['GET'])
def show_form():
    return render_template('index.html')
