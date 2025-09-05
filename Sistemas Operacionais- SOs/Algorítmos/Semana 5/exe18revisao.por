programa {

  const real PERCENTUAL_DESCONTO = 0.15
  cadeia nome_produto
  real preco_original, preco_final,valor_do_desconto,desconto


  funcao inicio() {

    //entrada

    escreva("Nome do Produto: ")
    leia(nome_produto)
    escreva("Preço Original: ")
    leia(preco_original)   

    //processamento

    desconto= (preco_original*PERCENTUAL_DESCONTO)
    preco_final= (preco_original-valor_do_desconto)

    
    //saída
    escreva("--- Preço Promocional ---")

    escreva("\nProduto: ",nome_produto)
    escreva("\nPreço original: ",preco_original)
    escreva("Desconto (15.0%): ",desconto)
    escreva("Preço fianl: ", preco_final)
  }
}
