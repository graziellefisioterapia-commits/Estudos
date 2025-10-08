programa {
  
  real km, preco1, preco2

  funcao inicio() {
    
		//entrada
		escreva("Digite a km que o cliente vai pecorrer: ")
		leia(km)

		
		//processamento e saída

		se(km<=200){
    preco1=km*0.50
			
		escreva("Sua viajem vicará no valor de R$ ",preco1)
			
		}
		senao{
		preco2=km*0.45
            
     escreva("Sua viagem ficará no valor de R$ ",preco2)
		}
		
	}
}

  }
}
