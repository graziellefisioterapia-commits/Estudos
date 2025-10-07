programa {

  real nota1, nota2, media
  cadeia nome

  funcao inicio() {
    
    //entrada

    escreva("Digite o nome do aluno: ")
    leia(nome) 
    escreva("Digite a 1° nota: ")
    leia(nota1)
    escreva("Digite a 2° nota: ")
    leia(nota2)

    //processamento

    media=(nota1+nota1)/2

    //saída

    se(media>=7.0){
      escreva("Você ficou acima da média, sua media foi ", media)
    }

    senao{
      escreva("Você ficou abaixo da média, sua media foi ", media)

    }
     }
}
