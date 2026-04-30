<?php

class Serie extends Titulo
{
    //Atributos nome: string, anoLancamento: int, genero: string
    //notas: array (ela não é criada pela função construtora)

    //Atributos
    private array $notas;

    public function __construct(
        string $nome,
        int $anoLancamento,
        Genero $genero,
        int $Temporadas,
        public readonly  int $epiTemporadas,
        public readonly int $duraçãoDeEpisodio
    ) 
    //alt + shift + f (aninha o codigo sozinho)
    //Métodos
    {
        parent::__construct($nome, $anoLancamento, $genero);
    }

    public function duracaoEmMinutos():int
    {
       return $this->epiTemporadas*$this->epiTemporadas*$this->duraçãoDeEpisodio;
    }

    
}
