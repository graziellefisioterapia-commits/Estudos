#criar um pequeno sistema automatizado que mostre uma mensagem de alerta e configuraçãopara o ususário, peça informações básicas (nome e email) confirme se o usuárioquer continuar, caso simtire automaticamente uma captura de tela

import pyautogui 
import time 
pyautogui.alert(text='Bem-vindo ao sistema automatizador',title='Inicio da automação',button='ok')

nome=pyautogui.prompt(text='Digite seu nome:',
                      title='Informação obrigatória')

email=pyautogui.prompt(text='Digite seu email:',
                       title='Informação obrigatória')

resposta=pyautogui.confirm(
    text=f'Confirme seus dados:\n\n nome: {nome}\n\n Email: {email}\n\n Deseja  continuarcom a captura de tela?',
    title='confirmação de dados', 
    buttons=['Sim','Não','Cancelar']
)

if resposta=='Sim':
    pyautogui.alert('Prepare-se! A captura de tela será feita em 3 segundos',title='Captura de tela')
    time.sleep(3)
    pyautogui.screenshot('Captura_usuário.png')
    pyautogui.alert('Captura realizada com sucesso', title='sucesso')

elif resposta=='não':
    pyautogui.alert('Processo cancelado pelo usuário', title='Cancelado')

else:pyautogui.alert('Automação foi interrompida', title='Encerrado')


print (f'Nome: {nome}')
print(f'Email: {email}')
print(f'Resposta do usuário: {resposta}')