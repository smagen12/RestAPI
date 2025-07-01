from flask import Blueprint, jsonify, request
from models.book_model import books

books_bp = Blueprint('books_bp', __name__)

@books_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@books_bp.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or not 'title' in data or not 'author' in data:
        return jsonify({'message': 'Invalid data'}), 400

    new_id = books[-1]['id'] + 1 if books else 1
    new_book = {
        'id': new_id,
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book['id'] == book_id:
            book['title'] = data.get('title', book['title'])
            book['author'] = data.get('author', book['author'])
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book not found'}), 404

# Intentional typo
@books_bp.route('/bokks/count', methods=['GET'])
def count_books():
    return jsonify({'count': len(books)})