from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/logado', methods = ['POST'])
def logado():
    name = request.form.get("email")
    return render_template('logado.html', nome= name)

@app.route('/')
def register():
    return render_template('register.html')
    # # Lógica de validação de login aqui...
    # email = request.form['email']
    # password = request.form['password']
    
    # # Verifique as credenciais (substitua esta parte pela sua lógica de validação)
    # if email == 'user@example.com' and password == 'password':
    #     # Se as credenciais estiverem corretas, redirecione para index.html
    #     return redirect(url_for('static', filename='index.html'))
    # else:
    #     # Se as credenciais estiverem incorretas, redirecione de volta para a página de login
    #     return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
