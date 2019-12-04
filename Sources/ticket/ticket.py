import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from pprint import pprint

app = Flask(__name__)
INSERT_STATEMENT = """INSERT INTO Tickets('change','title','description',
                    'submitter_name','submitter_email','submitter_website','file')
                     VALUES ("{change}","{title}","{description}",
                     "{submitter_name}","{submitter_email}","{submitter_website}","{file}");"""


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
    else:
        db_connection = sqlite3.connect('ticket.db.sqlite3')
        cursor = db_connection.cursor()
        pprint(request.form)
        cursor.execute(INSERT_STATEMENT.format(**request.form))
        db_connection.commit()
        return redirect(url_for('list_tickets'))


@app.route('/ticket/id/<int:ticket_id>')
def view_ticket(ticket_id):
    """Display the details of the ticket with id *ticket_id*."""
    db_connection = sqlite3.connect('ticket.db.sqlite3')
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM Tickets WHERE id={}'.format(ticket_id))
    ticket = cursor.fetchone()
    return render_template('detail.html', ticket=ticket)


if __name__ == '__main__':
    app.run(debug=True)
