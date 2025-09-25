programa {

  real preco,consumo,d,custo

  funcao inicio() {

  //entrada
  
  escreva("Preço do combustível(R$/L): ")
  leia(preco)
  escreva("Consumo do carro(km\L): ")
  leia(consumo)
  escreva("Distância da viagem(Km): ")
  leia(d)
  
  //processamento

  custo = d/(consumo/preco)

  //saída 
  
  escreva("O custo total da viagem será de R$: ",custo)




  }
}
