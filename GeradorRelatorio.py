from reportlab.pdfgen import canvas


    



nome_empresa = input ('Digite o nome da empresa: \n')

regiao_atuacao = input ('Qual região a empresa atua: Nacional ou Internacional: \n' )

cronograma_definido = input ('A empresa conta com cronograma definido: caso sim, envie arquivo. \n' )

outros_nomes = input ('A empresa realiza negócios com outros nomes não se limitando ao nome fantasia e razão social? caso sim, qual? \n' )

terceiros = input ('A empresa envolve subcontratadas e/ou outros terceiros no curso normal do seu negócio e/ou serviços prestados aos seus clientes? caso sim, quais os serviços terceirizados? \n' )

clientes_empresa =input ('Quem são os principais clientes da empresa? Qual o setor de atuação? \n' )

fornecedores_empresa = input ('Quem são os principais fornecedores da empresa? Qual o setor de atuação? \n' )

valores_empresa = input ('A empresa conta com missão, visão e valores definidos? Caso sim, enviar arquivo. \n' )

politicas_empresa = input ('A empresa conta com políticas ou qualquer outro documento que trate do assunto de saúde e segurança? Se sim, enviar arquivo. Já houve algum evento de exposição negativa de algum funcionário? Se sim, descrever. \n')

vazamento = input ('A empresa já enfrentou algum caso de vazamento ou uso indevido de informações privilegiadas? Se sim, decrever. \n' )

destruicao = input ('A empresa já enfrentou algum caso de destruição ou uso indevido dos ativos? Se sim, descrever. \n' )

exposicao_empresa = input ('A empresa já enfrentou algum caso de exposição negativa nas redes sociais e outras mídias relaciondas? (fotos indevidas no facebook, posts indevidos no instagram). Se sim, descrever. \n' )

contratos_pub = input ('A empresa mantém, já manteve ou pretende manter contratos com a iniciativa pública? \n')

ent_gov = input ('A empresa é uma entidade governamental ou é de propriedade de alguma entidade governamental? \n' )


cargo_gov = input ('Algum Representante da empresa possui cargo no Governo? \n')

rep_gov = input ('Em caso afirmativo, (i) identifique o Representante da empresa; (ii) descreva seu cargo e responsabilidades na empresa; e (iii) descreva seu cargo no Governo. Caso não, basta responder um não há. \n' )

licencas = input ('A empresa necessita de licenças ou autorizações para atender os seus contratos? Ela é responsável por solicitar essas licenças? \n' )

reunioes_gov = input ('As atividades da empresa demandam interação com representantes do governo? Ex. reuniões, encontros de negócio e outros. \n' )

age_gov = input ('A empresa atua em setores regulados por agências governamentais, como, por exemplo, Agência Nacional de Petróleo ANP, Agência Nacional de Vigilância Sanitária Anvisa, Agência Nacional de Energia Elétrica Aneel etc.? \n' )

registro_empresa = input ('As operações financeiras ou patrimoniais da empresa são registradas em seu sistema contábil de forma transparente e precisa? \n' )

arquivo_empresa = input ('A documentação de suporte para as transações contábeis e financeiras é mantida em arquivo por 5 anos?  \n' )

fora_livro = input ('Existe alguma operação de cunho econômico, financeiro ou patrimonial da empresa que é realizada fora dos livros comerciais ou fiscais?  \n' )

livro_dentro = input ('Os livros e registros da empresa refletem a situação dos ativos da empresa de forma precisa, razoável e detalhada?  \n' )

canal_denuncia = input ('A empresa possui um canal de denúncia, endereço de e-mail ou algum outro canal por meio do qual os funcionários da empresa possas fazer denúncias anônimas de potenciais irregularidades? \n')

cod_etica = input ('A empresa tem código de ética e conduta ou alguma regra formal e escrita que descreva os limites da atuação dos representantes?  \n' )

comite_etica = input ('A empresa conta com um comitê de ética que se reúne periodicamente para tratar dos assuntos referentes ao tema?  \n' )

combate_corrupcao = input ('A empresa tem Políticas de Combate à Corrupção formais e escritas? \n' )

oferta_brindes = input ('A empresa tem  Políticas para oferta e recebimento de brindes, presentes e hospitalidades formais e escritas? \n' )

direitos_humanos = input ('A empresa possui política ou procedimento em vigor de prevenção e combate à violação de direitos humanos? \n' )

vaza_dados = input ('A empresa já teve incidente de vazamento de dados? \n' )

armazena_nuvem = input ('A empresa possuí sistema de armazenamento em cloud? \n' )

servico_dcenter = input ('A empresa contrata algum serviço de data center? \n' )

sof_gestao = input ('A empresa utiliza software para gestão de documentos? \n' )



frase1 = ('O nome da empresa é: ' + nome_empresa)
frase2 = ('A empresa atua na região ' + regiao_atuacao)
frase3 = ('A empresa conta com cronograma definido? '+ cronograma_definido)
frase4 = ('A empresa possui outros nomes? '+ outros_nomes)
frase5 = ('A empresa possui serviços terceirizados de qualquer tipo? '+ terceiros)
frase6 = ('Os principais clientes da empresa são: '+ clientes_empresa)
frase7 = ('Os principais fornecedores da empresa são: '+ fornecedores_empresa)
frase8 = ('A empresa conta com políticas ou qualquer outro documento que trate do assunto de saúde e segurança? '+ politicas_empresa)
frase9 = ('Conta com missão, visão e valores definidos? '+valores_empresa)
frase10 = ('Já enfrentou algum caso de vazamento ou uso indevido de informações privilegiadas? '+ vazamento)
frase11 = ('A empresa já enfrentou algum caso de destruição ou uso indevido dos ativos? '+ destruicao)
frase12 = ('A empresa já enfrentou algum caso de exposição negativa nas redes sociais e outras mídias relaciondas? '+ exposicao_empresa)
frase13 = ('A empresa mantém, já manteve ou pretende manter contratos com a iniciativa pública? '+ contratos_pub)
frase14 = ('A empresa é uma entidade governamental ou é de propriedade de alguma entidade governamental? '+ ent_gov)
frase16 = ('Algum Representante da empresa possui cargo no Governo? '+ cargo_gov)
frase17 = ('Identificação, cargo e responsabilidade na empresa, cargo no governo: '+ rep_gov)
frase18 = ('A empresa necessita de licenças ou autorizações para atender os seus contratos? '+ licencas)
frase19 = ('As atividades da empresa demandam interação com representantes do governo? '+ reunioes_gov)
frase20 = ('A empresa atua em setores regulados por agências governamentais? '+ age_gov)
frase30 = ('As operações financeiras e patrimôniais são registradas em seu sistema contábil? '+ registro_empresa)
frase31 = ('O arquivo da empresa é mantido por 5 anos? '+ arquivo_empresa)
frase32 = ('Existe alguma operação realizada fora dos livros comerciais ou fiscais? '+ fora_livro)
frase33 = ('Os registros refletem a situação dos ativos da empresa de forma precisa? '+ livro_dentro)
frase34 = ('A empresa possui canal de denúncia? '+ canal_denuncia)
frase35 = ('A empresa possui código de ética e conduda ou alguma regra formal que descreve os limites da atuação dos representantes? '+ cod_etica)
frase36 = ('A empresa possui comitê de ética? '+ comite_etica)
frase37 = ('A empresa possui políticas de combate à corrupção formais e escritas? '+ combate_corrupcao)
frase38 = ('Possui políticas de oferta e recebimentos de brindes? '+ oferta_brindes)
frase39 = ('Possui política de combate à violação dos direitos humanos? '+ direitos_humanos)
frase40 = ('A empresa já teve incidente de vazamento de dados? '+ vaza_dados)
frase41 = ('A empresa possuí sistema de armazenamento em cloud? '+ armazena_nuvem)
frase42 = ('A empresa contrata algum serviço de data center? '+ servico_dcenter)
frase43 = ('A empresa utiliza software para gestão de documentos? '+ sof_gestao)


y = 0
cnv= canvas.Canvas("RelatorioLgpd.pdf")
cnv.setFont("Times-Bold", 25)
cnv.drawString(100,800, "Relatório LGPD")
cnv.setFont("Times-Bold", 11)
    
for nome_empresa in frase1:
        y = y + 20
        cnv.drawString(0, 750 - y, frase1)
        break
for regiao_atuacao in frase2:
        y = y + 20
        cnv.drawString(0, 750 - y, frase2)    
        break
for cronograma_definido in frase3:
        y = y + 20
        cnv.drawString(0, 750 - y, frase3) 
        break
for outros_nomes in frase4:
        y = y + 20
        cnv.drawString(0, 750 - y, frase4) 
        break
        
for terceiros in frase5:
        y = y + 20
        cnv.drawString(0, 750 - y, frase5)
        break
        
for clientes_empresa in frase6:
        y = y + 20
        cnv.drawString(0, 750 - y, frase6)
        break
for fornecedores_empresa in frase7:
        y = y + 20
        cnv.drawString(0, 750 - y, frase7)
        break
for valores_empresa in frase8:
        y = y + 20
        cnv.drawString(0, 750 - y, frase8)
        break
for politicas_empresa in frase9:
        y = y + 20
        cnv.drawString(0, 750 - y, frase9)
        break
for vazamento in frase10:
        y = y + 20
        cnv.drawString(0, 750 - y, frase10)
        break
for destruicao in frase11:
        y = y + 20
        cnv.drawString(0, 750 - y, frase11)
        break
for exposicao_empresa in frase12:
        y = y + 20
        cnv.drawString(0, 750 - y, frase12)
        break
for contratos_pub in frase13:
        y = y + 20
        cnv.drawString(0, 750 - y, frase13)
        break
for contratos_pub in frase14:
        y = y + 20
        cnv.drawString(0, 750 - y, frase14)
        break 
for cargo_gov in frase16:
        y = y + 20
        cnv.drawString(0, 750 - y, frase16)
        break 
for rep_gov in frase17:
        y = y + 20
        cnv.drawString(0, 750 - y, frase17)
        break
for licencas in frase18:
        y = y + 20
        cnv.drawString(0, 750 - y, frase18)
        break
for reunioes_gov in frase19:
        y = y + 20
        cnv.drawString(0, 750 - y, frase19)
        break
for age_gov in frase20:
        y = y + 20
        cnv.drawString(0, 750 - y, frase20)
        break
for registro_empresa in frase30:
        y = y + 20
        cnv.drawString(0, 750 - y, frase30)
        break
for arquivo_empresa in frase31:
        y = y + 20
        cnv.drawString(0, 750 - y, frase31)
        break
for fora_livro in frase32:
        y = y + 20
        cnv.drawString(0, 750 - y, frase32)    
        break
    
for livro_dentro in frase33:
        y = y + 20
        cnv.drawString(0, 750 - y, frase33)
        break
for canal_denuncia in frase34:
        y = y + 20
        cnv.drawString(0, 750 - y, frase34)
        break
for cod_etica in frase35:
        y = y + 20
        cnv.drawString(0, 750 - y, frase35)
        break
for comite_etica in frase36:
        y = y + 20
        cnv.drawString(0, 750 - y, frase36) 
        break
for combate_corrupcao in frase37:
        y = y + 20
        cnv.drawString(0, 750 - y, frase37)
        break
for oferta_brindes in frase38:
        y = y + 20
        cnv.drawString(0, 750 - y, frase38)
        break
for direitos_humanos in frase39:
        y = y + 20
        cnv.drawString(0, 750 - y, frase39)
        break
for vaza_dados in frase40:
        y = y + 20
        cnv.drawString(0, 750 - y, frase40)
        break
for armazena_nuvem in frase41:
        y = y + 20
        cnv.drawString(0, 750 - y, frase41) 
        break
for servico_dcenter in frase42:
        y = y + 20
        cnv.drawString(0, 750 - y, frase42)  
        break
for sof_gestao in frase43:
        y = y + 20
        cnv.drawString(0, 750 - y, frase43)
        
        cnv.save()  
        