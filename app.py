from flask import Flask, render_template, request
import bot

app = Flask(__name__)

def get_bot_response(message):
    if message.strip() == '':
        return "Please enter a message."
    else:
        return bot.bot_prompt(message)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        response = get_bot_response(message)
        return render_template('index.html', message=message, response=response)
    else:
        # Define a default response for GET requests
        response = "Welcome! How can I assist you today?"
        return render_template('index.html', response=response)

# Define routes for other pages
@app.route('/about')
def about():
    response = get_bot_response("About")
    return render_template('about.html', response=response)

@app.route('/dashboard')
def dashboard():
    response = get_bot_response("Dashboard")
    return render_template('dashboard.html', response=response)

@app.route('/services')
def services():
    response = get_bot_response("Services")
    return render_template('services.html', response=response)

@app.route('/doctors')
def doctors():
    response = get_bot_response("Doctors")
    return render_template('doctors.html', response=response)

@app.route('/appointment')
def appointment():
    response = get_bot_response("Appointment")
    return render_template('appointment.html', response=response)

@app.route('/contact')
def contact():
    response = get_bot_response("Contact")
    return render_template('contact.html', response=response)

@app.route('/login')
def login():
    response = get_bot_response("Login")
    return render_template('login.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
