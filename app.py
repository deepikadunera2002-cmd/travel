from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Database create
def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/")
def home():
    return "Travel Guide Backend Running!"


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )

    conn.commit()
    conn.close()

    return "Message Saved Successfully!"


@app.route("/admin")
def admin():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()

    conn.close()

    html = """
    <html>
    <head>
        <title>Admin Panel</title>
    </head>
    <body>
        <h1>Travel Guide India - Admin Panel</h1>

        <table border="1" cellpadding="10">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Message</th>
            </tr>
    """

    for row in data:
        html += f"""
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
                <td>{row[3]}</td>
            </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)