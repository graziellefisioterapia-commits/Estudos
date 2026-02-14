<?php
echo 'Média de Notas';


$somaDeNotas = $argv[1] ?? 0;
$somaDeNotas += $argv[2];
$somaDeNotas += $argv[3];




$mediadeNotas = $somaDeNotas /3;



echo"\n A média das três notas é: $mediadeNotas";

