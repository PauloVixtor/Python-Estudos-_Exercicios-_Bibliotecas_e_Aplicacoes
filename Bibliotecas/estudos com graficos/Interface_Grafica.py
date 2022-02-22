import PySimpleGUI as sg

############## Multiplas Janelas ##############
"""
# Criar as Janelas e layout(layot)

def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout= layout, finalize=True)
def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox('Pizza Frango', key='pizza2')],
        # Chave de identificação key=
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar pedido', layout=layout, finalize=True)

# Criar as janelas iniciais

janela1, janela2 = janela_login(), None # Inicia apenas a primeira função e não puxa segunda janela

# Criar um loop de leitura de eventos

while True: # Criando loop para que o programa sempre esteja sendo lido.

    window, event, values = sg.read_all_windows() # Eventos de tela

    # Quando janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED: # Evento fecha arimeira janela
        break
    if window == janela2 and event == sg.WIN_CLOSED: # Evento fecha a segunda janela
        break

    # Quando queremos ir para proxima janela
    if window == janela1 and event == 'Continuar': # referenciando o botão continuar
        janela2 = janela_pedido() # Puxa a segunda janela
        janela1.hide() # Esconde a primeira janela

    # Quando queremos voltar para janela anterior
    if window == janela2 and event == 'Voltar':
        janela2.hide() # Esconde a segunda janela
        janela1.un_hide() # Exibi a primeira janela

    # Logica de o que deve acontecer com os botões
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Duas Pizzas foram Solicitadas!')
        elif values['pizza1'] == True:
            sg.popup('Foi Solicitado uma Pizza Pepperoni!')
        elif values['pizza2'] == True:
            sg.popup('Foi Solicitado uma Pizza de Frango!')"""

############## Temas das Janelas ##############

"""

# Lista de Temas de janelas
sg.theme('DarkTeal9')

layout = [[sg.Text('List of InBuilt Themes')],
          [sg.Text('Please Choose a Theme  to see Demo window')],
          [sg.Listbox(values=sg.theme_list(),
                      size=(20, 12),
                      key='-LIST-',
                      enable_events=True)],
          [sg.Button('Exit')]]

window = sg.Window('Theme List', layout)

# This is an Event Loop
while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break

    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

# Close
window.close()"""

############## Janela de login ##############

# layout
sg.theme('Reddit') # Tema escolhido


layout = [ # Criando layout
    [sg.Text('Usuario: '), sg.Input(key='usuario', size=(20, 1))], # Texto e informação a ser inserida com chave de localização, Tamanho
    [sg.Text('  Senha: '), sg.Input(key='senha', password_char='*', size=(20, 1))], # Texto, escrever, chave e proteção de dados, Tamanho
    [sg.Text(' Arquivo: '), sg.Input(key='arquivo', size=(20, 1))],
    [sg.Checkbox('Salvar o Login:')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout=layout)

# Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Paulo' and valores['senha'] == '123':
            print('Bem vindo!')
            sg.popup('Seja Bem-vindo!')


