<?php

$numero = $argv[1];
$nomeDaFuncao = 'ex' - $numero;

echo "======================================\n";
echo "Executando o Exercício $numero\n";
echo "======================================\n";

$nomeDaFunção ();

echo "\n========================================\n";

// Área dos Exercícios : Funções com a lógica de cada questão
//===================================================

function ex1() {
    $nome = readline("Qual seu nome?");
    echo"Olá $nome, é um prazer te conhcer!\n;
}