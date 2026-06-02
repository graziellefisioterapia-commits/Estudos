<?php

require __DIR__ . '/src/Model/CategoriaEletronico.php';
require __DIR__ . '/src/Model/Produto.php';
require __DIR__ . '/src/Model/Geladeira.php.';
require __DIR__ . '/src/Model/Smartphone.php';
require __DIR__ . '/src/Services/Categoria.php';

//Instanciando Produtos

$novaGeladeira = new Geladeira("Electrolux", 3500, categoriaEletronico::ELETRODOMESTICOS,8);
$novoSmartphone= new Smartphone("Samsung", 4500, categoriaEletronico ::TELEFONIA, 15);

$calculadora = new CalculadoraDeFrete();

// Calculando o Frete ( Polimorfirmo em ação!)
$calculadora->CalcularFrete($novaGeladeira);
$calculadora->calcularFrete($novoSmartphone);

echo "Total do valor do Frete: R$ " . $calculadora->getTotal();