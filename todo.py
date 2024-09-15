from flask import render_template, Flask, Blueprint, jsonify, request, flash, redirect, url_for,abort

from db import get_db

import json

bp = Blueprint('todo',__name__,url_prefix="/")

@bp.route("/",methods=['GET'])
def index():


     
    db, c = get_db()
    c.execute("SELECT * FROM todos")
    todos = c.fetchall()
  

    return render_template('todo/index.html',todos=todos)

@bp.route("/add",methods=['POST','GET'])
def add_todo():


    if request.method == 'POST':
        todo = request.form.get('todo').strip()
        status = request.form.get('status').strip()

        errors = []

        if not todo:
            errors.append("Todo can't be empty")
        if not status:
            errors.append("Status can't be empty")
        
        if len(errors) == 0:
            db, c = get_db()
            c.execute("INSERT INTO todos (todo,status) VALUES (%s, %s)",(todo,status))
            
            db.commit()

            return redirect(url_for('todo.index'))

        else:
            for error in errors:
                flash(error)

    return render_template('todo/add_todo.html')



@bp.route('/todos',methods=['GET'])
def list_todos():

    db, c = get_db()
    c.execute("SELECT * FROM todos")
    todos = c.fetchall()


    return jsonify([dict(todo) for todo in todos])


@bp.route("/todos", methods=['POST'])
def add_todo_api():

    todos = [{"todo": request.json['todo']
             ,"status": request.json['status'] } ]

    todo_obj = [todo for todo in todos]
    
    errors = []

    if not todo_obj[0]['todo']:
        errors.append("Todo can't be empty")
    if not todo_obj[0]['status']:
        errors.append("Status can't be empty")

    if todo_obj:
        if len(errors) == 0:
            db, c = get_db()
            c.execute("INSERT INTO todos (todo,status) VALUES (%s,%s)", (todo_obj[0]['todo'],todo_obj[0]['status']))
            db.commit()

            return jsonify({"todos": todo_obj}), 201
    return jsonify({"Message": errors}), 400



def get_todo(id):

    db, c = get_db()
    c.execute(
        "SELECT * FROM todos WHERE id = %s",
        (id,)
    )
    
    todo = c.fetchone()

    if todo is None:
        abort(404, "Todo {0} does not exists ".format(id))
    return todo

@bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit_todo(id):

    todo = get_todo(id)
    if request.method == 'POST':
        
        todo = request.form.get('todo').strip()
        status = request.form.get('status').strip()

        errors = []

        if not todo:
            errors.append("Todo can't be empty")
            
        if not status:
            errors.append("Status can't be empty")
        
        if len(errors) == 0:
            
            db, c = get_db()
            c.execute("UPDATE todos SET todo = %s, status = %s WHERE id = %s", (todo,status,id))
            db.commit()
             
            return redirect(url_for('todo.index'))
        else:
        
            
            for error in errors:
                flash(error)


    return render_template('todo/edit_todo.html', todo=todo)

@bp.route("/delete/<int:id>", methods=['POST'])
def delete_todo(id):

    db, c = get_db() 
    c.execute("DELETE FROM todos WHERE id = %s", (id,))
    db.commit()

    return redirect(url_for('todo.index'))



@bp.route("/todos/<int:id>",methods=['PUT'])
def edit_todo_api(id):

    todo = get_todo(id)
    
    new_todo = request.json['todo']
    new_status = request.json['status']

    errors = []

    if not new_todo:
        errors.append("Todo can't be empty")
    if not new_status:
        errors.append("Status can't be empty")

    if todo:
        if len(errors) == 0:
            
            db, c = get_db()
            c.execute("UPDATE todos SET todo = %s, status = %s WHERE id = %s", (new_todo,new_status,id))
            db.commit()

            return jsonify({"Message": f"Todo sucessfully added"})
        return jsonify({"Error": errors})
    return jsonify({"Error": f"Todo with id {id} not found"}), 404


@bp.route("/deletejson/<int:id>",methods=['DELETE'])
def delete_todo_api(id):

    todo = get_todo(id)

    if todo:
        db, c = get_db() 
        c.execute("DELETE FROM todos WHERE id = %s", (id,))
        db.commit()

        return jsonify({"Message": "Todo deleted successfully"})
    return jsonify({"Error": f"Todo with id {id} not found"}), 404