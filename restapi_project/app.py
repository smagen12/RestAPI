from flask import Flask
from routes.books_routes import books_bp

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(books_bp)

@app.route('/ping')
def ping():
    status = {'status': 'ok'}
    # Forgot to return -- intentional bug!

# Intentional bug: forgot to protect main
if __name__ == '__main__':
    app.run(debug=True)