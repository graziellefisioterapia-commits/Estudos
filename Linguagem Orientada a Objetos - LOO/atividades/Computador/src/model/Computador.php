<?php

class Computador {

 public function __construct(
        public readonly Marca $marca,
        public readonly Situacao $situacao,
        public readonly string $descricao)

        {}
}