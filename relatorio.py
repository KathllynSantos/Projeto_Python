from fpdf import FPDF
 
class PDF(FPDF):

    def titulo(self, label):

        self.set_font('helvetica', 'B', size=24)

        self.cell(0, 60, label, 0, 1, 'C')
 
    def sub_titulo(self, label):

        self.set_font('helvetica', 'I', size=16)

        self.cell(0, 10, label, 0, 1, 'C')

    def linha_centralizada(self, label):

        self.set_font('helvetica', '', size=12)

        self.cell(0, 10, label, 0, 1, 'C')

    def titulo_base(self, label):

        self.set_font('helvetica', 'B', size=16)

        self.cell(0, 10, label, 0, 1, 'L')

        self.ln()

    def paragrafo(self, text):

        self.set_font('helvetica', '', size=12)

        self.multi_cell(0, 7, text)

        self.ln()

    def imagem(self, img, x, y, w):

        self.image(img, x, y, w)

        

        self.ln(180)  
 


pdf = PDF()
 


pdf.add_page()
 
pdf.titulo("Relatório sobre Desigualdade Educacional no Brasil")

pdf.sub_titulo("Uma análise da distribuição de vagas e cursos")
 


img_path = "imagem_capa.jpg"  

img_w = 130

img_x = (pdf.w - img_w) / 2  

pdf.image(img_path, x=img_x, y=90, w=img_w) 

pdf.ln(100)  
 
pdf.linha_centralizada("Autor: Kathllyn Santos")

pdf.linha_centralizada("Data: 5 de Setembro de 2024")
 


pdf.add_page()
 
pdf.titulo_base("Introdução")
 
pdf.paragrafo(

    "A desigualdade educacional no Brasil é um tema recorrente em debates sobre o desenvolvimento social e econômico do país. "
    "Essa análise busca evidenciar a distribuição de instituições, cursos e vagas de ensino superior, e como essas variáveis "
    "estão distribuídas de forma desigual entre as diferentes regiões do Brasil. Os dados utilizados nesta análise foram tirados "
    "do Ministério da Educação (MEC)."

)
 
pdf.paragrafo(

    "Serão apresentados gráficos que ilustram a distribuição de instituições e vagas, com uma comparação entre modalidades "

    "de ensino e categorias administrativas (públicas e privadas), destacando as diferenças significativas entre as regiões."

)
 


pdf.add_page()
 
pdf.titulo_base("Análise 1: Distribuição de Instituições por Região")
 
pdf.paragrafo(

    "Nesta seção, analisamos o número de instituições de ensino superior presentes em cada região do Brasil. "

    "Observamos que as regiões mais desenvolvidas, como o Sudeste e o Sul, apresentam uma maior concentração de instituições, "

    "enquanto regiões como o Norte e Nordeste possuem uma menor oferta educacional."

)
 
pdf.imagem("grafico_instituicoes_por_regiao.png", 10, 60, 180)  

pdf.ln(10)  
 
pdf.paragrafo(

    "A concentração de instituições no Sudeste é significativamente maior do que no Norte, evidenciando um cenário de desigualdade "

    "que afeta diretamente o acesso à educação superior."

)
 


pdf.add_page()
 
pdf.titulo_base("Análise 2: Vagas Autorizadas por Região")
 
pdf.paragrafo(

    "Aqui, analisamos o número de vagas autorizadas por região. O gráfico a seguir demonstra que a maior parte das vagas está concentrada "

    "nas regiões Sudeste e Sul, enquanto o Norte apresenta o menor número de vagas disponíveis."

)
 
pdf.imagem("grafico_vagas_por_regiao.png", 10, 60, 180)  
pdf.ln(10) 
 
pdf.paragrafo(

    "Essa distribuição desigual de vagas dificulta o acesso de estudantes de regiões menos favorecidas a cursos de ensino superior, "

    "perpetuando a desigualdade educacional no país."

)
 


pdf.add_page()
 
pdf.titulo_base("Análise 3: Modalidade de Ensino por Região")
 
pdf.paragrafo(

    "Neste gráfico, comparamos a oferta de cursos presenciais e a distância (EAD) em cada região. A modalidade EAD aparece "

    "como uma alternativa importante para regiões com menor oferta de instituições, como o Norte e o Nordeste."

)
 
pdf.imagem("grafico_modalidade_por_regiao.png", 10, 60, 180)  
pdf.ln(10)  
 
pdf.paragrafo(

    "A educação a distância tem permitido a democratização do acesso ao ensino superior em locais onde a infraestrutura de ensino presencial é limitada, "

    "mas ainda existem barreiras como acesso à internet e qualidade do ensino."

)
 


pdf.add_page()
 
pdf.titulo_base("Conclusão")
 
pdf.paragrafo(

    "A análise da desigualdade educacional no Brasil revela uma clara concentração de instituições e vagas nas regiões mais ricas, como o Sudeste e o Sul, "

    "enquanto o Norte e o Nordeste continuam a enfrentar grandes desafios no acesso ao ensino superior."

)
 
pdf.paragrafo(

    "A modalidade de ensino a distância tem se mostrado uma ferramenta importante para reduzir a disparidade regional, mas é necessário mais investimento "

    "em infraestrutura e políticas públicas que incentivem o acesso à educação de qualidade em todas as regiões."

)
 
pdf.output("relatorio_desigualdade_educacional.pdf")

 