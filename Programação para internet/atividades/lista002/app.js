function ex001 (){
  let texto = document.querySelector("h1");
  texto.textContent = "Hora do Desafio";
}
function ex002 (){
console.log("O botão foi clicado");
}
function ex003 (){
  alert ("Eu amo Js");
}
function ex004 (){
  let cidade = prompt ("Digite uma cidade do Brasil");
  alert ("Estive em "+cidade+"e lembrei de você");
}
function ex005 (){
  let n1 = parseInt(prompt ("Digite um número inteiro"));
  let n2 = parseInt(prompt ("Digite um número inteiro"));
  let soma = n1 + n2;
  alert (soma)
}
function ex006 (){
  console.log("Olá Mundo");
}
function ex007 (){
  let nome = document.getElementById("inputEx07").value;
  console.log("Olá "+nome+"!");
}
function ex008 (){
  let n1 = parseInt(document.getElementById("inputex008").value);
  let dobro = n1 * 2; 
  let campoResultado = document.getElementById("resultadoex008");
  campoResultado.textContent = dobro;

}