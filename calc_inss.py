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

    #verificado.
    

    if vinculação == "clt": #Se o cidadão trabalhar de carteira assinada, seu desconto INSS será calculado da seguinte forma:

        if salário <= 1518.00:
            aliquota = 7.5
            inss = salário * 0.075

        elif salário > 1518.00 and salário <= 2793.88:
            aliquota = 9
            inss = salário * 0.09 - 22.77

        elif salário > 2793.88 and salário <= 4190.83:
            aliquota = 12
            inss = salário * 0.12 - 106.59

        elif salário > 4190.83 and salário <= 8157.41:
            aliquota = 14
            inss = salário * 0.14 - 190.40
    
        elif salário > 8157.41:
            aliquota = 11.66  
            inss = 951.62 #Mesmo que o salário do cidadão seja maior que R$8.157,41, o teto de contribuição INSS já foi atingido.
        

#Contribuinte individual:

    elif vinculação == "autônomo plano comum": #Se o cidadão for autônomo, seu desconto INSS será calculado da seguinte forma: 

        if salário <= 8157.41:
            aliquota = 20
            inss = salário * 0.20

        else:
            aliquota = 20 
            inss = 1631.48 #Mesmo que o salário do cidadão seja maior que R$8.157,41, o teto de contribuição INSS já foi atingido.
    

    elif vinculação == "autônomo plano simplificado":

        if salário <= 1518.00:
            aliquota = 11
            inss = salário * 0.11

        else:
            aliquota = 11
            inss = 166.98

    elif vinculação == "autônomo cooperado": #verificar
        
        if salário <= 8157.41:
            aliquota = 20
            inss = salário * 0.20

        else:
            aliquota = 20
            inss = 1631.48

    elif vinculação == "autônomo prestador de serviços":
        
        aliquota = 11
        salário = 1518.00
        inss = salário * 0.11

    elif vinculação == "empresário": #Se o cidadão for empresário, seu desconto INSS será calculado da seguinte forma:

        if salário <= 14831.64:
            aliquota = 11
            inss = salário * 0.11

        elif salário > 14831.64:
            aliquota = 11
            inss = 1631.48

            # if inss > 1631.48:
            #     inss = 1631.48 #Mesmo que o salário do cidadão seja maior que R$8.157,41, o teto de contribuição INSS já foi atingido.

            # else:
            #     inss = salário * 0.11 
                
    return round(inss, 2), aliquota

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
    resultado, aliquota = calc_inss(salário, vinculação)


    if resultado is not None:
        return jsonify({"inss": resultado, "aliquota": aliquota})
    else:
        return jsonify({"error": "Tipo de vinculação inválido!"}), 400
    
if __name__ == "__main__":
    app.run(debug=True)
    
