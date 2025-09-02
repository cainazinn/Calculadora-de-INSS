#Olá! Hoje iremos fazer o cálculo do desconto do INSS 2025.

#O cidadão informa para o programa quanto recebe de salário e como ele exerce sua atividade profissional.

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "SENHA"

# print("-----------------------------------------------------")
# print("| Seja bem vindo(a) ao simulador de cálculo de INSS |")
# print("| Aqui você saberá quanto terá que pagar de INSS    |")
# print("| de acordo com sua vinculação profissional!        | ")
# print("|                                                   |")
# print("-----------------------------------------------------\n")

# salário = float(input("Informe seu salário:"))
# vinculação = input("Informe como você exerce sua atividade profissional:")

def calc_inss(salário, vinculação):
    if vinculação == "clt": #Se o cidadão trabalhar de carteira assinada, seu desconto INSS será calculado da seguinte forma:
        if salário <= 1518.00:
            inss = salário * 0.075
        elif salário > 1518.00 and salário <= 2793.88:
            inss = salário * 0.09 - 22.77
        elif salário > 2793.88 and salário <= 4190.83:
            inss = salário * 0.12 - 106.59  
        elif salário > 4190.83 and salário <= 8157.41:
            inss = salário * 0.14 - 190.40
        elif salário > 8157.41:  
            inss = salário * 0.14 - 190.40 #Mesmo que o salário do cidadão passe de R$8.157,41, seu desconto INSS já atingiu o limite.
        
    elif vinculação == "autônomo": #Se o cidadão for autônomo, seu desconto INSS será calculado da seguinte forma: 
        if salário <= 8157.41:
            inss = salário * 0.20
        else:
            inss = salário * 0.14 #Mesmo que o salário do cidadão passe de R$8.157,41, seu desconto INSS já atingiu o limite.
        
    elif vinculação == "empresário": #Se o cidadão for empresário, seu desconto INSS será calculado da seguinte forma:
        if salário <= 8157.41:
            inss = salário * 0.11
        else:
            inss = salário * 0.14 #Mesmo que o salário do cidadão passe de R$8.157,41, seu desconto INSS já atingiu o limite.

    return round(inss, 2)

# resultado = calc_inss(salário)
# print(f"Você pagará R${resultado} de INSS!")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    salário = float(data['salario'])
    vinculação = data['vinculacao'].lower()
    resultado = calc_inss(salário, vinculação)

    if resultado is not None:
        return jsonify({"inss": resultado})
    else:
        return jsonify({"error": "Tipo de vinculação inválido!"}), 400
    
if __name__ == "__main__":
    app.run(debug=True)
