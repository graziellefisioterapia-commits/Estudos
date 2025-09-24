programa {

cadeia produto1, produto2
inteiro qtd1,qtd2
real preco,subtotal1,subtotal2,qtd1,qtd2,vt




  funcao inicio() {

//Entrada
    escreva ("--- Supermecardo Preço Bom ---\n Vamos registrar sua compra!\n\n")

    escreva ("---Produto 1---\n")
    escreva ("Digite o nome do produto: \n")
    leia (produto1)
    escreva ("Digite a quantidade: \n")
    leia (qtd1)
    escreva ("Digite o preço unitário: R$ \n")
    leia (preco)


    escreva ("---Produto 2---\n")
    escreva ("Digite o nome do produto: \n")
    leia (produto2)
    escreva ("Digite a quantidade: \n")
    leia (qtd2)
    escreva ("Digite o preço unitário: R$\n\n")
    leia (preco)

//Processamento

subtotal1=qtd1*preco
subtotal2=qtd2*preco
vt=subtotal1+subtotal2



//Saída

  escreva ("---Recibo da Compra---\n")
  escreva ("Item: ",produto1, "\n")
  escreva ("Qtde: ",qtd2, " | Preço Unit: ", preco, " | Subtotal: R$", subtotal1, "\n\n")

  escreva ("Item: " ,produto2, "\n")
  escreva ("Qtde: ",qtd2, "| Preço Unit: ", preco, "| Subtotal: R$", subtotal2, "\n\n")

  escreva("---------------------------------\n VALOR TOTAL DA COMPRA: R$",vt, "\n --------------------------------")

     
    
  }
}
