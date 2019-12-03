# Ticket
# ----------------------
# Id : Int Primary Key
# Type of change : String
# Title : String
# Description : String
# Submitter Name : String
# Submitter email : String
# Submitter website : String
# File : File
# Date Created : Date
#
# CREATE TABLE Ticket (
#    id INT PRIMARY KEY,
#    change TEXT NOT NULL,
#    title TEXT NOT NULL,
#    description TEXT NULL,
#    submitter_name TEXT NOT NULL,
#    submitter_email TEXT NOT NULL,
#    submitter_website TEXT NULL,
#    file TEXT NULL,
#    date_created DATE NOT NULL,
#    );
#
# JAVASCRIPT to POST request and update page
# async function update_POST(){
# resp = await fetch('/ticket', {method: 'POST'});
# reader = resp.body.getReader();
# let { value: chunk, done: readerDone } = await reader.read();
# chunk = new TextDecoder('utf-8').decode(chunk);
# document.getElementsByTagName('body')[0].innerText = chunk; }

import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def list_tickets():
    """Display a list of tickets in the system."""
    db_connection = sqlite3.connect('ticket.db.sqlite3')
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM Tickets')
    tickets = cursor.fetchall()
    return render_template('index.html', tickets=tickets)


@app.route('/ticket', methods=['GET', 'POST'])
def add_ticket():
    """Add a new ticket via a form."""
    if request.method == 'GET':
        return render_template('edit.html')
    elif request.method == 'POST':
        print(request.__dict__)
        return 'add_ticket : process_form()'


@app.route('/ticket/id/<int:ticket_id>')
def view_ticket(ticket_id):
    """Display the details of the ticket with id *ticket_id*."""
    return 'view_ticket : id = {}'.format(ticket_id)


if __name__ == '__main__':
    app.run(debug=True)
