import random
datas=["04/09/476", "21/06/622", "25/12/800", 15/08/1096","15/06/1215", "29/05/1453", "12/10/1492", "31/10/1517", "14/07/1789", "18/06/1815", "12/04/1861", "28/06/1914", "25/10/1917", "24/10/1929", "07/05/1945", "20/07/1969", "09/11/1989", "11/09/2001"]
dicas=["O Império Romano do Ocidente termina em 476 d.C., quando o Imperador Rômulo Augusto é obrigado a abdicar em favor de Odoacro, chefe militar de origem germânica.",
Hégira foi a fuga de Maomé de Meca para Medina, que marca o ano inicial do calendário islâmico",
"Carlos Magno, rei dos Francos, foi coroado imperador do Sacro Império Romano pelo papa Leão III, na antiga Basílica de S. Pedro",
"Início da primeira cruzada, que ficou conhecida como “Cruzada dos Nobres”, ou “Cruzada dos Barões”, por ter sido organizada pela nobreza.", 
"Com o Rei enfraquecido pelas derrotas, houve uma grande pressão dos nobres, liderados por Robert Fitzwalter, que forçou o Rei João a assinar a Magna Carta, para evitar uma guerra civil.",
"Queda de Constantinopla, a cidade foi invadida e subjugada pelos otomanos, comandados pelo sultão Mehmed II.", 
"Descobrimento da América, a chegada e ocupação pelo navegador Cristóvão Colombo.",
 "Martinho Lutero escreveu 95 teses que criticavam a Igreja Católica e Papa.",
 "Tomada da batilha, o marco inicial da revolução francesa.",
"A Batalha de Waterloo foi o confronto final após anos de guerra entre as nações europeias e o imperador francês Napoleão Bonaparte.",
 "Início da Guerra Civil Americana, também chamada de Guerra de Secessão foi um confronto armado entre os estados do Norte contra os estados do Sul dos Estados Unidos.",
"O herdeiro do império austro-húngaro, o arquiduque Francisco Ferdinando, foi assassinado juntamente com sua esposa.",
  "O Partido Bolchevique, liderado por Lênin, derrubou o governo provisório e instaurou o governo socialista soviético.",
"A grande depressão foi um abalo econômico que teve início nos Estados Unidos logo após a quebra da Bolsa de Valores de Nova York. O capitalismo internacional foi alvo dessa crise e marcou a decadência do liberalismo econômico",
"Rendição da Alemanha na 2ª Guerra Mundial",
"Neil Armstrong foi o primeiro homem a pisar a Lua, como comandante da missão Apollo 11.",
  "A queda do muro de Berlim,um evento crucial na história mundial que marcou a queda da Cortina de Ferro.", 
  "O atentado às torres gêmeas foram uma série de ataques suicidas contra os Estados Unidos coordenados pela organização fundamentalista islâmica Al-Qaeda",
"A pandemia do COVID-19 teve início em dezembro de 2019 na cidade de Wuhan, na província de Hubei, na China, e desde então se espalhou para quase todos os países ao redor do mundo."]
escolhido=random.choice(datas)
i=datas.index(escolhido)
print(dicas[i])
n=input("Data: ")
if n==datas[i] or n==datas[i].replace("/", ""):
	print("Voce acertou!")
else:
	print("Você errou!")