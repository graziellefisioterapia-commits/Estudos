programa {

  real peso,altura,imc

  funcao inicio() {

    //entrada

    escreva("Digite o seu peso: ")
    leia(peso)
    escreva("Digite sua altura (m): ")
    leia(altura)
    
    
    //processamento

    imc= peso/(altura*altura)

    //saída
    
    escreva("Seu IMC é: ",imc)
  }
}
