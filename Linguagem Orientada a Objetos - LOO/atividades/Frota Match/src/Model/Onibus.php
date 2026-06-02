<?php

class Onibus extends Veiculo {
    
    public function __construct(
        string $marca,
         string $modelo, 
         int $anoFabricacao, 
         TipoCombustivel $combustível,
         public readonly int $qtdPassageiros
    ){
        parent :: __construct(
        $marca, 
        $modelo,
        $anoFabricacao, 
        $combustível);
    }
    public function calcularTaxa(): float {
        return $this->qtdPassageiros * 35.00;
    }
}