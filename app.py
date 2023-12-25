from flask import Flask, render_template, request, jsonify, flash, redirect,Request
import json
import requests

app = Flask(__name__)

app.secret_key = 'ladoski59@&D'

CONTACTS_FILE = 'contacts.json'

# Part 1: Add Contact - Display form and handle form submission
@app.route('/add_contact', methods=['GET', 'POST'])
  
def add_contact():
    if request.method == "POST":
        Name = request.form.get('name')
        Phone_number = request.form.get('phone_number')
        message = request.form.get('message')

        if Name and Phone_number:  # Check if both fields are not empty
            new_contact = {"Name": Name, "Phone_number": Phone_number}

            with open("contacts.json", "r") as file:
                contacts = json.load(file)

            contacts.append(new_contact)  # Add the new contact to the list

            with open("contacts.json", "w") as file:
                json.dump(contacts, file, indent=4)

            flash('Contact added successfully!', 'success')
        else:
            flash('Please provide both Name and Phone Number.', 'error')

    return render_template('add_contact.html')

# Part 2: Send SMS - Display form and handle form submission
@app.route('/send_sms', methods=['GET', 'POST'])
def send_sms():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

        # Your SMS Chef API integration code here (not implemented in this example)

        flash('SMS sent successfully!', 'success')

    return render_template('send_sms.html')


# Part 3: Delete Contact - Display form and handle form submission

@app.route('/delete_contact', methods=['GET', 'POST'])
def delete_contact():
    if request.method == 'POST':
        name = request.form.get('name')

        with open("contacts.json", 'r') as f:
            contacts = json.load(f)
            
            # updated_contacts.app(name)
            
            updated_contacts = [contact for contact in contacts if 'Name' in contact and contact['Name'] != name]
        updated_contacts=[]
        


        if len(updated_contacts) < len(contacts):
            with open("contacts.json", 'w') as f:
                json.dump(updated_contacts, f, indent=4)
            flash('Contact deleted successfully!', 'success')
        else:
            flash('Contact not found!', 'error')

    return render_template('delete_contact.html')


# Part 4: API endpoint to display all contacts
@app.route('/contacts')
def display_contacts():
    with open(CONTACTS_FILE, 'r') as f:
        contacts = json.load(f)

    return jsonify(contacts)

if __name__ == '__main__':
    app.run(port=5500,debug=True)
