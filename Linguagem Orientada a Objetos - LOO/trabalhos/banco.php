<?php

$saldo = 1000;
echo "***********BEM VINDO*******************\n";
echo "***********GRAZIELLE MOREIRA*******************\n";

do{

echo "Menu Principal\n";
echo "1 - Consultar saldo atual\n";
echo "2 - Sacar valor\n";
echo "3 - Depositar Valor\n";
echo "4 - Adeus\n";


$opcao= (float) fgets(STDIN);

switch ($opcao) {
    case 1:
        echo "Consultar saldo atual\n";
        echo "Seu saldo atual é: $saldo\n";
        break;

    case 2:
        echo "Sacar valor\n";
        echo "Qual valor deseja sacar?";
        $saque = (float)fgets(STDIN);

        if($saque>$saldo){
            echo "Saldo Insuficiente\n";
        }
        else {
            $saldo-=$saque;
            echo"Novo Saldo:".$saldo."\n";
        }
        break;

    case 3:
        echo "Depositar valor\n";
        echo "Qual valor a ser depositado?";
        $deposito =  (float) fgets(STDIN);
        
        if ($deposito<0){
            echo "valor inválido para depósito\n";
        }
        else
            $saldo+=$deposito;{
            echo "Seu novo saldo é: $saldo";
        }
        break;

    case 4:{
        echo "Adeus\n";
        break;}
        
        default:
        echo "Opcao inválida";
   
}

}while($opcao!=4);