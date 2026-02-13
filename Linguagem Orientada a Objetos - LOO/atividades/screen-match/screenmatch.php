<?php
    //$nomeFilme  = "Top Gun - Maverick";
    //$nomeFilme = "Thor Ragnarok";
    //$nomeFilme = "Se beber não case";

    $genero = match ($nomeFilme) {
        "Top Gun - Maverick" => "Ação",
        "Thor Ragnarok" => "Super Herói",
        "Se beber não case" => "Comédia",
        default => "Desconhecido",
    };

    $anoLancamento = $argv[1] ?? 2022; //2022;              //Int

    $somaNotas = 9;
    $somaNotas +=6;
    $somaNotas +=8;
    $somaNotas +=7.5;
    $somaNotas +=5;

    //Soma de Valores em Variáveis
    $notaFilme = $somaNotas/5;            //Float
    $planoPrime = true;            //Bool

    $incluidoNoPlano = $planoPrime || $anoLancamento < 2000;
    
    
    
    //No php a variável é definida automaticamente

    echo "\nBem Vindo ao Screen Match\n";

    echo "\nNome do Filme: $nomeFilme\n";
    echo 'Ano do Filme: ' .$anoLancamento ."\n";    //Concatenando
    echo "Nota do Filme: $notaFilme\n";
    echo "Incluido no plano: $incluidoNoPlano\n";
    echo "Genero do filme : $genero\n";
    //php teste.php

    if ($anoLancamento > 2022) {
        echo 'Lancamento!';
    } elseif ($anoLancamento > 2020 && $anoLancamento <= 2022) {
        echo 'Ainda é novo.';
    } else {
        echo 'Não é Lançamento';
    }