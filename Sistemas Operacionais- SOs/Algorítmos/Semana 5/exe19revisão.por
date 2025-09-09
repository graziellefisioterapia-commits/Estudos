programa {

  real nota1,nota2,nota3,media,soma

  funcao inicio() {

    //entrada

    escreva("Digite o primeiro valor: ")
    leia(nota1)
    escreva("Digite o segundo valor: ")
    leia(nota2)
    escreva("Digite o terceiro valor: ")
    leia(nota3)

    //processamento

    soma=nota1+nota2+nota3
    
    media=soma/3

    //saída

    escreva("--- Resultados ---")
    escreva("\nValores: ",nota1," , ",nota2," , ",nota3)
    escreva("\nsoma total: ",soma)
    escreva("\nmedia: ",media)






    
  }
}
