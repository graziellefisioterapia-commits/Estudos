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
function ex009 (){
  let n1 = parseInt(document.getElementById("inputex009").value);
  let n2 = parseInt(document.getElementById('inputex0010').value);
  let n3 = parseInt(document.getElementById('inputex0011').value);
  let media = (n1+n2+n3)/3;
  let campoResultado = document.getElementById("resultadoex009");
  campoResultado.textContent = media;
}
function ex010 (){
  let n1 = parseInt(document.getElementById("inputex12").value);
  let n2 = parseInt(document.getElementById("inputex13").value);
  
  let campoResultado = document.getElementById("resultadoex010");
  if (n1 > n2){
    campoResultado.textContent = n1;
  }else{
    campoResultado.textContent = n2;
  }
}
function ex011 (){
  let n1 = parentInt(document.getElementById("inputex14").value);
  let campoResultado = document.getElementById("resultadoex011");
  let multiplicacao = (n1 * n1);
  campoResultado.textContent = multiplicacao;
}
function ex012 (){
  let altura = parseFloat(document.getElementById("inputex15").value);
  let peso = parseFloat(document.getElementById("inputex16").value);
  let campoResultado = document.getElementById("resultadoex012")
  let imc = peso/ (altura * altura);
  campoResultado.textContent = imc;
}
function ex013 (){
  let numero = document.getElementById("inputex17").value; 
   alert (numero)
  let campoResultado = document.getElementById("resultadoex013");
  let fatorial = 1
  for(let i = numero; i >= 1; i--){
        fatorial = fatorial * i;
    }
  campoResultado.textContent = fatorial;
}
function ex014 ()
