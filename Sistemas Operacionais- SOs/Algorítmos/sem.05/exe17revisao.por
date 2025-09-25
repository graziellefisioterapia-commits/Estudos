programa {

  cadeia nome
  real peso_unitario,peso_total,quantidade

  funcao inicio() {

    //entrada
    
    escreva("Nome do item: ")
    leia(nome)
    escreva("Peso Unitário (OZ): ")
    leia(peso_unitario)
    escreva("Quantidade em posse: ")
    leia(quantidade)

    //processamento

    peso_total = peso_unitario*quantidade




    //saída
   escreva ("----- Detalhes do Item -----") 
   escreva("Item:",nome)
   escreva("\nQuantidade: ",quantidade)
   escreva("\nPeso Unitário: ",peso_unitario," Oz")
   escreva("\nPeso Total: ",peso_total," Oz")

  }
}
