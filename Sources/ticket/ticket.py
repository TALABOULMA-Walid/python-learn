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

import sqlite3
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def list_tickets():
    """Display a list of tickets in the system."""
    return 'list_tickets'


@app.route('/ticket', methods=['GET', 'POST'])
def add_ticket():
    """Add a new ticket via a form."""
    return 'add_ticket'


@app.route('/ticket/id/<int:ticket_id>')
def view_ticket(ticket_id):
    """Display the details of the ticket with id *ticket_id*."""
    return 'view_ticket : id = {}'.format(ticket_id)


if __name__ == '__main__':
    app.run(debug=True)
