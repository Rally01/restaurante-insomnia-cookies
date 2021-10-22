from flask import Flask, render_template, redirect, session, url_for
from flask.globals import request
from db import get_db
from werkzeug.security import check_password_hash, generate_password_hash
import functools

app = Flask(__name__)
app.secret_key = 'misiontic2022'


@app.route('/') #Ruta de inicio, pagina principal donde inicia la web
def inicio():
    return render_template('inicio.html')


def login_required(view):
    @functools.wraps(view)
    def wraped_view(**kwargs):
        if 'nombre' not in session:
            return redirect('/')
        return view(**kwargs)
    
    return wraped_view


@app.route('/ingreso/', methods = ('GET', 'POST')) #Validacion desde el formulario de ingreso
def ingreso():
    if( request.method == 'POST'):
        
        correo = request.form['correoingreso']
        contraseña = request.form['passwordingreso']

        dataBase = get_db()

        #select * from Usuarios where correo = 'facorrales@uninorte.edu.co' and contraseña = '12345'
        ingreso = dataBase.execute('select * from Usuarios where USU_CORREO = ?', (correo,)).fetchone()
        dataBase.commit()

        if ingreso is not None:
            #print(ingreso[4]) #Imprimir contraseña
           
            contraseña = contraseña + correo
            sw = check_password_hash(ingreso[4], contraseña)

            if(sw):
                print('Usuario Correcto')
                session['nombre'] = ingreso[1]
                session['correo'] = ingreso[3]
                return redirect('/menu/')
            else:
                print('Usuario no registrado')
        
    return render_template('inicio.html')


@app.route('/registro/', methods = ('GET', 'POST')) #Validacion desde el formulario de registro
def registro():
    if( request.method == 'POST'):
        
        nombres = request.form['nombreregistro']
        apellidos = request.form['apellidoregistro']
        correo = request.form['correoregistro']
        contraseña = request.form['passwordregistro']
        valcontraseña = request.form['confirmpasswordregistro']

        if contraseña == valcontraseña:

            dataBase = get_db()

            valregistro = dataBase.execute('select * from Usuarios where USU_CORREO = ?', (correo,)).fetchone()
            print(correo)
            #dataBase.commit()
            
            if valregistro is not None:
                print('Usuario registrado anteriormente')
                return render_template('inicio.html')
            
            else:
                #Agregar SALT
                contraseña = contraseña + correo
                contraseña = generate_password_hash(contraseña)
                print('Usuario nuevo')
                #insert into Usuarios (id, nombres, apellidos, correo, contraseña) values('2', 'Mariana', 'Corrales', 'mariana@hotmail.com', '12345');
                dataBase.execute('insert into Usuarios (USU_NOMBRE, USU_APELLIDO, USU_CORREO, USU_CLAVE) values(?, ?, ?, ?);', (nombres, apellidos, correo, contraseña))
                #print(nombres, apellidos, correo, contraseña)
                #dataBase.commit()

                valregistro = dataBase.execute('select * from Usuarios where USU_CORREO = ?', (correo,)).fetchone()
                dataBase.commit()
                if valregistro is not None:
                    print('Usuario registrado correctamente')
                    session['nombre'] = valregistro[1]
                    return redirect('/menu/')

        else:
            print('Las contraseñas no coinciden')
            return render_template('inicio.html')

    #return render_template('inicio.html')


@app.route('/menu/') #Ruta a la pagina del menu
@login_required
def menu():
    return render_template('menu.html')


@app.route('/perfil/') #Ruta a la pagina de perfil de usuario
@login_required
def perfil():
    correo = session['correo']
    print(correo)
    
    dataBase = get_db()
    perfil = dataBase.execute('select * from Usuarios where USU_CORREO = ?', (correo,)).fetchone()

    if perfil is not None:
        print('Perfil Cargado Correctamente')
        print(perfil[1],perfil[2],perfil[3])
        session['Usu_Nombre'] = perfil[1]
        session['Usu_Apellido'] = perfil[2]
        session['Usu_Correo'] = perfil[3]
        return render_template('perfil.html')

    return render_template('perfil.html')

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')


if __name__ == '__main__':
 app.run()