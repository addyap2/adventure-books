#!/usr/bin/env python3
"""Extend The Orchard's French gist to full per-passage coverage.
Merges into content/gist/the-orchard/fr.json, keeping existing entries and adding the rest.
French-first; native review: complete. Run: python3 scripts/build_gist_fr_full_ep06.py
"""
import json, os
SLUG = "the-orchard"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "gist", SLUG, "fr.json")

FR = {
 2: "Vous rassemblez ce que l'abri contient : un bidon d'huile, des allumettes, une bonne lanterne, une brassée de paille sèche. Dehors, l'air est parfaitement immobile et d'un froid mordant. Le givre rampe déjà, blanc, sur l'herbe. Il faut décider quoi faire, et vite.",
 3: "Vous essayez le téléphone. Il sonne, sonne, puis enfin la voix de Tom passe depuis la coopérative. Aucune équipe ne peut venir avant le matin, dit-il — pas par un gel pareil. Allume les feux le long des rangs, vous dit-il, et tiens-les si tu le peux.",
 4: "Vous rejoignez Edith au pied des marches et l'installez aussi au chaud que possible. Mais les rangs sont encore noirs et froids. L'abri seul ne suffit pas. Les fleurs là-dehors ont besoin des feux allumés. Il faut de l'huile, un plan, et la tête froide avant d'aller parmi les arbres.",
 5: "Vous sortez parmi les rangs. La nuit est immense et parfaitement immobile, et les fleurs pâles semblent luire dans le noir. Le froid pèse sur tout le verger comme une main. Puis, loin, parmi les arbres du bout, vous la saisissez : une petite lumière qui bouge, là où personne ne devrait être cette nuit.",
 6: "Vous vous forcez à vous arrêter et à réfléchir. Allumer d'abord les feux, et voir le reste après. Ou aller vers Edith et les voisins. Ou ameuter le village pour avoir plus de bras. Chaque choix coûte un temps que vous n'avez pas — et dans le noir, le gel travaille déjà les arbres.",
 8: "Le froid s'installe dans votre poitrine comme un poids. Vous pensez aux fleurs là-dehors : une année entière de fruits, le verger qui est tout ce qui reste à Edith. Si les feux restent éteints trop longtemps, le gel prend tout d'ici l'aube. Ce n'est pas une peur, c'est un fait. Personne d'autre ne viendra. Ce sera vous, cette nuit, ou personne.",
 11: "Vous sortez droit aux rangs et allumez ce que vous pouvez. Une allumette, une flambée de paille, un pot qui prend çà et là. Mais les flammes sont minces et basses. Sans vraie huile, elles ne tiendront pas une heure. Vous ne pouvez pas juste les allumer, partir et espérer.",
 13: "Vous prenez vous-même en charge l'huile et la paille. Le fût est lourd, et chaque goutte compte désormais. Entretenue avec soin, elle gardera les feux allumés toute la nuit le long des rangs ; gaspillée, et les fleurs gèlent avant l'aube. Alors vous la serrez contre vous et partez vers les arbres.",
 14: "Vous ne prenez qu'une lanterne et un fagot de petit bois. Ils vous donnent de quoi voir et de quoi lancer une flamme. Mais pas les feux eux-mêmes. Et vous n'avez mis aucune vraie huile de côté. Il vous faudra quand même de l'huile, et vite. Sinon, les rangs restent noirs et le gel gagne.",
 15: "Le vieux Jack Hale connaît ce verger dans le noir mieux que personne. « Reste loin de l'étang gelé, dit-il. Ça ressemble à un raccourci. Ça n'en est pas un — c'est une noyade. » Il vous met aussi en garde contre l'acheteur, cet homme souriant de la société. « Surveille ton huile, tiens les feux — c'est tout le travail de cette nuit. »",
 16: "Vous allumez le poêle de M. Hollis et l'installez auprès avec une couverture. Peu à peu, ses tremblements s'apaisent. « Que Dieu te bénisse », dit-il en vous serrant fort la main. Vous promettez de repasser avant le matin. Puis vous ressortez dans le gel et les rangs qui attendent.",
 17: "Tenir les feux passe d'abord. Le reste peut attendre un instant. Mais il faut encore choisir comment. Prendre d'abord de la vraie huile au magasin. Ou aller droit aux rangs et commencer.",
 18: "Le travail vous épuise. Vos jambes brûlent, votre poitrine halète, et le froid lutte contre vous à chaque pas. Vous êtes près de votre limite, et vous le savez. Si vous tombez ici, il ne reste personne pour tenir les feux. Alors allez lentement, et avec soin.",
 19: "Le village se réveille à lui-même, et les gens se mettent à bouger. Un homme roule un fût d'huile. Une femme tire du bois sec. Porte après porte, un plan prend forme. Vous n'êtes plus seul là-dedans. Et cela change tout.",
 20: "Personne ne bouge. Les portes restent closes, et les visages se détournent des fenêtres. Ils ont peur, et les gens effrayés se taisent. Vous ne pouvez pas les forcer à aider. Alors vous vous détournez et continuez seul. C'est plus dur ainsi. Mais les fleurs ne peuvent pas attendre.",
 21: "Les feux proches brûlent. Maintenant, les rangs du bout. Deux chemins pour y descendre. La longue allée qui contourne est sûre mais lente. L'étang gelé est rapide, tout droit. Mais par un gel pareil, la glace pourrait tuer.",
 22: "Vous prenez à cœur les mots de Jack Hale. Surveiller l'huile avec soin. Bien éviter l'étang gelé. Ne pas faire confiance à l'acheteur. Et tenir les feux avant tout. Un conseil simple, et bon. Reste à le suivre.",
 23: "Vous vous sentez plus ferme après ce bon geste. Aider quelqu'un semble, curieusement, vous affermir aussi. La tête plus claire, les mains plus sûres. Il reste une nuit dure à passer. Mais vous vous sentez de taille.",
 24: "Un homme se tient dans l'allée, une lanterne au poing — l'acheteur. Il a de l'huile à vendre et des bras à prêter, et il sourit trop facilement. « Le verger, ce n'est pas vraiment ton affaire ce soir, l'ami », dit-il. Vous avez déjà croisé son genre.",
 25: "Vous menez une petite bande vers les feux. À marcher ensemble, tous se sentent plus forts. Ils portent huile, bois et paille. « Par ici ! » criez-vous dans le froid, et ils suivent. Un bon sentiment, dans une heure dure.",
 26: "L'allée est noire et dure, le froid y pesant, pas d'abri nulle part. Mais elle est ferme sous les pieds, et elle mène où il faut aller. Alors vous continuez de marcher, pas après pas.",
 28: "Vous posez le pied sur la glace, et aussitôt cela sonne faux. L'eau attend dessous, noire, profonde et glacée. Chaque pas est un pari désormais — et vous y êtes, seul. Plus de retour possible une fois la traversée commencée.",
 29: "La paille est humide et ne prend pas. Elle ne donne qu'une flamme basse et vacillante. Peu utile par un gel pareil. Il faudra faire avec. Ou retourner au magasin chercher de la paille sèche.",
 30: "L'allée court le long des rangs, le froid s'approfondissant d'heure en heure. En contrebas, une chaumière sombre, sans feu. Devant, l'air immobile et dur semble vous repousser. Et il y a un piquet de rang, à moitié tombé dans le gel.",
 31: "Un vieil homme est tombé sur l'allée gelée et ne peut se relever. Le froid le gagne déjà. Vous arrêter, c'est perdre un temps que vous n'avez pas. Ne pas le faire, c'est risquer qu'il ne passe pas l'heure.",
 33: "Vous poussez à travers le pire du froid, chaque pas un combat, le gel cinglant votre visage. Des choix devant vous. L'acheteur est peut-être proche. Il y a cette étrange lumière dans les arbres du bout. Ou vous pouvez simplement foncer vers les rangs.",
 34: "Vous remettez le vieil homme debout et le réchauffez du mieux possible. Ses yeux s'emplissent, et il vous presse un sac sec dans les mains. « Prends-le, dit-il, pour ta peine. » Peu de chose — mais donné de bon cœur, et vous le prenez et repartez.",
 35: "Vous ne pouvez pas rester — mais vous ne pouvez pas non plus les laisser. Alors vous promettez d'envoyer vite de l'aide. « Tenez bon ! criez-vous. Restez au chaud, restez ensemble — je ne vous oublierai pas. » Et vous le pensez. Puis vous tournez les talons et partez.",
 36: "Le village allume un grand feu parmi les rangs — un fût en flammes, jetant lumière et chaleur dans le gel. Les gens s'y pressent, les vieux et les faibles au plus près. Ce n'est pas tout le verger sauvé. Mais c'est une vraie chaleur, et un début.",
 37: "Chaumière après chaumière, le village effrayé devient un village qui travaille. Chacun a sa tâche : l'un entretient le feu, l'un porte la paille, l'un surveille les rangs. La peur devient action. Et l'action vaut mieux que l'attente, à tous les coups.",
 38: "Le long froid ronge votre volonté. Une petite voix dit : arrête, rentre, repose-toi — personne ne t'en voudrait, et ce serait si facile. Mais vous pensez aux fleurs là-dehors sur les arbres. Et vous repoussez la voix. Pas encore. Pas tant qu'on peut encore les sauver.",
 39: "Vous atteignez le vieux piquet de rang, mais le gel l'a fendu et à moitié renversé. À peine lisible, à présent. Un bras indique les rangs. L'autre les arbres du bout. Quel chemin ? Il faudra deviner, et bien deviner.",
 42: "Vous lui tournez le dos et le laissez à son commerce glacé. Ça fait du bien de partir. Il vous hèle, mais vous ne vous retournez pas. Son genre trouve toujours quelqu'un, à la fin. Mais pas vous, pas cette nuit.",
 43: "Vous prenez son huile et son argent. Vos mains se referment dessus, et quelque chose en vous sait déjà. Son sourire s'élargit. « Sage », dit-il. Mais cela n'a rien de sage. Cela ressemble à une porte qui se ferme en silence.",
 44: "Vous demandez franchement : que veut-il vraiment, et pourquoi le verger devrait-il périr ? Il sourit et regarde au loin dans l'allée. « La terre se vend à bas prix après une mauvaise année, dit-il. Un gel pareil, c'est une aubaine — pour un acheteur comme moi. »",
 45: "Vous portez son huile aux pots. Mais en la versant, la flamme étouffe et crache. L'huile est fluette, coupée d'eau — elle ne nourrit pas le feu. Les flammes retombent, basses, brunes et inutiles.",
 46: "Vous ouvrez le bidon, et l'odeur vous saisit — fluette, aigre, coupée d'eau. Cette huile ne nourrira jamais de flamme. Vous l'avez payée cher, et elle ne vaut rien. Le doute dans votre ventre avait raison depuis le début.",
 47: "Vous le cherchez, mais la lanterne de l'acheteur est déjà partie, au bout de l'allée. Il ne vous aidait pas du tout. Il attendait le gel, la récolte perdue, la terre à bas prix ensuite. Vous avez été dupé, tout simplement.",
 48: "Il est parti, et l'allée est vide — rien que le froid, le noir, et ce que vous lui avez donné pour rien. Vous avez appris une dure leçon cette nuit. Et vous l'avez payée bien trop cher. Vous continuez avec moins qu'au départ.",
 49: "Les gens effrayés lui fourrent leurs pièces. Des mains pleines d'argent, des voix suppliant pour de l'huile. Il prend, lentement, avec ce même sourire. Il choisit qui aider selon qui peut payer le plus.",
 50: "Loin sur la glace, les rangs du bout paraissent enfin plus proches — ou pas ? Vous n'en êtes plus sûr. Le noir trompe, et vos yeux fatigués aussi. Et vous voilà loin de l'une comme de l'autre rive.",
 51: "La glace, le noir, l'eau profonde en dessous — et une fissure part de sous votre pied. C'est le moment. Vous pouvez sombrer dans l'eau glacée. Ou vous rejeter en arrière, loin de la fissure, tant que vous le pouvez.",
 52: "Vous atteignez enfin les rangs du bout, trempé et tremblant, les mains écorchées — mais de l'autre côté. D'une façon ou d'une autre, vous avez réussi. Maintenant il faut décider : continuer, épuisé comme vous êtes, ou affronter ce que vous avez perdu sur la glace.",
 53: "Vous vous rejetez loin de la fissure tant que vous le pouvez — le choix dur et juste. Vous rampez le dernier bout à quatre pattes, et atteignez la rive, secoué et lent. La nuit n'est pas perdue. Mais cela vous a coûté un temps qui vous manquera.",
 54: "Vous tentez d'allumer leur poêle et de boucher le pire des courants d'air avec des sacs et un vieux coffre. Cela retient un peu de froid. Mais il n'y a toujours pas de lampe à leur laisser, et la nuit est loin d'être finie.",
 55: "Vous donnez votre propre manteau et votre lampe, et la famille se blottit autour de la petite flamme, le soulagement passant sur leurs visages. L'enfant cesse enfin de pleurer. « Merci », dit la mère — puis elle vous montre une lumière, là-bas parmi les arbres du bout.",
 56: "Sans votre manteau, le froid et l'humidité vous trouvent vite — dents qui claquent, doigts qui se raidissent. Vous l'avez donné pour aider, et vous recommenceriez. Mais le gel se moque de tout cela. Il mord plus fort, c'est tout.",
 57: "Un inconnu vous fait entrer dans une porte éclairée. « Juste une minute, dit-il. Hors du froid — reprends ton souffle. » C'est chaud et sec, et tout votre corps vous supplie de rester. Mais une minute pareille peut glisser, sans bruit, vers une heure.",
 58: "Vous avancez dans le gel, glacé jusqu'aux os, le froid luttant à chaque pas, les yeux larmoyants et piquants. Chaque pas est un petit combat à lui seul. Mais vous les enchaînez, l'un après l'autre, vers les rangs.",
 60: "Quelqu'un montre les arbres du bout : une silhouette est partie par là, seule, dans le froid et le noir. Là-bas il n'y a que le gel et le sol bas qui tue. Si personne ne la suit, elle pourrait ne pas revenir.",
 61: "Vous la trouvez parmi les arbres du bout, à moitié gelée et perdue, le froid la déchirant. Elle ne semble pas du tout reconnaître votre visage. Vous lui saisissez fermement le bras. « Viens avec moi, dites-vous. Tout va bien maintenant. Je te tiens. »",
 62: "Vous ne pouvez pas tout faire à la fois, et les feux ont le plus besoin de vous. Alors vous faites prévenir quelqu'un d'autre pour elle, et vous continuez. Cela vous pèse — mais cette nuit, il faut choisir, et choisir encore.",
 63: "Vous les ramenez sains et saufs aux chaumières, où leur famille crie de soulagement. On vous enveloppe d'un manteau sec et on vous fait une place près du feu. « Merci », répètent-ils. Mais les rangs attendent, et vous ne pouvez pas rester longtemps.",
 64: "Vous regardez tout le verger — tout blanc, tout immobile. Les fleurs luisent, pâles et fragiles, dans le noir. Nulle lumière ne paraît, sinon là-bas parmi les arbres du bout. Tout le verger semble retenir son souffle et attendre l'aube.",
 65: "Le froid s'approfondit à son pire désormais. Le thermomètre descend aussi bas qu'il le peut, et votre souffle fait de la buée dans l'air immobile. Dur de penser, dur de bouger, dur de s'en soucier. C'est l'heure la plus dure de toute la nuit.",
 67: "Tom vous presse la dernière lanterne sèche. « Pour les rangs, dit-il. Vas-y — je reste ici près du téléphone. » Son visage est gris d'inquiétude. C'est l'aide qu'il peut donner cette nuit, et il la donne tout entière, de bon cœur.",
 68: "Au magasin de carburant, on se rue sur les bidons — voix qui montent, mains qui saisissent, la peur qui prend et se répand vite. Une bousculade de plus et c'est la bagarre. Vous pouvez tenter de les calmer et partager l'huile équitablement. Ou simplement prendre la vôtre et filer.",
 70: "Loin parmi les arbres du bout, une petite lumière monte et s'éteint. C'est là où personne ne devrait être cette nuit — paraissant, disparaissant, reparaissant. Personne ne sait l'expliquer. Et quelque chose en vous veut aller y répondre.",
 71: "Vous gagnez les arbres du bout et appelez dans le noir. Nulle réponse que le froid. Puis vous la voyez : une petite forme, parmi les arbres, à demi cachée dans le givre blanc. Quelqu'un est là-dehors, après tout. Et il bouge à peine.",
 72: "Vous l'atteignez, et le cœur vous chavire. C'est un enfant — Wren — recroquevillé dans le gel, à moitié gelé et à peine éveillé. Le froid le tient. Pas le temps de s'arrêter pour réfléchir. Il faut agir, maintenant.",
 73: "Vous rappelez dans le noir, et un instant, rien. Puis une voix frêle répond, déchirée par le froid : « Ici ! Par ici ! » Quelqu'un est parmi les arbres, et a besoin d'aide. Et sa voix n'a rien de fort.",
 74: "Vous sortez Wren du gel et l'enveloppez bien dans votre manteau. Lentement il revient, vous agrippant le bras. « Les feux, souffle-t-il. Garde les feux allumés. Les fleurs… » Même à moitié gelé, il pense au verger.",
 75: "Vous vous retournez pour courir chercher de l'aide — puis vous vous arrêtez net. Il n'y a pas d'aide ici, pas avant le matin. Pas d'équipe, pas de voisins, personne qui vienne. C'est vous ou personne, et Wren le sait aussi. Ses yeux effrayés vous suivent dans le noir.",
 76: "Wren lève les yeux, plus clairs à présent. « La cultivatrice, Edith — c'est ma grand-mère, dit-il. On ne s'est pas parlé depuis des années. Pas depuis que mon père et elle se sont brouillés. C'est une longue et triste histoire. » Et vous entendez à quel point elle est longue.",
 77: "Vous décidez de les mettre face à face avant la fin de la nuit — Wren et la vieille Edith, après toutes ces années. C'est peu de chose, à côté des feux et du gel. Mais ce n'est pas rien. Certaines portes closes peuvent encore s'ouvrir.",
 78: "La petite forme ne bouge pas, et le gel travaille dessus, froid et patient. Et pourtant quelqu'un est venu jusqu'ici, dans le noir, seul. Vous ne pouvez pas le laisser là, étendu. Il faut approcher et savoir qui c'est.",
 79: "Vous approchez, et vous le reconnaissez aussitôt. C'est Wren — le petit-enfant de la vieille Edith, qu'on n'a pas vu ici depuis des années, depuis la brouille de la famille. Puis un bruit faible monte du gel à vos pieds. Vous agissez vite, maintenant.",
 80: "L'acheteur revient une dernière fois, sa lanterne oscillant. « Tu te bats encore ? dit-il. Laisse le gel l'emporter. Dernière chance d'être du côté des gagnants, l'ami. » Le même sourire facile. Le même vieux mensonge.",
 90: "Vous revoilà au verger, glacé jusqu'aux os, le plus dur froid de la nuit pesant sur tout. Près des marches de derrière, Edith gît, grise et immobile. Dans les rangs, les feux brûlent bas. C'est l'heure où bascule toute la nuit.",
 91: "Vous atteignez les feux : les flammes basses, les pots du bout éteints. Parmi les rangs du bout, le gel est tout près de prendre les fleurs pour de bon. Il faut rendre les feux pleins et ardents de nouveau — et il faut le faire maintenant, vite.",
 92: "Puis l'aide vous atteint enfin — plus de bras, plus d'huile, des gens fermes qui connaissent le travail. Vous n'êtes plus seul avec ça ; d'autres sont là pour partager le poids. C'est comme poser quelque chose de lourd que vous portiez depuis bien trop longtemps.",
 93: "Maintenant, tenir les feux — et ce que vous pouvez faire dépend de ce que vous avez porté ici. Avec de la vraie huile, vous avez de quoi faire. Sans elle, il faut coaxer chaque dernière lueur de flamme. Dans tous les cas, la nuit est loin d'être finie.",
 94: "Vous descendez voir Edith, et ses yeux s'entrouvrent. De la peur dedans — puis, en voyant votre visage, un peu moins de peur. « Tu les as gardés allumés », souffle-t-elle. « C'est fait, lui dites-vous doucement. Repose-toi maintenant. »",
 95: "L'huile fait tout. Vous alimentez et attisez les pots, et un à un les feux montent, pleins et dorés, tout le long des rangs. Une lumière chaude repoussant tout ce froid. Voilà, pensez-vous, à quoi a servi toute cette dure nuit.",
 96: "Vous n'avez pas de vraie huile à verser, alors vous coaxez le peu de flamme qui reste. Vous la protégez du courant d'air de votre corps, la nourrissant de bribes, de souffle, de pure volonté. Elle brûle, basse et mince. Ce ne sera peut-être pas assez. Mais vous ne la laisserez pas mourir sans vous battre.",
 97: "La flamme est basse et faiblit, et vous craignez que la protéger seule ne suffise pas. Vous avez fait tout ce que vous pouviez. Mais cela pourrait ne pas tenir. Il faut plus, maintenant — plus d'huile, plus de bras, ou les deux.",
 98: "Vous levez les yeux et la voyez. Loin parmi les arbres du bout, une lumière flambe et retombe — là où personne ne devrait être, paraissant et disparaissant. Elle tire votre œil. Et elle tire quelque chose de plus profond.",
 99: "La lumière parmi les arbres reparaît — là où tous jurent que personne ne serait. Mais une lumière veut dire une main pour l'allumer, et une main une personne. Une personne là-bas, seule, par un froid pareil.",
 100: "Vient maintenant la longue veille : vous alimentez les feux, gardez Edith au chaud, et surveillez le froid, heure après heure. Ce n'est pas palpitant — juste un travail régulier, dur, soigneux. Mais c'est tout le travail de cette nuit, et il est à vous.",
 101: "Et puis, enfin, ça bascule. Le froid desserre un peu son étreinte. Le ciel grisonne au bord de la crête, et la première lumière mince monte. Le gel perd. Vous avez presque tenu toute la nuit.",
 102: "C'est l'heure la pire, juste avant la rupture. Le froid n'a pas encore faibli ; vos bras souffrent, vos yeux brûlent. Mais vous sentez la nuit commencer à tourner, quelque part là-dessous. Tenez encore un peu.",
 103: "Le long des rangs, vous les voyez — des lanternes, des silhouettes sombres, des feux brûlant bas contre le gel. D'autres gens, dans le froid avec vous. Le village a passé cette nuit, lui aussi. Vous n'étiez jamais tout à fait aussi seul que vous le sentiez.",
 104: "Enfin, de l'aide remonte l'allée — un camion, plus de bras, plus d'huile, de la vraie aide à vraie allure. Vous vous appuyez à un arbre et la regardez venir, les jambes tremblantes à présent. Mais le pire de la nuit est derrière vous.",
 105: "L'aube se lève sur le verger, la lumière virant au gris, puis au pâle et au net. Le soleil grimpe la crête, et le gel lâche prise. Les fleurs sont toujours là, sur les arbres. Le pire est passé, enfin.",
 106: "Puis cela vient — le premier oiseau du matin, chantant au-dessus des arbres comme s'il n'y avait jamais eu de gel. Après la nuit que vous avez eue, cela paraît presque absurde. Et c'est beau, et vous vous arrêtez pour l'écouter.",
 107: "Du verger, vous guettez les arbres du bout, où une lumière monte et descend et grandit peu à peu. Quelque chose vient enfin, encore trop loin pour qu'on voie. Mais une lumière veut dire quelqu'un là-bas — et quelqu'un vaut bien mieux que personne cette nuit.",
 110: "La première lumière arrive enfin, et la nuit s'additionne en ce qu'elle est. Tout ce que vous avez fait là-dehors dans le froid vous revient — de quoi être fier, et de quoi l'être moins. Voyons, donc, à quoi tout cela a abouti.",
 111: "La nuit s'additionne — pas toujours par un grand acte, mais par beaucoup de petits. Ce que vous avez gardé, ce que vous avez refusé, pour qui vous êtes sorti dans le froid. Tout compte au bout du compte. Tout a fait la nuit telle qu'elle fut.",
 112: "Il y a plus à peser ; la nuit a tenu d'autres choses. Un inconnu pour qui vous vous êtes arrêté. Un manteau et une lampe donnés d'une main ouverte. De petits choix, faits dans le froid, quand il aurait été plus facile de passer son chemin.",
 113: "Et que vous laisse la nuit ? Peut-être pas une victoire nette. Peut-être juste le fait d'être sorti, d'avoir essayé. Quand c'était noir, froid et facile de barrer la porte, vous ne l'avez pas fait. Cela compte pour quelque chose.",
 114: "Mais toutes les nuits ne finissent pas bien. Certains choix coûtent plus qu'on ne le croyait alors ; certaines portes, une fois ouvertes, ne se referment pas. C'est la dure fin de la nuit — le lieu où le pire revient.",
}


def main():
    data = json.load(open(OUT, encoding="utf-8"))
    added = 0
    for nid, text in FR.items():
        k = str(nid)
        if k not in data:
            data[k] = text; added += 1
    data = {k: data[k] for k in sorted(data, key=lambda x: int(x))}
    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{SLUG}/fr.json: {len(data)} passages total (+{added} added)")


if __name__ == "__main__":
    main()
