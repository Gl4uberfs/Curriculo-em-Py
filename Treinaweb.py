import os
from time import sleep

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

def leiaStr(msg):
    ok = False
    string = str
    while True:
        n = str(input(msg))
        if n.isalpha():
            string = str(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite uma informação válida.\033[m')
        if ok:
            break
    return string

def processar_resposta(resposta, nome):
    if resposta == 1:
        print('\033[32mGerando informação...\033[m')
        sleep(2)
        print(f'''{os.linesep}Olá, tudo bem? Espero que sim. 
        Nome: Glauber Felipe Santos Silva    | Idade: 23 anos                      
        Telefone: (11) 95805-2925            | Endereço Residencial: Vila dos Andrades - ZN/SP
        E-mail: gabbe.mars@gmail.com         | Estado Civil: Solteiro
        LinkedIn: www.likendin.com/in/glauberfss
        {os.linesep}''')
    elif resposta == 2:
        print('\033[32mGerando informação...\033[m')
        sleep(2)
        print(f'''{os.linesep}Data Lover atuando em Fraud Prevention Analyst há mais de 1 ano
e com perfil altamente colaborativo e resiliente. Prazer em buscar
soluções inovadoras para problemas complexos.
Dentre as experiências, constam:
● Data Analyst;
● Fraud Prevention Analyst;
● BackOffice;
● Uso da linguagem Python para coleta e análise de dados;
● Desenvolvimento de dashboards utilizando ferramentas como
Tableau;
● Sistema Operacional Linux;
● Bancos de Dados - SQL;
● Elaboração de relatórios. {os.linesep}''')
    elif resposta == 3:
        print('\033[32mGerando informação...\033[m')
        sleep(2)
        print(f'''{os.linesep}Business Intelligence (BI)
Data Analysis
Tableau
Python
Linux 
MySQL
Fraud Prevention Analyst {os.linesep}''')
    elif resposta == 4:
        print('\033[32mGerando informação...\033[m')
        sleep(2)
        print(f'''{os.linesep}Teleperformance
Expert em Interação III
março de 2020 - Presente (atual)
São Paulo, Brasil\t

Autônomo
Ajudante de Bar
fevereiro de 2016 - dezembro de 2019 (3 anos 11 meses)
Ituaçu-BA{ os.linesep}''')
    elif resposta == 5:
        print('\033[32mGerando informação...\033[m')
        sleep(2)
        print(f'''{os.linesep}Univesp Oficial
Data Scientist, Computer Engineering · (agosto de 2022)\t

UNOPAR - Universidade Norte do Paraná
Bachelor of Software , Computer Software Engineering · (março de
2022 - junho de 2025){os.linesep}''')
    
def start():
    #apresentar quem sou eu
    print('Olá! Me chamo Glauber.\n')
    print('Venho apresentar a vocês o meu curriculo em python\n')
    #pedir o nome
    nome = input('Informe seu nome: ')
    while True:
        #Oferecer o menu de opções
        print(f'''Olá {nome}, O que gostaria de saber? 
        [1] - Informações! 
        [2] - Resumo.
        [3] - Principais competências. 
        [4] - Experiência. 
        [5] - Formação acadêmica. ''')
        resposta = leiaInt('Digite sua opção: ')
        #processar a resposta enviada
        processar_resposta(resposta, nome)
        opcao = ' '
        sleep(3)
        opcao = leiaStr('Quer saber mais? [digite "sair" para encerrar]: ').upper()
        if opcao == 'SAIR':
            print('\033[32mVocê está saindo...')
            sleep(1)
            print('Muito Obrigado! Até mais.\033[m')
            sleep(1)
            break


if __name__ == '__main__':
    start()