<?php
    class VerificadorDeEmprestimo {
        private int $dias = 0;
    
        public function tempoEmprestimo(MaterialDidatico $material): void {
            $this->dias += $material->calcularDiasEmprestimo();
        }
        
        public function getTotal(): float {
            return $this->dias;
        }
    }