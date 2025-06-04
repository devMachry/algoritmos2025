import random
print("PIZZARIA BOM LAR")
print("1. Pedido")
print("2. Formas de Pagamento")
print("3. Reclamação")
print("4. Falar com o atendente")
opcao = int(input("OPÇÃO: "))

if(opcao == 1):
    print("\n\nTudo sobre o Pedido")
    print("----------------------")
    print("1. Realizar pedido")
    print("2. Consultar pedido")
    print("3. Cancelar pedido")
    print("4. Voltar")

    opc_pedido = int(input("Opção: "))

    if(opc_pedido == 1):
        print("\nRealizar novo pedido")
        tam = input("Informe o tamanho da Pizza P, M ou G: ").upper()

        print("===== MENU DE PIZZAS =====")
        print("20. Calabresa")
        print("21. Margherita")
        print("22. Frango com Catupiry")
        print("23. Portuguesa")
        print("24. Quatro Queijos")
        print("25. Pepperoni")
        print("26. Vegetariana")
        print("27. Bacon com Cheddar")
        print("==========================")

        if(tam == "P"):
            preco = 35
        elif(tam == "M"):
            preco = 48.90
        elif(tam == "G"):
            preco = 59.90
    
        sabor = int(input("Informe o código do sabor: "))

        formaEntrega = input("Digite R para retirar no local ou E para entrega: ").upper

        if(formaEntrega == "E"):
            taxa = 10
            preco = preco + taxa
       

        numeroPedido = random.randint(1, 1000)

        print("======== Resumo do pedido ========")
        print(f"Número do pedido: {numeroPedido}")
        print("Resumo do pedido:")
        print(f"Tamanho: {tam}")
        print(f"Código do Sabor: {sabor}")
        print(f"Taxa de entrega: {taxa}")
        print(f"Preço total: {preco}")
        print("===================================")

    elif(opc_pedido == 2):
        print("\nConsultando pedido...")
        print("Informe o código do pedido:")
    
    elif(opc_pedido == 3):
        print("\nCancelamento de pedidos...")
        print("Informe o número do pedido para cancelamento:")
    
    elif(opc_pedido == 4):
        print("\nVoltando ao menu anterior...")
    
    else:
        print("\nOpção inválida!!")

elif(opcao == 2):
    print("Formas de Pgto")

elif(opcao == 3):
    print("Reclamação")

elif(opcao == 4):
    print("Falar com atendente")

else:
    print("Opção inválida...")