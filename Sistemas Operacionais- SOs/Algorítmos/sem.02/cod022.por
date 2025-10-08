programa {

  real ano, result, idade, ano_atual

  funcao inicio() {

  //entrada
	escreva("Digite o ano de nascimento:")
	leia(ano)
	escreva("Digite o ano atual: ")
	leia(ano_atual)
		
	idade=ano_atual-ano
	result=idade-18
		
	//processamento e saída 
	se(idade>18){
	escreva("Você nao pode se alistar ja se passaram ",result, " anos do alistamento!")
	}
        
	senao{ 
  
  result=18-idade
	escreva("Você não pode se alistar, ainda faltam ",result, " anos!")
	}
		
}   
}