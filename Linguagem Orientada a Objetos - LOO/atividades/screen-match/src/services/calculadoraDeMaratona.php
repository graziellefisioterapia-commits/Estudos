<?php

class calculadora{

private int $duracaoMaratona,

public function incluir(Titulo $titulo): void{
$this->duracaoMaratona += $titulo->duracaoEmMinutos();
}

public function getDuracao(){
    return$this->duracaoMaratona;
}
}