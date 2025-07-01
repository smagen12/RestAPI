# Books REST API

A simple Flask REST API to manage books.

## Endpoints

- `GET /books` - Get all books
- `GET /books/<id>` - Get a book by ID
- `POST /books` - Add new book
- `PUT /books/<id>` - Update a book
- `DELETE /books/<id>` - Delete a book
- `GET /bokks/count` - Buggy count endpoint
- `GET /ping` - Should return OK, but has bug

## Run

```bash
pip install -r requirements.txt
python app.py
```