import yfinance as yf
import pandas as pd
from carteira import *
from papel import *

def get_b3(carteira, periodo, codigos):
    empresas = yf.download(codigos, period=periodo, auto_adjust=True)
    if  len(codigos) == 1:
        preco_papel = empresas["Close"][0]
        data = empresas.index[0].to_pydatetime()
        papel = Papel(codigos, preco_papel , data)
        carteira.add_ativo(papel)
        tamanho_periodo = len(empresas["Close"])
        for index in range(1, tamanho_periodo):
            valor = empresas["Close"][index]
            data = empresas.index[index].to_pydatetime()
            papel.update_valor(valor, data)
            carteira.update_carteira(valor, data)
    else:
        for codigo in codigos:
            preco_papel = empresas["Close"][codigo][0]
            data = empresas.index[0].to_pydatetime()
            papel = Papel(codigo, preco_papel , data)
            carteira.add_ativo(papel)
            tamanho_periodo = len(empresas["Close"][codigo])
            for index in range(1, tamanho_periodo):
                valor = empresas["Close"][codigo][index]
                data = empresas.index[index].to_pydatetime()
                papel.update_valor(valor, data)
                carteira.update_carteira(valor, data)

    for ativo in carteira.ativos:
        df1 = pd.DataFrame(ativo.get_historico_formatado())
        print("\n","O PAPEL",ativo.codigo," TEVE UM A RENTABILIDADE ACUMULADA DE :", ativo.rentabilidade_periodo)
        print(df1.set_index("data"))

    df2 = pd.DataFrame(carteira.get_historico_formatado())

    print("\n"," SUA CARTEIRA TEVE UMA  rentabilidade acumulada no período: ".upper(), carteira.rentabilidade_periodo)
    print(df2.set_index("data"))

def main():
  carteira = Carteira()
  numero_papeis = int(input("Digite a Quantidade de Ativos para carteira: "))
  periodo = {1:"1d", 2:"5d", 3:"1mo", 4: "1y"}
  escolha = int(input("Escolha o período:\n1 - um dia   2 - uma semana  3 - um mês 4 - um ano: "))
  lista_papeis = []
  for papel in range(numero_papeis):
    ativo = input("Digite o código do ativo: ")
    ativo += ".sa"
    lista_papeis.append(ativo.upper())

  get_b3(carteira, periodo[escolha],lista_papeis)

if __name__ == "__main__":
    main()