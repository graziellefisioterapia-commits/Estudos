<?php

require __DIR__ . '/src/Model/TipoCombust%C3%ADvel.php';
require __DIR__ . '/src/Model/Veiculo.php';
require __DIR__ . '/src/Model/Carro.php.';
require __DIR__ . '/src/Model/Onibus.php';
require __DIR__ . '/src/Services/CalculadoraDeIPVA.php';

//Instanciando Veículos

$meuCarro = new Carro("Fiat","Uno", 2020, TipoCombustivel::GASOLINA,5);
$meuOnibus = new Onibus("Mercedes-Benz", "O500", 2018, TipoCombustivel::DIESEL, 4);

$calculadora = new CalculadoraDeIPVA();

// Calculando o imposto  ( Polimorfirmo em ação!)
$calculadora->incluirNoCalculo($meuCarro);
$calculadora->incluirNoCalculo($meuOnibus);

echo "Total de impostos a pagar da frota: R$ " . $calculadora->getTotal();