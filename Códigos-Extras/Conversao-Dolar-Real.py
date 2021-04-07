valor_em_dolar = float(input("Qual valor em dolar que você deseja converter? "))

valor_em_real = valor_em_dolar * 5.51
valor_real_fixado = round(valor_em_real, 2)

print("A conversão do valor" ,valor_em_dolar, "em real é:" ,valor_real_fixado)