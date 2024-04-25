from flask import Flask, render_template, flash, redirect, request, url_for, send_from_directory
from flask_mail import Mail, Message
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_SERVER'] = '#'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True  # Use SSL as it's recommended for secure connection
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')
mail = Mail(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/download_resume')
def download_resume():
    return send_from_directory('static', 'resume/resume.pdf', as_attachment=True)

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Send the email
    msg = Message(f"New contact request from {name}",
                  sender=email,
                  recipients=['akshay@codebyakshay.com'],
                  reply_to=email)
    msg.body = f"Message from {name} &  <{email}>  :  {message}"
    mail.send(msg)

    flash('Your message has been sent successfully!')
    return redirect(url_for('home'))  # Redirect to the 'home' endpoint


if __name__ == '__main__':
    app.run(debug=True)