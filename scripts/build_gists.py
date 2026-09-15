#!/usr/bin/env python3
"""Build the per-passage gist files — the on-demand "meaning in your language" fallback.

A concise 1–2 sentence meaning per passage, offered only where a learner is likely to get
stuck (the pivotal/dense beats and every ending — "where needed"), not on every passage.
Emits content/gist/<lang>.json → { "<nodeId>": "gist" }, lazy-loaded per language.

Authored here in the five languages Claude can vouch for (fr, es, it, de, pt). Russian,
Arabic and Mandarin are left for native translators — the reader simply shows no meaning
control for a language that has no gist for that node.
"""
import json, os

L = ["fr", "es", "it", "de", "pt"]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "gist")
os.makedirs(OUT, exist_ok=True)

# nodeId : [fr, es, it, de, pt]
G = {
 1: [
  "Vous arrivez de nuit dans une ville inconnue avec une lettre : un entretien d'embauche chez Kessler & Rowe, 14 Rosewater Street, mardi à neuf heures. La gare est vide et froide.",
  "Llegas de noche a una ciudad desconocida con una carta: una entrevista de trabajo en Kessler & Rowe, 14 Rosewater Street, el martes a las nueve. La estación está vacía y fría.",
  "Arrivi di notte in una città sconosciuta con una lettera: un colloquio di lavoro da Kessler & Rowe, 14 Rosewater Street, martedì alle nove. La stazione è vuota e fredda.",
  "Sie kommen nachts in einer fremden Stadt an, mit einem Brief: ein Vorstellungsgespräch bei Kessler & Rowe, Rosewater Street 14, Dienstag um neun. Der Bahnhof ist leer und kalt.",
  "Chegas de noite a uma cidade desconhecida com uma carta: uma entrevista de emprego na Kessler & Rowe, Rosewater Street 14, terça-feira às nove. A estação está vazia e fria.",
 ],
 7: [
  "Rosewater Street est sombre et à moitié en travaux. Le numéro 14 est un immeuble gris et poussiéreux, à l'abandon : la société est manifestement partie depuis longtemps.",
  "Rosewater Street está oscura y medio en obras. El número 14 es un edificio gris y polvoriento, abandonado: la empresa se marchó hace tiempo.",
  "Rosewater Street è buia e mezza in cantiere. Il numero 14 è un palazzo grigio e polveroso, abbandonato: l'azienda se n'è andata da tempo.",
  "Die Rosewater Street ist dunkel und halb Baustelle. Nummer 14 ist ein graues, staubiges, verlassenes Gebäude: die Firma ist längst weg.",
  "A Rosewater Street está escura e meio em obras. O número 14 é um prédio cinzento e poeirento, abandonado: a empresa foi-se há muito.",
 ],
 24: [
  "Une agence pour l'emploi, trop neuve et trop souriante, propose du travail — mais réclame d'abord 200 d'« inscription ». C'est le piège de l'histoire.",
  "Una agencia de empleo, demasiado nueva y sonriente, ofrece trabajo, pero pide primero 200 de «inscripción». Es la trampa de la historia.",
  "Un'agenzia per il lavoro, troppo nuova e sorridente, offre lavoro ma chiede prima 200 di «iscrizione». È la trappola della storia.",
  "Eine Arbeitsagentur, zu neu und zu freundlich, bietet Arbeit an — verlangt aber erst 200 „Anmeldegebühr“. Das ist die Falle der Geschichte.",
  "Uma agência de emprego, nova e sorridente demais, oferece trabalho mas pede primeiro 200 de «inscrição». É a armadilha da história.",
 ],
 32: [
  "Vous payez les 200. On vous donne un reçu sans adresse ni nom, juste un numéro. Votre argent est parti.",
  "Pagas los 200. Te dan un recibo sin dirección ni nombre, solo un número. Tu dinero se ha ido.",
  "Paghi i 200. Ti danno una ricevuta senza indirizzo né nome, solo un numero. I tuoi soldi sono spariti.",
  "Sie zahlen die 200. Man gibt Ihnen eine Quittung ohne Adresse und Namen, nur eine Nummer. Ihr Geld ist weg.",
  "Pagas os 200. Dão-te um recibo sem morada nem nome, só um número. O teu dinheiro desapareceu.",
 ],
 33: [
  "Vous refusez de payer. Le sourire de l'homme disparaît aussitôt : vous aviez raison, c'était une arnaque. Vous gardez votre argent.",
  "Te niegas a pagar. La sonrisa del hombre desaparece al instante: tenías razón, era una estafa. Conservas tu dinero.",
  "Ti rifiuti di pagare. Il sorriso dell'uomo sparisce subito: avevi ragione, era una truffa. Tieni i tuoi soldi.",
  "Sie weigern sich zu zahlen. Das Lächeln des Mannes verschwindet sofort: Sie hatten recht, es war Betrug. Ihr Geld bleibt Ihnen.",
  "Recusas-te a pagar. O sorriso do homem desaparece logo: tinhas razão, era uma fraude. Ficas com o teu dinheiro.",
 ],
 35: [
  "Mme Rowe lit votre lettre et comprend l'erreur : la société a déménagé il y a deux ans, mais quelqu'un envoie encore l'ancienne adresse. Elle vous invite à vous asseoir.",
  "La Sra. Rowe lee tu carta y comprende el error: la empresa se mudó hace dos años, pero alguien sigue enviando la dirección antigua. Te invita a sentarte.",
  "La signora Rowe legge la lettera e capisce l'errore: l'azienda ha traslocato due anni fa, ma qualcuno manda ancora il vecchio indirizzo. Ti invita a sederti.",
  "Frau Rowe liest Ihren Brief und versteht den Fehler: die Firma ist vor zwei Jahren umgezogen, aber jemand verschickt noch die alte Adresse. Sie bittet Sie, sich zu setzen.",
  "A Sra. Rowe lê a tua carta e percebe o erro: a empresa mudou-se há dois anos, mas alguém ainda envia a morada antiga. Convida-te a sentar.",
 ],
 36: [
  "Vous lui racontez toute votre nuit. Touchée que vous ne soyez pas rentré chez vous, elle vous embauche : votre première tâche sera de corriger les lettres. (Bonne fin.)",
  "Le cuentas toda tu noche. Conmovida de que no te hayas ido a casa, te contrata: tu primera tarea será corregir las cartas. (Final bueno.)",
  "Le racconti tutta la notte. Colpita dal fatto che non sei tornato a casa, ti assume: il tuo primo compito sarà correggere le lettere. (Finale buono.)",
  "Sie erzählen ihr die ganze Nacht. Gerührt, dass Sie nicht heimgefahren sind, stellt sie Sie ein: Ihre erste Aufgabe wird sein, die Briefe zu korrigieren. (Gutes Ende.)",
  "Contas-lhe toda a noite. Comovida por não teres ido para casa, contrata-te: a tua primeira tarefa será corrigir as cartas. (Final bom.)",
 ],
 37: [
  "Pas de poste aujourd'hui, mais elle note votre nom sur du vrai papier et vous dit de rappeler au printemps. Vous êtes dans la ville, et on s'y souvient de vous. (Fin neutre.)",
  "Hoy no hay puesto, pero anota tu nombre en papel de verdad y te dice que llames en primavera. Estás en la ciudad, y alguien te recuerda. (Final neutro.)",
  "Oggi niente posto, ma annota il tuo nome su carta vera e ti dice di richiamare in primavera. Sei in città, e qualcuno ti ricorda. (Finale neutro.)",
  "Heute keine Stelle, aber sie notiert Ihren Namen auf echtem Papier und sagt, Sie sollen im Frühling anrufen. Sie sind in der Stadt, und man kennt Sie. (Neutrales Ende.)",
  "Hoje não há vaga, mas ela anota o teu nome em papel a sério e diz para ligares na primavera. Estás na cidade, e alguém se lembra de ti. (Final neutro.)",
 ],
 38: [
  "Vous appelez Mme Rowe par son nom avant qu'elle ne se présente : elle comprend que vous êtes allé jusqu'à Rosewater Street. Elle vous embauche. (Fin secrète, bonne.)",
  "Llamas a la Sra. Rowe por su nombre antes de que se presente: entiende que llegaste hasta Rosewater Street. Te contrata. (Final secreto, bueno.)",
  "Chiami la signora Rowe per nome prima che si presenti: capisce che sei arrivato fino a Rosewater Street. Ti assume. (Finale segreto, buono.)",
  "Sie nennen Frau Rowe beim Namen, bevor sie sich vorstellt: sie versteht, dass Sie bis zur Rosewater Street gegangen sind. Sie stellt Sie ein. (Geheimes, gutes Ende.)",
  "Chamas a Sra. Rowe pelo nome antes de ela se apresentar: percebe que foste até Rosewater Street. Contrata-te. (Final secreto, bom.)",
 ],
 39: [
  "Le numéro de l'agence ne répond plus. Le bureau est vide, sans meubles. Vous n'avez ni argent ni travail : vous avez été escroqué. (Mauvaise fin.)",
  "El número de la agencia ya no responde. La oficina está vacía, sin muebles. No tienes ni dinero ni trabajo: te han estafado. (Final malo.)",
  "Il numero dell'agenzia non risponde più. L'ufficio è vuoto, senza mobili. Non hai né soldi né lavoro: sei stato truffato. (Finale cattivo.)",
  "Die Nummer der Agentur antwortet nicht mehr. Das Büro ist leer, ohne Möbel. Sie haben weder Geld noch Arbeit: Sie wurden betrogen. (Schlechtes Ende.)",
  "O número da agência já não atende. O escritório está vazio, sem móveis. Não tens dinheiro nem trabalho: foste enganado. (Final mau.)",
 ],
 40: [
  "Vous abandonnez et regardez le tableau des départs : un train à deux heures vous ramène d'où vous venez. (Mauvaise fin.)",
  "Te rindes y miras el panel de salidas: un tren a las dos te lleva de vuelta a casa. (Final malo.)",
  "Ti arrendi e guardi il tabellone delle partenze: un treno alle due ti riporta da dove sei venuto. (Finale cattivo.)",
  "Sie geben auf und schauen auf die Abfahrtstafel: ein Zug um zwei bringt Sie zurück, woher Sie kamen. (Schlechtes Ende.)",
  "Desistes e olhas para o painel das partidas: um comboio às duas leva-te de volta de onde vieste. (Final mau.)",
 ],
 44: [
  "L'homme du kiosque explique : la société a déménagé vers le fleuve il y a des années, mais les lettres partent toujours avec l'ancienne adresse. Ce détail est au cœur de l'histoire.",
  "El hombre del quiosco explica: la empresa se mudó al río hace años, pero las cartas siguen saliendo con la dirección antigua. Ese detalle es el centro de la historia.",
  "L'uomo dell'edicola spiega: l'azienda si è trasferita al fiume anni fa, ma le lettere partono ancora col vecchio indirizzo. Questo dettaglio è il cuore della storia.",
  "Der Mann am Kiosk erklärt: die Firma zog vor Jahren an den Fluss, aber die Briefe gehen noch mit der alten Adresse raus. Dieses Detail ist der Kern der Geschichte.",
  "O homem do quiosque explica: a empresa mudou-se para o rio há anos, mas as cartas ainda saem com a morada antiga. Esse detalhe é o centro da história.",
 ],
 63: [
  "À l'accueil, un plateau de courrier renvoyé : de vieilles lettres avec l'adresse de Rosewater Street barrée. L'une d'elles est la vôtre — celle qui vous a mené à la mauvaise porte.",
  "En recepción, una bandeja de correo devuelto: cartas viejas con la dirección de Rosewater Street tachada. Una es la tuya, la que te llevó a la puerta equivocada.",
  "Alla reception, un vassoio di posta rispedita: vecchie lettere con l'indirizzo di Rosewater Street cancellato. Una è la tua, quella che ti ha portato alla porta sbagliata.",
  "Am Empfang ein Tablett mit zurückgeschickter Post: alte Briefe mit durchgestrichener Rosewater-Street-Adresse. Einer ist Ihrer — der, der Sie zur falschen Tür führte.",
  "Na receção, um tabuleiro de correio devolvido: cartas velhas com a morada de Rosewater Street riscada. Uma é a tua, a que te levou à porta errada.",
 ],
 85: [
  "Le bureau de Mme Rowe donne sur l'eau. Sur la table, votre propre lettre, revenue à l'expéditeur. Elle voit que vous l'avez remarquée.",
  "El despacho de la Sra. Rowe da al agua. Sobre la mesa, tu propia carta, devuelta al remitente. Ella ve que te has dado cuenta.",
  "L'ufficio della signora Rowe dà sull'acqua. Sul tavolo, la tua stessa lettera, tornata al mittente. Lei vede che l'hai notata.",
  "Frau Rowes Büro liegt am Wasser. Auf dem Tisch Ihr eigener Brief, zurückgeschickt. Sie sieht, dass Sie ihn bemerkt haben.",
  "O gabinete da Sra. Rowe dá para a água. Na mesa, a tua própria carta, devolvida ao remetente. Ela vê que reparaste.",
 ],
 86: [
  "Elle explique que quelqu'un envoie l'ancienne adresse depuis deux ans ; vous n'êtes pas le premier égaré, mais le premier à être quand même venu.",
  "Explica que alguien lleva dos años enviando la dirección antigua; no eres el primero al que despistó, pero sí el primero en venir de todos modos.",
  "Spiega che qualcuno manda il vecchio indirizzo da due anni; non sei il primo a essere sviato, ma il primo a venire lo stesso.",
  "Sie erklärt, dass jemand seit zwei Jahren die alte Adresse verschickt; Sie sind nicht der erste Fehlgeleitete, aber der erste, der trotzdem kam.",
  "Explica que alguém envia a morada antiga há dois anos; não és o primeiro a ser desencaminhado, mas o primeiro a vir na mesma.",
 ],
 96: [
  "Dans la cour, un plateau d'enveloppes prêtes à poster — toutes adressées à Rosewater Street, c'est-à-dire à personne. Vous découvrez d'où vient l'erreur.",
  "En el patio, una bandeja de sobres listos para enviar, todos a Rosewater Street, es decir, a nadie. Descubres de dónde viene el error.",
  "Nel cortile, un vassoio di buste pronte da spedire, tutte indirizzate a Rosewater Street, cioè a nessuno. Scopri da dove nasce l'errore.",
  "Im Hof ein Tablett mit versandfertigen Umschlägen — alle an die Rosewater Street, also an niemanden. Sie entdecken, woher der Fehler kommt.",
  "No pátio, um tabuleiro de envelopes prontos a enviar, todos para Rosewater Street, ou seja, para ninguém. Descobres de onde vem o erro.",
 ],
 106: [
  "L'adresse donnée par l'agence n'est qu'un terrain vague derrière une clôture. Il n'y a jamais eu de travail : seulement les 200 envolés.",
  "La dirección que dio la agencia es solo un solar tras una valla. Nunca hubo trabajo: solo los 200 desaparecidos.",
  "L'indirizzo dato dall'agenzia è solo un terreno abbandonato dietro una recinzione. Non c'è mai stato lavoro: solo i 200 spariti.",
  "Die Adresse der Agentur ist nur ein leeres Grundstück hinter einem Zaun. Es gab nie Arbeit — nur die verschwundenen 200.",
  "A morada dada pela agência é só um terreno baldio atrás de uma vedação. Nunca houve trabalho: apenas os 200 desaparecidos.",
 ],
 120: [
  "Mme Rowe vous demande pourquoi elle devrait embaucher un inconnu arrivé presque par hasard. Elle attend votre réponse.",
  "La Sra. Rowe te pregunta por qué debería contratar a un desconocido que llegó casi por casualidad. Espera tu respuesta.",
  "La signora Rowe ti chiede perché dovrebbe assumere uno sconosciuto arrivato quasi per caso. Aspetta la tua risposta.",
  "Frau Rowe fragt, warum sie einen Fremden einstellen sollte, der fast zufällig kam. Sie wartet auf Ihre Antwort.",
  "A Sra. Rowe pergunta por que deveria contratar um desconhecido que chegou quase por acaso. Espera a tua resposta.",
 ],
 121: [
  "Vous lui parlez de l'agence qui a failli vous prendre 200. Elle vous dit que vous avez eu raison de partir.",
  "Le hablas de la agencia que casi te quita 200. Te dice que hiciste bien en marcharte.",
  "Le parli dell'agenzia che stava per prenderti 200. Ti dice che hai fatto bene ad andartene.",
  "Sie erzählen ihr von der Agentur, die Ihnen fast 200 abgenommen hätte. Sie sagt, Sie hätten richtig gehandelt, zu gehen.",
  "Falas-lhe da agência que quase te tirou 200. Ela diz que fizeste bem em ir embora.",
 ],
 141: [
  "Vous répondez simplement, sans faire semblant. Cela suffit : « Commencez lundi. » Un travail honnêtement gagné. (Bonne fin.)",
  "Respondes con sencillez, sin fingir. Basta con eso: «Empieza el lunes». Un trabajo ganado con honestidad. (Final bueno.)",
  "Rispondi con semplicità, senza fingere. Basta così: «Inizi lunedì». Un lavoro guadagnato onestamente. (Finale buono.)",
  "Sie antworten schlicht, ohne sich zu verstellen. Das genügt: „Fangen Sie Montag an.“ Ehrlich verdiente Arbeit. (Gutes Ende.)",
  "Respondes com simplicidade, sem fingir. Basta: «Começa segunda-feira». Um trabalho ganho com honestidade. (Final bom.)",
 ],
 142: [
  "Vous entrez reposé et sans rien devoir à ceux qui voulaient vous vendre de l'espoir — et cela se voit. Elle vous embauche. (Bonne fin, secrète.)",
  "Entras descansado y sin deberle nada a quienes querían venderte esperanza, y se nota. Te contrata. (Final bueno, secreto.)",
  "Entri riposato e senza dover nulla a chi voleva venderti speranza, e si vede. Ti assume. (Finale buono, segreto.)",
  "Sie treten ausgeruht ein und schulden niemandem etwas, der Ihnen Hoffnung verkaufen wollte — man sieht es. Sie stellt Sie ein. (Gutes, geheimes Ende.)",
  "Entras descansado e sem dever nada a quem queria vender-te esperança, e nota-se. Contrata-te. (Final bom, secreto.)",
 ],
 143: [
  "Pas de travail, mais elle écrit votre nom à la main. Vous êtes dans la ville, et on s'y souvient de vous. (Fin neutre.)",
  "No hay trabajo, pero anota tu nombre a mano. Estás en la ciudad, y alguien te recuerda. (Final neutro.)",
  "Niente lavoro, ma scrive il tuo nome a mano. Sei in città, e qualcuno ti ricorda. (Finale neutro.)",
  "Keine Arbeit, aber sie schreibt Ihren Namen von Hand auf. Sie sind in der Stadt, und man erinnert sich an Sie. (Neutrales Ende.)",
  "Não há trabalho, mas ela escreve o teu nome à mão. Estás na cidade, e alguém se lembra de ti. (Final neutro.)",
 ],
 144: [
  "Tout se passe vite, on vous embauche avant midi — mais personne ne demande ce que la nuit vous a coûté, et vous ne ressentez rien. (Fin neutre, amère.)",
  "Todo va rápido, te contratan antes del mediodía, pero nadie pregunta qué te costó la noche, y no sientes nada. (Final neutro, amargo.)",
  "Tutto va veloce, ti assumono prima di mezzogiorno, ma nessuno chiede cosa ti è costata la notte, e non provi nulla. (Finale neutro, amaro.)",
  "Alles geht schnell, man stellt Sie vor Mittag ein — aber niemand fragt, was die Nacht Sie gekostet hat, und Sie fühlen nichts. (Neutrales, bitteres Ende.)",
  "Tudo corre depressa, contratam-te antes do meio-dia, mas ninguém pergunta o que a noite te custou, e não sentes nada. (Final neutro, amargo.)",
 ],
 145: [
  "Pas de travail, mais l'homme du banc, que vous avez aidé, vous offre une chambre et une clé. Vous n'êtes pas embauché, mais plus seul. (Fin neutre.)",
  "No hay trabajo, pero el hombre del banco, al que ayudaste, te ofrece un cuarto y una llave. No te contratan, pero ya no estás solo. (Final neutro.)",
  "Niente lavoro, ma l'uomo della panchina, che hai aiutato, ti offre una stanza e una chiave. Non sei assunto, ma non più solo. (Finale neutro.)",
  "Keine Arbeit, aber der Mann von der Bank, dem Sie geholfen haben, bietet Ihnen ein Zimmer und einen Schlüssel. Nicht eingestellt, aber nicht mehr allein. (Neutrales Ende.)",
  "Não há trabalho, mas o homem do banco, que ajudaste, oferece-te um quarto e uma chave. Não és contratado, mas já não estás sozinho. (Final neutro.)",
 ],
 146: [
  "Vous arrivez à neuf heures vingt : le carnet de rendez-vous est fermé, les chaises pleines. On vous dit gentiment non. (Mauvaise fin.)",
  "Llegas a las nueve y veinte: la agenda está cerrada, las sillas llenas. Te dicen que no con amabilidad. (Final malo.)",
  "Arrivi alle nove e venti: l'agenda è chiusa, le sedie piene. Ti dicono gentilmente di no. (Finale cattivo.)",
  "Sie kommen um zwanzig nach neun: der Terminkalender ist zu, die Stühle besetzt. Man sagt freundlich Nein. (Schlechtes Ende.)",
  "Chegas às nove e vinte: a agenda está fechada, as cadeiras cheias. Dizem-te que não com gentileza. (Final mau.)",
 ],
 147: [
  "Le matin se lève sur le banc et vous ne bougez pas. Quand vous reprenez vos esprits, neuf heures sont passées — et la raison de votre venue aussi. (Mauvaise fin.)",
  "Amanece sobre el banco y no te mueves. Cuando reaccionas, ya han pasado las nueve, y con ellas el motivo de tu viaje. (Final malo.)",
  "Sorge il mattino sulla panchina e non ti muovi. Quando ti riprendi, le nove sono passate, e con esse il motivo del tuo viaggio. (Finale cattivo.)",
  "Der Morgen graut über der Bank, und Sie rühren sich nicht. Als Sie zu sich kommen, ist neun Uhr vorbei — und damit der Grund Ihrer Reise. (Schlechtes Ende.)",
  "O dia nasce sobre o banco e não te mexes. Quando dás por ti, passaram das nove — e com elas a razão da tua viagem. (Final mau.)",
 ],
}

for i, code in enumerate(L):
    data = {str(nid): tr[i] for nid, tr in G.items()}
    json.dump(data, open(os.path.join(OUT, f"{code}.json"), "w", encoding="utf-8"),
              ensure_ascii=False, separators=(",", ":"), sort_keys=True)
print(f"Gists: {len(G)} passages × {len(L)} languages → content/gist/<lang>.json "
      "(ru/ar/zh left for native translators)")
