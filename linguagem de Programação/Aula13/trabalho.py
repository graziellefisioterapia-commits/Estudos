import webbrowser
import pyautogui
import time

pyautogui.alert(text='Bem-vindo ao sistema da loja Day variedades', title='Inicialização', button='OK')

nome = pyautogui.prompt(text='Digite seu nome:', title='Informação obrigatória')
email = pyautogui.prompt(text='Digite seu email:', title='Informação obrigatória')

resposta = pyautogui.confirm(
    text=f'Confirme seus dados:\n\n Nome: {nome}\n\n Email: {email}\n\nDeseja continuar?',
    title='Confirmação',
    buttons=['Sim', 'Cancelar']
)

if resposta == 'Sim':
    pyautogui.alert('Você será direcionado ao site em 3 segundos.', title='Redirecionando...')
    time.sleep(3)

    webbrowser.open('https://www.boticario.com.br/')
    time.sleep(5)

    pyautogui.press('end')
    time.sleep(2)
    pyautogui.scroll(300)

    time.sleep(2)
    pyautogui.click(x=645, y=391)
    pyautogui.write(nome)
    time.sleep(2)
    pyautogui.click(x=915, y=389)
    pyautogui.write(email)
    time.sleep(2)
    pyautogui.press('enter')
else:
    pyautogui.alert('Processo cancelado pelo usuário', title='Cancelado') 