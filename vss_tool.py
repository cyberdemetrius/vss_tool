# Verificador de Senhas e Políticas Seguras - projeto base, necessita melhorias, implementações e funcionalidades
# Em caso de dúvidas, entre em contato

# Importando a biblioteca Tkinter para criar a interface gráfica
# 'datetime' e 'timedelta' do módulo 'datetime' para manipular datas para verificar a questão da expiração de senhas

import tkinter as tk
from datetime import datetime, timedelta

# Funções de verificação de políticas de segurança
def verifica_senha_forte():
    senha = entry_senha.get()
    # Implementação da lógica para verificar se a senha é forte...
    comprimento_minimo = 8
    tem_caracter_especial = False
    tem_numero = False

    if len(senha) >= comprimento_minimo:
        for char in senha:
            if char in "!@#$%^&*()_+-=[]{};:,.<>?":
                tem_caracter_especial = True
            if char.isdigit():
                tem_numero = True

    if tem_caracter_especial and tem_numero:
        resultado_senha.config(text="A senha é forte!", fg="green")
    else:
        resultado_senha.config(text="A senha não atende aos critérios de complexidade.", fg="red")

def verifica_expiracao_senha():
    data_ultima_mudanca = datetime.strptime(entry_ultima_mudanca.get(), "%Y-%m-%d")
    dias_expiracao = 180  # A senha deve ser alterada a cada 180 dias
    data_atual = datetime.now()

    if (data_atual - data_ultima_mudanca).days > dias_expiracao:
        resultado_expiracao.config(text="A senha precisa ser atualizada.", fg="red")
    else:
        resultado_expiracao.config(text="A senha está dentro do prazo de expiração.", fg="green")

# Configuração da janela
root = tk.Tk()
root.title("Verificador de Senhas e Políticas Seguras")

# Labels, Entradas e Botões para os critérios (código anterior)
label_senha = tk.Label(root, text="\nSenha:")
label_senha.pack()
entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

button_verificar_senha = tk.Button(root, text="Verificar Senha", command=verifica_senha_forte)
button_verificar_senha.pack()
resultado_senha = tk.Label(root, text="")
resultado_senha.pack()

label_ultima_mudanca = tk.Label(root, text="Última mudança de senha (AAAA-MM-DD):")
label_ultima_mudanca.pack()
entry_ultima_mudanca = tk.Entry(root)
entry_ultima_mudanca.pack()

button_verificar_expiracao = tk.Button(root, text="Verificar Expiração", command=verifica_expiracao_senha)
button_verificar_expiracao.pack()
resultado_expiracao = tk.Label(root, text="")
resultado_expiracao.pack()

# Novos critérios e funcionalidades (adicionados)
label_tentativas = tk.Label(root, text="Número de tentativas malsucedidas de login:")
label_tentativas.pack()
entry_tentativas = tk.Entry(root)
entry_tentativas.pack()

def verifica_bloqueio_conta():
    tentativas_falhas = int(entry_tentativas.get())
    tentativas_maximas = 5  # Exemplo: conta bloqueada após 5 tentativas

    if tentativas_falhas >= tentativas_maximas:
        resultado_tentativas.config(text="A conta pode estar bloqueada.", fg="red")
    else:
        resultado_tentativas.config(text="A conta provavelmente não está bloqueada.", fg="green")

button_verificar_tentativas = tk.Button(root, text="Verificar Tentativas", command=verifica_bloqueio_conta)
button_verificar_tentativas.pack()
resultado_tentativas = tk.Label(root, text="")
resultado_tentativas.pack()

root.mainloop()
