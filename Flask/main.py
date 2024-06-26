from flask import Flask
import random

app = Flask(__name__)
facts_list = ['Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas', 'Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos', 'Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos', 
              'Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo', 'Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo',
              'El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna', 'Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.', 'La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos']

emojis = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '🥳', '🎄', '🎉', '🎊', '🥳', '🎈', '🎁', '🎀', '🎎', '🏆', '🏅', '🎯', '🎭', '🎨', '🎬', '🎤', '🎧', '🎼', '🎵', '🥁', '🎷', '🎸', '🎹', '🥂', '🍸', '🍹', '🍷', '🍴', '🍔', '🍟', '🍕', '🌭', '🥪', '🌮', '🌯', '🥙', '🍲', '🍛', '🍜', '🍝', '🍠', '🍢', '🍣', '🍤', '🍥', '🥮', '🍦', '🍧', '🍨', '🍩', '🍪', '🎂', '🍰', '🥧', '🍫', '🍬', '🍭', '🍮', '🍯', '🍼', '🥛', '☕', '🍵', '🍶', '🍺', '🍻', '🥂', '🍷', '🥃', '🍸', '🍹', '🍾', '🍿', '🎈', '🎉', '🎊', '🎋', '🎍', '🎎', '🎏', '🎐', '🎑', '🌁', '🌃', '🌄', '🌅', '🌆', '🌇', '🌈', '🌊']

@app.route("/")
def hello_web():
    x = '<h1 style="text-align: center;">Hola! aqui puedes ver datos aleatorios de la dependencia tecnologica (y más!)</h1>'
    y = '<div style="text-align: center;"><a href="/random_fact" style="font-size: 32px">¡Ver un dato aleatorio!</a><br>'
    z = '<a href="/random_number" style="font-size: 32px">¡Ver un número aleatorio!</a>'
    w = '<br><a href="/coin" style="font-size: 32px">¡Lanzar una moneda!</a>'
    u = '<br><a href="/random_password/10" style="font-size: 32px">��Generar una contraseña!</a></div>'
    return x + y + z + w + u

@app.route("/random_fact")
def random_fact():
    return f'<h1>{random.choice(facts_list)}</h1>'

@app.route("/random_number")
def random_number():
    return f'<h1>{random.randint(1,100)}</h1>'

@app.route("/coin")
def coin():
    return f'<h1>{random.choice(["Cara", "Cruz"])}</h1>'

@app.route("/random_emoji")
def random_emoji():
    return f'<h1>{random.choice(emojis)}</h1>'

@app.route("/random_password/<int:length>")
def random_password(length):
    return f'<h1>{"".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=length))}</h1>' + '<p>Puedes cambiar la longitud de la contraseña en el link de la pagina usando /random_password/(Tu numero), ejemplo: /random_password/20 </p>'

if __name__ == "__main__":
    app.run(debug=True)