import win32com.client as win32


# Criar a integração com outlook
outlook = win32.Dispatch('outlook.application')

# Criar um email
email = outlook.CreateItem(0)

# Adiconando variaveis ao email.
faturamento = 1500
qtde = 10
ticket_medio = faturamento / qtde

# Configurar as informações do email

email.To = "paulovixtor22@gmail.com"
email.Subject = "Email teste de automatização 03.02"
# Formata o email em HTML
email.HTMLBody = f"""
<p>Olá, esse é um teste python!</p>

<p>Exemplo: O faturamento da loja foi de R$ {faturamento:.2f}</p>
<p>         Vendemos {qtde} produtos</p>
<p>O ticket medio foi de R$ {ticket_medio:.2f}</p>

<p>Abs,</p>

<p>Codigo Python</p>
"""

# Como adicionar um anexo // pode fazer para diversos anexos
# anexo = "C:/Users/.xlsx"
# email.Attachments.Add(anexo)

# Como enviar o email
email.Send()

print('Email enviado!')



# Infos:
"""
email.To = "Destino"
email.Subject = "Assunto"
email.HTMLBody = "Corpo do email"
email.Body = "Corpo do email"
"""