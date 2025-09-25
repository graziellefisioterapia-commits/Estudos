programa {
  
  const cadeia NOME_MAGIA = "energy beam"
  const inteiro CUSTO_MANA_MAGIA = 20
  inteiro quantidade_lancamentos
  inteiro custo_total_mana
  
funcao inicio() {

  escreva("---- Calculadora de Custo de Mana (Magia:", NOME_MAGIA, ") ----\n")


  escreva("\nQuantas vezes você pretende lançar a magia ",NOME_MAGIA, "? ")
  leia(quantidade_lancamentos)

  //processamento

  custo_total_mana= quantidade_lancamentos*CUSTO_MANA_MAGIA

  escreva("\nPara lançar a magia",NOME_MAGIA," ",quantidade_lancamentos, " vez(es), você gastará: ", custo_total_mana, " de mana.\n")

    
    
  }
}
