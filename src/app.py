from flask import Flask, render_template,request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from config import config

from models.ModelUser import ModelUser, ModelRegistro, ModelEditar
from models.ModelMensaje import ModelMensaje
from models.entities.User import User
from models.entities.Registro import Registro

app=Flask(__name__, template_folder='templates')

db=MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        correo = request.form.get('correo') 
        password = request.form.get('password')
        if correo and password:
            logged_user = ModelUser().login(db, correo, password)
            if logged_user is not None:
                session['usuario_id'] = logged_user.id
                return redirect(url_for('base'))
            else:
                flash('Correo o contraseña incorrectos', 'error')
                return render_template('auth/login.html')
        else:
            flash('Por favor, ingrese correo y contraseña', 'error')
    return render_template('auth/login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method=='POST':     
        correo = request.form['correo']
        password = request.form['password']
        user = request.form['user']    
        apellido = request.form['apellido']
        celular = request.form['celular']
        user_existente = ModelUser().get_user_by_email(db, correo)
        if user_existente:
            flash('El correo ya está registrado', 'error')
            return redirect(url_for('registro'))
        else:
            new_user = Registro(id = 1, correo = correo, password = password, user = user, apellido = apellido, celular = celular)
            ModelRegistro().create_registro(db, new_user)
            flash('Se registró con exito', 'success')
            return redirect(url_for('login'))
    return render_template('auth/registro.html')

@app.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    if request.method == 'POST':
        remitente_id = request.form['remitente_id']
        destinatario_id = request.form['destinatario_id']
        mensaje = request.form['mensaje']
        ModelMensaje().enviar_mensaje(db, remitente_id, destinatario_id, mensaje)
        flash('Enviado', 'success')
        return redirect(url_for('base'))
    
@app.route('/mensajes')
def pagina_mensajes():
    usuario_id = session.get('usuario_id')
    mensajes = ModelMensaje().obtener_mensaje(db, usuario_id)
    return render_template('mensajes', mensajes = mensajes, usuario_id = usuario_id)

@app.route('/base')
def base():
    usuario_id = session.get('usuario_id')
    usuarios = ModelMensaje().usuario_db(db)
    if usuarios:
        return render_template('base.html', usuarios = usuarios, remitente_id = usuario_id)
    else:
        print('Usuario no encontrado', 'error')
        return redirect(url_for('login'))

@app.route('/edit_user', methods=['POST'])
def edit_user():
    usuario_id = session.get('usuario_id')
    if usuario_id:
        correo = request.form['correo']
        user = request.form['user']
        apellido = request.form['apellido']
        celular = request.form['celular']
        try:
            editar = ModelEditar().actualizar(db, usuario_id, correo, user, apellido, celular)
            if editar:
                flash('Datos del usuario actualizados correctamente', 'success')
            else:
                flash('Error al actualizar los datos del usuario', 'error')
        except Exception as ex:
            flash(str(ex), 'error')
    else:
        flash('Usuario no autenticado', 'error')
    
    return redirect(url_for('base'))
    
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()