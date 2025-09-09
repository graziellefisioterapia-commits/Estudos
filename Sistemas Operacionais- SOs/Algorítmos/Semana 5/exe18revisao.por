programa {

  const real percentual_de_desconto = 0.15
  cadeia nome_produto
  real preco, pfinal,desconto


  funcao inicio() {

    //entrada

    escreva("Nome do Produto: ")
    leia(nome_produto)
    escreva("Preço Original: ")
    leia(preco)   

    //processamento

    desconto= preco*percentual_de_desconto
    pfinal= preco-desconto

    
    //saída
    escreva("\n--- Preço Promocional ---")

    escreva("\n\nProduto: ",nome_produto)
    escreva("\nPreço original: ",preco)
    escreva("\nDesconto (15.0%): ",desconto)
    escreva("\nPreço final: ",pfinal)
  }
}
