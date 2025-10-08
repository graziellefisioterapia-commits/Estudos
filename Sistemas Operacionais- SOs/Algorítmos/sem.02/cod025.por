programa {
  
  inteiro a, b, c

  funcao inicio() {

    // Entrada 

    escreva("Digite o comprimento do primeiro segmento: ")
    leia(a)
    escreva("Digite o comprimento do segundo segmento: ")
    leia(b)
    escreva("Digite o comprimento do terceiro segmento: ")
    leia(c)
    
    // saída
    se( (c<a+b) e (b<a+c) e (a<b+c) ){
    
      escreva("É possível formar um triângulo!")
    
    }

    senao{

    escreva("Não é possível formar um triângulo!")

    }

  }
}
