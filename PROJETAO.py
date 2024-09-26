from tkinter import*
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

janela = Tk()



class relatorios():
    def printclientes(self):
        webbrowser.open("cliente.pdf")

    def gerarelatorio(self):
        self.c = canvas.Canvas("cliente.pdf", pagesize=A4)

        self.codigorel = self.codigo_entry.get()
        self.nomerel = self.nome_entry.get()
        self.quantidade = self.quantidade_entry.get()
        self.valorembalagem = self.valorembalagem_entry.get()

    
        
        self.data = self.data_entry.get()
        self.cliente = self.nomecliente_entry.get()
        self.contato = self.contato_entry.get()
        self.endereco = self.endereco_entry.get()
        self.cidade = self.cidade_entry.get()
        self.hora = self.hora_entry.get()
        self.cpf_cnpj = self.cpfcnpj_entry.get()
        self.telefone = self.telefone_entry.get()
        self.bairro = self.bairo_entry.get()
        self.vencimento = self.vencimento_entry.get()
        self.desconto = self.desconto_entry.get()
        self.nota_pedido = self.nota_pedido_entry.get()
        
        
        

        #INFORMAÇÕES DA EMPRESA
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(200, 820, 'SOUZA & SILVA COM. VAR. DE ALIM. E. BEBIDAS LTDA')
        self.c.drawString(200, 805, 'CNPJ: 24.390.400/0001-19')
        self.c.drawString(200, 790, 'Fones: (84) 99407-4644 / (84) 3206-5141')
        self.c.drawString(200, 775, 'Natal/RN')
        self.c.drawString(505, 820, 'VIA CLIENTE')

        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(200, 407, 'SOUZA & SILVA COM. VAR. DE ALIM. E. BEBIDAS LTDA')
        self.c.drawString(200, 392, 'CNPJ: 24.390.400/0001-19')
        self.c.drawString(200, 377, 'Fones: (84) 99407-4644 / (84) 3206-5141')
        self.c.drawString(200, 362, 'Natal/RN')
        self.c.drawString(500, 405, 'VIA EMPRESA')

        #INFORMAÇÕES DO CLIENTE
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(20, 750, 'Data:')
        self.c.drawString(20, 730, 'Cliente:')
        self.c.drawString(20, 710, 'Contato:')
        self.c.drawString(20, 690, 'Endereço:')
        self.c.drawString(20, 670, 'Cidade:')
        self.c.drawString(330, 750, 'Hora:')
        self.c.drawString(330, 730, 'CPF/CNPJ:')
        self.c.drawString(330, 710, 'Telefone:')
        self.c.drawString(330, 690, 'Bairro:')
        self.c.drawString(330, 670, 'Vencimento:')
        self.c.drawString(470, 760, 'Nota de Pedido n:')

        self.c.drawString(20, 330, 'Data:')
        self.c.drawString(20, 310, 'Cliente:')
        self.c.drawString(20, 290, 'Contato:')
        self.c.drawString(20, 270, 'Endereço:')
        self.c.drawString(20, 250, 'Cidade:')
        self.c.drawString(330, 330, 'Hora:')
        self.c.drawString(330, 310, 'CPF/CNPJ:')
        self.c.drawString(330, 290, 'Telefone:')
        self.c.drawString(330, 270, 'Bairro:')
        self.c.drawString(330, 250, 'Vencimento:')
        self.c.drawString(470, 348, 'Nota de Pedido n:')

        #INFORMAÇÕES QUE VÃO PREENCHER AS INFORMAÇÕES DO CLIENTE.
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(70, 750, self.data)
        self.c.drawString(70, 730, self.cliente)
        self.c.drawString(70, 710, self.contato)
        self.c.drawString(70, 690, self.endereco)
        self.c.drawString(70, 670, self.cidade)
        self.c.drawString(390,750, self.hora)
        self.c.drawString(390, 730, self.cpf_cnpj)
        self.c.drawString(390, 710, self.telefone)
        self.c.drawString(390, 690, self.bairro)
        self.c.drawString(390, 670, self.vencimento)
        self.c.drawString(540, 760, self.nota_pedido)

        self.c.drawString(70, 330, self.data)
        self.c.drawString(70, 310, self.cliente)
        self.c.drawString(70, 290, self.contato)
        self.c.drawString(70, 270, self.endereco)
        self.c.drawString(70, 250, self.cidade)
        self.c.drawString(390,330, self.hora)
        self.c.drawString(390, 310, self.cpf_cnpj)
        self.c.drawString(390, 290, self.telefone)
        self.c.drawString(390, 270, self.bairro)
        self.c.drawString(390, 250, self.vencimento)
        self.c.drawString(540, 348, self.nota_pedido)

        linha = 615
        for i, v in enumerate(self.itens_list):
            self.c.drawString(20, linha, str(i))
            self.c.drawString(80, linha, v["Nome"])
            self.c.drawString(220, linha,v["Quantidade"])
            self.c.drawString(300, linha,'05 UNI')
            self.c.drawString(385, linha, v["Valor_uni"])
            self.c.drawString(500, linha, str(float(v["Valor_uni"]) * float(v["Quantidade"])))
            linha -= 15


        linha = 195
        for i, v in enumerate(self.itens_list):
            self.c.drawString(20, linha, str(i))
            self.c.drawString(80, linha, v["Nome"])
            self.c.drawString(220, linha,v["Quantidade"])
            self.c.drawString(300, linha,'05 UNI')
            self.c.drawString(385, linha, v["Valor_uni"])
            self.c.drawString(500, linha, str(float(v["Valor_uni"]) * float(v["Quantidade"])))
            linha -= 15

        
        soma_valor_uni = 0
        for item in self.itens_list:
            quantidade = int(item["Quantidade"])
            valor_uni = float(item["Valor_uni"])
            soma_valor_uni += valor_uni * quantidade
            
        if self.desconto == '':
            self.c.drawString(545, 436, str(soma_valor_uni))
            self.c.drawString(360, 436, str(soma_valor_uni))
            self.c.drawString(545, 18, str(soma_valor_uni))
            self.c.drawString(360, 18, str(soma_valor_uni))
            self.c.drawString(460,436, '0')
            self.c.drawString(460, 18, '0')
                
        else:
            desconto = self.desconto
            tora = soma_valor_uni - int(desconto)
            self.c.drawString(360, 436, str(soma_valor_uni))
            self.c.drawString(460, 436, desconto)
            self.c.drawString(545,436, str(int(tora)))

            self.c.drawString(360, 18, str(soma_valor_uni))
            self.c.drawString(460, 18, desconto)
            self.c.drawString(545,18, str(int(tora)))


        #Relação do itens
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(20, 650, 'Relação dos itens:')

        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(20, 630, 'Item:')
        self.c.drawString(80, 630, 'Descrição:')
        self.c.drawString(220, 630, 'Quant:')
        self.c.drawString(300, 630, 'Medida:')
        self.c.drawString(385, 630, 'Valor Unit:')
        self.c.drawString(500, 630, 'Valor total:')
        #self.c.drawString(80, 462, 'TOTAL DE ITENS')
        self.c.drawString(20, 436, 'Observações:')
        
        
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(310, 436, 'SUBTOTAL:')
        self.c.drawString(410, 436, 'DESCONTO:')
        self.c.drawString(510, 436, 'TOTAL:')



        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(20, 230, 'Relação dos itens:')

        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(20, 210, 'Item:')
        self.c.drawString(80, 210, 'Descrição:')
        self.c.drawString(220, 210, 'Quant:')
        self.c.drawString(300, 210, 'Medida:')
        self.c.drawString(385, 210, 'Valor Unit:')
        self.c.drawString(500, 210, 'Valor total:')
        #self.c.drawString(80, 30, 'TOTAL DE ITENS')
        self.c.drawString(20, 18, 'Observações:')
        

        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(310, 18, 'SUBTOTAL:')
        self.c.drawString(410, 18, 'DESCONTO:')
        self.c.drawString(510, 18, 'TOTAL:')

        # self.c.drawString(20, 195, '1')
        # self.c.drawString(20, 180, '2')
        # self.c.drawString(20, 165, '3')
        # self.c.drawString(20, 150, '4')
        # self.c.drawString(20, 135, '5')
        # self.c.drawString(20, 120, '6')
        # self.c.drawString(20, 105, '7')
        # self.c.drawString(20, 90, '8')
        # self.c.drawString(20, 75, '9')
        # self.c.drawString(20, 60, '10')
        # self.c.drawString(20, 45, '11')
        # self.c.drawString(20, 30, '12')


        self.c.rect(20, 770, 550, 60, fill=False, stroke=True) #Quadrado que está la em cima que contém CNPJ e etc.
        self.c.rect(20, 667, 550, 1, fill=True, stroke=False) # 1-?, 2-Ele muda o X( para cima ou para baixo), 3- Aumenta sua largura para direita
        self.c.rect(20, 628, 550, 1, fill=True, stroke=False) #Linha que está embaixo de item, descrição, etc.
        self.c.rect(20, 445, 550, 1, fill=True, stroke=False) #Linha que está embaixo de "12".
        #self.c.rect(20, 432, 550, 1, fill=True, stroke=False) #Linha que está embaixo de 'SUBTOTAL, DESCONTO, TOTAL'.
        self.c.rect(20, 358, 550, 60, fill=False, stroke=True) #Segundo quadrado que está la embaixo
        self.c.rect(20, 247, 550, 1, fill=True, stroke=False) #Em baixo de cidade e vencimento.
        self.c.rect(20, 208, 550, 1, fill=True, stroke=False) # Linha qu está em baixo de item, descrição, etc.
        self.c.rect(20, 26, 550, 1, fill=True, stroke=False)
        


        self.c.showPage()
        self.c.save()
        
        self.printclientes()

class func(relatorios):
    def novo_relatorio(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.quantidade_entry.delete(0, END)
        self.valorembalagem_entry.delete(0, END)
         
        self.itens_list = []

    def limpa_produto(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.quantidade_entry.delete(0, END)
        self.valorembalagem_entry.delete(0, END)
        

    def limpa_produto2(self):
        self.codigo_entry.delete(0, END)
        self.nomecliente_entry.delete(0, END)
        self.contato_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.hora_entry.delete(0, END)
        self.cpfcnpj_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.bairo_entry.delete(0, END)

    def conecta_bancodedados(self):
        self.conn = sqlite3.connect('churrasco.bd')
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')

    def conecta_bancodedados2(self):
        self.conn_2 = sqlite3.connect('clientela.bd')
        self.cursor_2 = self.conn_2.cursor(); print('Conectado ao banco de dados dos clientes')

    def desconecta_bancodedados(self):
        self.conn.close(); print('Desconectando ao banco de dados')

    def desconecta_bancodedados2(self):
        self.conn.close(); print('Desconectando ao banco de dados')
 
    def montatabela(self):
        self.conecta_bancodedados()

        #CRIANDO A TABELA
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS churrasquinho (
                            cod INTEGER PRIMARY KEY,
                            nome char(40) NOT NULL,
                            quantidade INT,
                            valor DECIMAL(10,2),
                            unidade TEXT DEFAULT 'PCT 05UN'
                        ); 
                    """)
        self.conn.commit(); print('Banco de dados criado')
        self.desconecta_bancodedados()
        

    
        
    
        #CRIANDO A TABELA
        self.conecta_bancodedados()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientela (
                            cod_cliente INTEGER PRIMARY KEY,
                            nome VARCHAR(100),
                            contato TEXT,
                            endereco TEXT,
                            cidade TEXT,
                            hora TEXT,
                            cpf_cnpj TEXT,
                            telefone TEXT,
                            bairro TEXT,
                            data TEXT
                            
                        ); 
                    """)
        self.conn.commit(); print('Bando de dados dos clientes criados')
        self.desconecta_bancodedados()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.quantidade = self.quantidade_entry.get()
        self.valorproduto = self.valorembalagem_entry.get()

    def variaveis2(self):
        self.data = self.data_entry.get()
        self.nomecliente = self.nomecliente_entry.get()
        self.contato = self.contato_entry.get()
        self.endereco = self.endereco_entry.get()
        self.cidade = self.cidade_entry.get()
        self.hora = self.hora_entry.get()
        self.cpf_cnpj = self.cpfcnpj_entry.get()
        self.telefone = self.telefone_entry.get()
        self.bairro = self.bairo_entry.get()
            
    def add_produto(self):
        self.variaveis()
        self.conecta_bancodedados()

        self.cursor.execute("""INSERT INTO churrasquinho (nome, quantidade, valor)
                            VALUES (?, ?, ?) """, (self.nome, self.quantidade, self.valorproduto))
        self.conn.commit()
        self.desconecta_bancodedados()
        self.selecione_lista()
        self.limpa_produto()

    def add_produto2(self):
        self.variaveis2()
        self.conecta_bancodedados()

        self.cursor.execute("""INSERT INTO clientela (nome, contato, endereco, cidade, hora, cpf_cnpj, telefone, bairro)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?) """,(self.nomecliente, self.contato, self.endereco, self.cidade, self.hora, self.cpf_cnpj, self.telefone, self.bairro))
        self.conn.commit()
        self.desconecta_bancodedados2()
        self.selecione_lista()
        self.limpa_produto()

    def selecione_lista(self):
        self.listapro.delete(*self.listapro.get_children())
        self.conecta_bancodedados()
        lista = self.cursor.execute("""SELECT cod, nome, quantidade, valor FROM churrasquinho 
                                    ORDER BY nome ASC; """)
        for i in lista:
            self.listapro.insert("", END, values=i)
        self.desconecta_bancodedados()

    
        self.listapro2.delete(*self.listapro2.get_children())
        self.conecta_bancodedados()
        lista2 = self.cursor.execute("""SELECT cod_cliente, nome, contato, endereco, cidade, hora, cpf_cnpj, telefone, bairro FROM clientela
                                    ORDER BY nome ASC; """)
        for o in lista2:
            self.listapro2.insert("", END, values=o)
        self.desconecta_bancodedados()

    def duplocliks(self, event):
        self.limpa_produto()
        self.listapro.selection()

        for n in self.listapro.selection():
            col1, col2, col3, col4 = self.listapro.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.quantidade_entry.insert(END, col3)
            self.valorembalagem_entry.insert(END, col4)

    
        self.limpa_produto2()
        self.listapro2.selection()

        for n in self.listapro2.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listapro2.item(n, 'values')
            self.codigo2_entry.insert(END, col1)
            self.nomecliente_entry.insert(END, col2)
            self.contato_entry.insert(END, col3)
            self.endereco_entry.insert(END, col4)
            self.cidade_entry.insert(END, col5)
            self.hora_entry.insert(END, col6)
            self.cpfcnpj_entry.insert(END, col7)
            self.telefone_entry.insert(END, col8)
            self.bairo_entry.insert(END, col9)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bancodedados()
        self.cursor.execute("""DELETE FROM churrasquinho WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bancodedados()
        self.limpa_produto()
        self.selecione_lista()

    def deleta_cliente2(self):
        self.variaveis2()
        self.conecta_bancodedados2()
        self.cursor.execute("""DELETE FROM clientela WHERE cod_cliente = ? """, (self.codigo2))
        self.conn.commit()
        self.desconecta_bancodedados2()
        self.limpa_produto2()
        self.selecione_lista()      

    def alterar_produto(self):
        self.variaveis()
        self.conecta_bancodedados()
        self.cursor.execute("""UPDATE churrasquinho SET nome = ?, quantidade = ?, valor = ?
                            WHERE cod = ? """, (self.nome, self.quantidade, self.valorproduto, self.codigo))
        self.conn.commit()
        self.desconecta_bancodedados()
        self.selecione_lista()
        self.limpa_produto()

    def buscar_produto(self):
        self.conecta_bancodedados()
        self.listapro.delete(*self.listapro.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute("""SELECT cod, nome, quantidade, valor FROM churrasquinho
                            WHERE nome LIKE '%s' ORDER BY NOME ASC""" % nome)
        
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listapro.insert("", END, values=i)
        self.limpa_produto()
        self.desconecta_bancodedados()
        
        
        

class aplicacao(func, relatorios):
    def __init__(self):
        self.itens_list = []
        self.janela = janela
        self.tela()

        self.frame_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.montatabela()
        self.selecione_lista()
        self.buscar_produto()
        self.menus()
        janela.mainloop()
        
    def tela(self):
        self.janela.title('TABELA DE PREÇOS')
        self.janela.configure(background='#1e3743')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True) #Deixa o cliente aumentar as telas horizontais e verticais.
        self.janela.maxsize(width=988, height=788) #Deixa o cliente aumentar a tela horizontal e vertical até um certo limite.
        self.janela.minsize(width=500, height=400) #Deixa o cliente diminuir a tela horizontal vertical até um certo limite.

    def frame_da_tela(self):
        self.frame1 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46) # A interação com o número é de 0 e 1.

        self.frame2 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def adicionar_item_lista(self):
        self.itens_list.append(
            {
                "Nome":self.nome_entry.get(),
                "Quantidade":self.quantidade_entry.get(),
                "Valor_uni":self.valorembalagem_entry.get(),
                "Desconto":self.desconto_entry.get()
            }
        )

        

    def widgets_frame1(self):

        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background='#dfe3ee')
        self.aba2.configure(background='#dfe3ee')
        
        self.abas.add(self.aba1, text='aba1')
        self.abas.add(self.aba2, text='aba2')

        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        #CRIAÇÃO DO BOTÃO LIMPAR ABA1
        self.bt_limpar = Button(self.aba1, text='Limpar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.limpa_produto)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        #CRIANDO BOTÃO DE BUSCAR ABA1
        self.bt_buscar = Button(self.aba1, text='Buscar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.buscar_produto)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        #CRIANDO BOTÃO INSERIR
        self.bt_incrementar = Button(self.aba1, text='Inserir', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.adicionar_item_lista)
        self.bt_incrementar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)

        #CRIANDO BOTÃO NOVO ABA1
        self.bt_novo = Button(self.aba1, text='Novo', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'),command=self.add_produto)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        #CRIANDO BOTÃO ALTERAR ABA1
        self.bt_alterar = Button(self.aba1, text='Alterar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.alterar_produto)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        #CRIANDO BOTÃO APAGAR ABA1
        self.bt_apagar = Button(self.aba1, text='Apagar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #CRIAÇÃO DO BOTÃO LIMPRAR ABA2
        self.bt_limpar2 = Button(self.aba2, text='Limpar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold' ), command=self.limpa_produto2)
        self.bt_limpar2.place(relx=0.85, rely=0.050, relwidth=0.1, relheight=0.15)

        #CRIAÇÃO DO BOTÃO BUSCAR ABA2
        self.bt_buscar2 = Button(self.aba2, text='Buscar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold' ))
        self.bt_buscar2.place(relx=0.85, rely=0.25, relwidth=0.1, relheight=0.15)

        #CIRAÇÃO DO BOTÃO NOVO ABA2
        self.bt_novo2 = Button(self.aba2, text='Novo', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.add_produto2)
        self.bt_novo2.place(relx=0.85, rely=0.45, relwidth=0.1, relheight=0.15)

        #CRIAÇÃO DO BOTÃO ALTERAR ABA2
        self.bt_alterar2 = Button(self.aba2, text='Alterar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_alterar2.place(relx=0.85, rely=0.65, relwidth=0.1, relheight=0.15)

        #CRIAÇÃO DO BOTÃO APAGAR ABA2
        self.bt_apagar2 = Button(self.aba2, text='Apagar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.deleta_cliente2)
        self.bt_apagar2.place(relx=0.85, rely=0.85, relwidth=0.1, relheight=0.15)

        #CRIAÇÃO DA LABEL E ENTRADA DO CÓDIGO ABA1
        self.lb_codigo = Label(self.aba1, text='Código', bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.aba1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        #CRIAÇÃO DA LABEL E ENTRADA DO NOME ABA1
        self.lb_nome = Label(self.aba1, text='Nome', bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        #CRIAÇÃO DA LABEL DA QUANTIDADE ABA1
        self.lb_quantidade = Label(self.aba1, text='Quantidade', bg='#dfe3ee', fg='#107db2')
        self.lb_quantidade.place(relx=0.05, rely=0.6)

        self.quantidade_entry = Entry(self.aba1)
        self.quantidade_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        #CRIAÇÃO DA LABEL VALOR DA EMBALAGEM ABA1
        self.lb_valorembalagem = Label(self.aba1, text='Valor da embalagem', bg='#dfe3ee', fg='#107db2')
        self.lb_valorembalagem.place(relx=0.5, rely=0.6)

        self.valorembalagem_entry = Entry(self.aba1)
        self.valorembalagem_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

        #CRIAÇÃO DA LABEL E ENTRADA DO DATA ABA2
        self.lb_data = Label(self.aba2, text='Data', bg='#dfe3ee', fg='#107db2')
        self.lb_data.place(relx=0.75, rely=0.005)

        self.data_entry = Entry(self.aba2)
        self.data_entry.place(relx=0.75, rely=0.1, relwidth=0.08)

        #CRIAÇÃO DA LABEL E ENTRADA DO DESCONTO ABA2
        self.lb_desconto = Label(self.aba2, text='Desconto', bg='#dfe3ee', fg='#107db2')
        self.lb_desconto.place(relx=0.75, rely=0.5)

        self.desconto_entry = Entry(self.aba2)
        self.desconto_entry.place(relx=0.75, rely=0.6, relwidth=0.08)

        #CRIAÇÃO DA LABEL E ENTRADA NO NOME DO CLIENTE ABA2
        self.lb_nomecliente = Label(self.aba2, text='Nome do cliente', bg='#dfe3ee', fg='#107db2')
        self.lb_nomecliente.place(relx=0.03, rely=0.005)

        self.nomecliente_entry = Entry(self.aba2)
        self.nomecliente_entry.place(relx=0.03, rely=0.1, relwidth=0.3)

        #CRIAÇÃO DA LABEL E ENTRADA NO CONTATO ABA2
        self.lb_contato = Label(self.aba2, text='Contato', bg='#dfe3ee', fg='#107db2')
        self.lb_contato.place(relx=0.03, rely=0.25)

        self.contato_entry = Entry(self.aba2)
        self.contato_entry.place(relx=0.03, rely=0.35, relwidth=0.3)

        #CRIAÇÃO DA LABEL E ENTRADA NO ENDEREÇO ABA2    
        self.lb_endereco = Label(self.aba2, text='Endereço', bg='#dfe3ee', fg='#107db2')
        self.lb_endereco.place(relx=0.03, rely=0.5)

        self.endereco_entry = Entry(self.aba2)
        self.endereco_entry.place(relx=0.03, rely=0.6, relwidth=0.3)

        #CRIAÇÃO DA LABEL E ENTRADA NA CIDADE ABA2
        self.lb_cidade = Label(self.aba2, text='Cidade', bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.03, rely=0.75)

        self.cidade_entry = Entry(self.aba2)
        self.cidade_entry.place(relx=0.03, rely=0.85, relwidth=0.3)

        #CRIAÇÃO DA LABEL E ENTRADA NA HORA ABA2
        self.lb_hora = Label(self.aba2, text='Hora', bg='#dfe3ee', fg='#107db2')
        self.lb_hora.place(relx=0.4, rely=0.005)

        self.hora_entry = Entry(self.aba2)
        self.hora_entry.place(relx=0.4, rely=0.1, relwidth=0.3)

        #CRIAÇÃO DA LABEL E ENTRADA DE CPF/CNPJ ABA2
        self.lb_cpfcnpj = Label(self.aba2, text='CPF/CNPJ', bg='#dfe3ee', fg='#107db2')
        self.lb_cpfcnpj.place(relx=0.4, rely=0.25)

        self.cpfcnpj_entry = Entry(self.aba2)
        self.cpfcnpj_entry.place(relx=0.4, rely=0.35, relwidth=0.3)

        #CRIAÇÃO DA LABEL E ENTRADA DE TELEFONE ABA2
        self.lb_telefone = Label(self.aba2, text='Telefone', bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.4, rely=0.5)

        self.telefone_entry = Entry(self.aba2)
        self.telefone_entry.place(relx=0.4, rely=0.6, relwidth=0.3)

        #CRIAÇÃO DA LABEL E ENTRADA DO BAIRRO ABA2
        self.lb_bairro = Label(self.aba2, text='Bairro', bg='#dfe3ee', fg='#107db2')
        self.lb_bairro.place(relx=0.4, rely=0.75)

        self.bairo_entry = Entry(self.aba2)
        self.bairo_entry.place(relx=0.4, rely=0.85, relwidth=0.3)

        #CRIAÇÃO DA LABEL E ENTRADA DO VENCIMENTO ABA2
        self.lb_vencimento = Label(self.aba2, text='Venc', bg='#dfe3ee', fg='#107db2')
        self.lb_vencimento.place(relx=0.75, rely=0.25)

        self.vencimento_entry = Entry(self.aba2)
        self.vencimento_entry.place(relx=0.75, rely=0.35, relwidth=0.08)

        #CRIAÇÃO DA LABEL E ENTRADA DA NOTA DE PEDIDO
        self.lb_nota_pedido = Label(self.aba2, text='Nota Ped', bg='#dfe3ee', fg='#107db2')
        self.lb_nota_pedido.place(relx=.75, rely=0.75)
        
        self.nota_pedido_entry = Entry(self.aba2)
        self.nota_pedido_entry.place(relx=0.75, rely=0.85, relwidth=0.08)


    def widgets_frame2(self):

        self.abas = ttk.Notebook(self.frame2)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background='#dfe3ee')
        self.aba2.configure(background='#dfe3ee')
        
        self.abas.add(self.aba1, text='aba1')
        self.abas.add(self.aba2, text='aba2')

        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        self.listapro = ttk.Treeview(self.aba1, height=3, column=("col1", "col2", "col3", "col4"))
        self.listapro.heading('#0', text='')
        self.listapro.heading('#1', text='Código')
        self.listapro.heading('#2', text='Nome')
        self.listapro.heading('#3', text='Quantidade')
        self.listapro.heading('#4', text='Valor da embalagem')

        self.listapro.column('#0', width=1)
        self.listapro.column('#1', width=50)
        self.listapro.column('#2', width=200)
        self.listapro.column('#3', width=125)
        self.listapro.column('#4', width=125)

        self.listapro.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollista = Scrollbar(self.aba1, orient='vertical') #Ngc de rolagem, aprendendo ainda.
        self.listapro.configure(yscroll=self.scrollista.set)
        self.scrollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listapro.bind("<Double-1>", self.duplocliks)

    

        self.listapro2 = ttk.Treeview(self.aba2, height=3, column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.listapro2.heading('#0', text='')
        self.listapro2.heading('#1', text='Cod')
        self.listapro2.heading('#2', text='Nome')
        self.listapro2.heading('#3', text='Contato')
        self.listapro2.heading('#4', text='Endereço')
        self.listapro2.heading('#5', text='Cidade')
        self.listapro2.heading('#6', text='Hora')
        self.listapro2.heading('#7', text='CPF/CNPJ')
        self.listapro2.heading('#8', text='Telefone')
        self.listapro2.heading('#9', text='Bairro')
        

        self.listapro2.column('#0', width=1)
        self.listapro2.column('#1', width=10)
        self.listapro2.column('#2', width=50)
        self.listapro2.column('#3', width=70)
        self.listapro2.column('#4', width=50)
        self.listapro2.column('#5', width=30)
        self.listapro2.column('#6', width=20)
        self.listapro2.column('#7', width=50)
        self.listapro2.column('#8', width=50)
        self.listapro2.column('#9', width=50)


        self.listapro2.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollista = Scrollbar(self.aba2, orient='vertical') #Ngc de rolagem, aprendendo ainda.
        self.listapro.configure(yscroll=self.scrollista.set)
        self.scrollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listapro.bind("<Double-1>", self.duplocliks)

    def menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.janela.destroy()

        menubar.add_cascade(label = "Opções", menu = filemenu)
        menubar.add_cascade(label = "Relatorios", menu = filemenu2)

        filemenu.add_command(label = "Sair", command=quit)
        filemenu.add_command(label = "Novo relatório", command = self.novo_relatorio)

        filemenu2.add_command(label = "Ficha do cliente", command=self.gerarelatorio)



        





aplicacao()        