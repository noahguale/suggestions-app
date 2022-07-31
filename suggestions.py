from models import Category, Suggestion, Comment
from settings import db, app

from flask import request, jsonify
from werkzeug.exceptions import HTTPException
from multiprocessing import Value
import json

@app.route('/api/categories/all')
def index():
    categories = Category.query.all()

    output = []
    for category in categories:
        output.append({'category':category.title})
    return {"categories":output}

@app.route('/api/categories/create',methods=['POST'])
def create_category():
    category = Category(title=request.json['title'])
    db.session.add(category)
    db.session.commit()
    return {'id':category.id}

@app.route('/api/categories/<category_id>/delete',methods=['DELETE'])
def delete_category(category_id):    
    category = Category.query.filter_by(id=category_id).first_or_404()
    db.session.delete(category)
    db.session.commit()
    return f'Deleted Category - {category.title}'

@app.route('/api/categories/<id>')
def get_category(id):
    category = Category.query.get_or_404(id)
    suggestions = category.suggestions

    output = []
    for suggestion in suggestions:
        output.append({suggestion.author:suggestion.body})
    return {'categeory':category.title,'suggestions':output}

@app.route('/api/suggestions/all')
def get_suggestions():
    suggestions = Suggestion.query.all()
    
    output = []
    for suggestion in suggestions:
        output.append({suggestion.author:suggestion.body})
    return {"suggestions":output}

@app.route('/api/suggestions/<id>')
def get_suggestion(id):
    suggestion = Suggestion.query.get_or_404(id)

    output = []
    for comment in suggestion.comments:
        output.append({'comment':comment.body})

    if suggestion:
        return {"author":suggestion.author,"body":suggestion.body,"upvotes":suggestion.upvotes,"downvotes":suggestion.downvotes,"comments":output}
    else:
        return 'Sorry this suggestion does not exist or was deleted'

@app.route('/api/suggestions/create',methods=['POST'])
def create_suggestion():    
    suggestion = Suggestion(body=request.json['body'],author=request.json['author'],upvotes=request.json['upvote'],downvotes=request.json['downvote'],category_id=request.json['category_id'])
    db.session.add(suggestion)
    db.session.commit()
    return {'id':suggestion.id}

@app.route('/api/suggestions/<suggestion_id>/edit/',methods=['PUT'])
def edit_suggestion(id):    
    suggestion = Suggestion.query.get_or_404(id)
    suggestion.body = request.json['body']
    db.session.commit()
    return {'id':suggestion.id}

@app.route('/api/suggestions/<suggestion_id>/delete',methods=['DELETE'])
def delete_suggestion(suggestion_id):    
    suggestion = Suggestion.query.filter_by(id=suggestion_id).first_or_404()
    db.session.delete(suggestion)
    db.session.commit()
    return f'Deleted Suggestion #{suggestion.id} and {len(suggestion.comments)} comments'

@app.route('/api/suggestions/<suggestion_id>/vote',methods=['PUT'])
def vote_suggestion(suggestion_id):    
    suggestion = Suggestion.query.filter_by(id=suggestion_id).first_or_404()
    if request.json['vote'] == 'up':
        suggestion.upvotes += 1
    elif request.json['vote'] == 'down':
        suggestion.downvotes += 1
    db.session.commit()
    # return jsonify(f'Suggestion #{suggestion.id}:  {len(suggestion.comments)} comments')
    return {"votes":{"upvotes":suggestion.upvotes,"downvotes":suggestion.downvotes}}

@app.route('/api/comments/all')
def get_comments():
    comments = Comment.query.all()
    
    output = []
    for comment in comments:
        output.append({'comment':comment.body})
    return {"suggestions":output}

@app.route('/api/comments/create',methods=['POST'])
def create_comment():    
    comment = Comment(body=request.json['body'],suggestion_id=request.json['suggestion_id'])
    db.session.add(comment)
    db.session.commit()
    return {'id':comment.id}

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response