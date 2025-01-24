
git remote add origin https://github.com/GabrielMReis/streamlit-imoveis.git

def calcular_beneficio():
    print("Simulador de Benefício da Nova Lei de IR sobre Imóveis")
    print("Insira os dados do imóvel para verificar se a nova lei compensa:\n")
    
    valor_compra = float(input("Valor de compra do imóvel (R$): "))
    valor_atual = float(input("Valor atual do imóvel (R$): "))
    tempo_ate_venda = int(input("Tempo estimado até a venda (anos): "))
    
    ganho_capital = valor_atual - valor_compra
    imposto_atual = ganho_capital * 0.15  # 15% de imposto
    imposto_antecipado = ganho_capital * 0.04  # 4% de imposto

    if tempo_ate_venda > 15:
        desconto_ganho_capital = ganho_capital * 0.15  # Sem imposto futuro
    else:
        desconto_ganho_capital = ganho_capital * 0.15 * (tempo_ate_venda / 15)

    beneficio_liquido = imposto_atual - (imposto_antecipado + desconto_ganho_capital)

    print("\nResultados da Simulação:")
    print(f"Ganho de capital: R$ {ganho_capital:.2f}")
    print(f"Imposto pelo regime atual: R$ {imposto_atual:.2f}")
    print(f"Imposto antecipado com a nova lei: R$ {imposto_antecipado:.2f}")
    print(f"Desconto no imposto futuro: R$ {desconto_ganho_capital:.2f}")
    print(f"Benefício líquido da nova lei: R$ {beneficio_liquido:.2f}")
    
    if beneficio_liquido > 0:
        print("A nova lei pode ser vantajosa para você!")
    else:
        print("A nova lei não parece vantajosa nesse caso.")

# Executar o simulador
calcular_beneficio()
