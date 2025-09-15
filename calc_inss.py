#Olá! Hoje iremos fazer o cálculo do desconto do INSS 2025.

#O cidadão informa para o programa quanto recebe de salário e como ele exerce sua atividade profissional.

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "SENHA"

# ("-----------------------------------------------------")
# ("| Seja bem vindo(a) ao simulador de cálculo de INSS |")
# ("| Aqui você saberá quanto terá que pagar de INSS    |")
# ("| de acordo com sua vinculação profissional!        | ")
# ("|                                                   |")
# ("-----------------------------------------------------\n")

# salário = float(input("Informe seu salário:"))
# vinculação = input("Informe como você exerce sua atividade profissional:")

def calc_inss(salário, tipo_segurado, modalidade):

    #verificado.
    

    if tipo_segurado in ["empregado", "empregado doméstico", "trabalhador avulso"]:

        if salário == 1518.00:
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
            inss = 951.62 
        

#Contribuinte individual:

    
    elif tipo_segurado in ["contribuinte individual", "segurado facultativo"]:  
         
        if modalidade == "plano simplificado":
                
            salário = 1518.00
            aliquota = 11
            inss = salário * 0.11

        elif modalidade == "plano normal":

            if salário >= 1518.00 and salário <= 8157.41:
                aliquota = 20
                inss = salário * 0.20

            elif salário > 8157.41:
                aliquota = 20
                inss = 8157.41 * 0.20
            
            else:
                aliquota = 20
                inss = 1518.00 * 0.20
        
        elif modalidade == "baixa renda":

            if salário > 1518.00:
                aliquota = 5
                inss = 1518.00 * 0.05
            
            else:
                aliquota = 5
                inss = 1518.00 * 0.05


    elif tipo_segurado == "mei":

        if modalidade == "obrigatória":

            salário = 1518.00
            aliquota = 5
            inss = salário * 0.05
    
        elif modalidade == "complementar":

            salário = 1518.00
            aliquota = 15
            inss = salário * 0.15


    elif tipo_segurado == "empresário": 

        if salário >= 1518.00 and salário <= 8157.41:
            aliquota = 20
            inss = salário * 0.20

        elif salário > 8157.41:
            aliquota = 20
            inss = 8157.41 * 0.20
        
        else:
            aliquota = 20
            inss = 1518.00 * 0.20


    elif tipo_segurado == "segurado especial":

        if modalidade == "facultativo":

            if salário >= 1518.00 and salário <= 8157.41:
                aliquota = 20
                inss = salário * 0.20
        
            elif salário > 8157.41:
                aliquota = 20
                inss = 8157.41 * 0.20
            
            else:
                aliquota = 20
                inss = 1518.00 * 0.20
        
        elif modalidade == "obrigatório":
            
            if salário >= 1518.00:
                aliquota = 1.3
                inss = salário * 0.013

            else:
                aliquota = 1.3
                inss = 1518.00 * 0.013

            
                
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
    tipo_segurado = data['segurado'].lower()
    modalidade = data['modalidade'].lower()
    
    resultado, aliquota = calc_inss(salário, tipo_segurado, modalidade)


    if resultado is not None:
        return jsonify({"inss": resultado, "aliquota": aliquota})
    else:
        return jsonify({"error": "Tipo de segurado inválido!"}), 400
    
if __name__ == "__main__":
    app.run(debug=True)
    
