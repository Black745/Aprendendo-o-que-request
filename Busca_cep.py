#criando uma request básica 

import requests
import json
try:
    a=str(input("informe o seu cep:"))
    Busca_cep=requests.get("https://cep.awesomeapi.com.br/json/"+a)#no lugar da variável:a será inserido o CEP que o usuário digitar
    CEP=Busca_cep.json()#trará os dados e  o python interpretar na sua propria linguagem
    print("="*20)
    print("informações do cep")
    print("Cep:",CEP["cep"],"\nDDD:",CEP["ddd"],"\nEstado:",CEP["state"], "\nCidade:",CEP["city"],"\nDistrito/bairro:",CEP["district"],"\nRua:",CEP["address"])
except:
        print("erro,CEP INVÁLIDO! ")
