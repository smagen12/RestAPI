from flask import Flask
from routes.books_routes import books_bp

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(books_bp)

@app.route('/ping')
def ping():
    return jsonify({'status': 'ok'}), 200
    
if __name__ == '__main__':
    app.run(debug=True)