## Problème :

On est 5 en gros, y'a en général 2 khôlles de maths, 2 khôlles de physique. Sachant que certaines personnes voudront pas faire de khôlles de physique, je propose qu'on décide les khôlles de physique simplement le WE avant.
Pour les maths : 

- Pour les profs demandés, genre Bruiltet/Molin, on décide à l'avance (genre chacun choisit un créneau dans l'année à son tour, et à la fin on a tous à peu près le bon nombre de khôlles).

- Pour les autres profs, le WE on doit décider qui passe la ou les deux khôlles de maths. Je pense que le système de crédit d'Emre est une bonne idée, mais je pense que ça va être difficile dans le sens où ça va toujours se jouer à quelques points près, donc on va souvent recourir à l'ordre alphabétique.

Par exemple, si X et Y passent semaine 1, ils auront chacun 1 point, donc la semaine suivante, ils ne passeront pas. Pour que tout le monde passe, il faudra donc attendre 3 semaines. Mais si A et B sont d'accord pour ne pas passer semaine 2, et que X et Y prennent leur place, alors X et Y auront 2 points chacun, et devront donc attendre 3 semaine avant de pouvoir squatter une khôlle.

## Solution :

Alors, à la place de faire un système simple de points j'ai cherché une formule sympa

$f : \mathbb{N} \times \llbracket 1, 15 \rrbracket \longrightarrow \mathbb{R}$

$f : (n, s) \longmapsto \sum_{i=0}^{s} \left(e^{\frac{2n-5}{10}} - e^{\frac{-5}{10}}\right)$

Avec : 

- $n$ le nombre de khôlles faites au moment du calcul

- $s$ : la s-ième semaine

- $2$ : le nombre de khôlles disponibles par semaine : on le fixe à 2 si on fait le calcul pour les maths, à 3 ou 4 si ça prend en compte la physique.

- $5$ : combien on est. Si y'a qqun qui s'incruste, on le monte à 6, et on divise par 12. 

J'ai laissé une fonction croissante : plus on a de points, plus on est désaventagé. On peut changer la formule pour faire en sorte que plus on a de points, plus on a une chance de passer.

## Par exemple :

- Semaine 3 : 
  
  - 1 khôlle : 4 points
  
  - 2 khôlles : 4.5 points
  
  - 3 khôlles : 5 points
  
  - 4 et + : 6 points et +

- Semaine 7 : 
  
  - 3 khôlles : 12 points
  
  - 4 khôlles : 13.6 points
  
  - 5 khôlles : 15.7 points
  
  - 7 khôlles : 21 points

## Aventages :

- Elle donne directement le nombre de points avec un simple calcul (mental)

- Elle gère le problème des points mal répartis au fil des 15 semaines

- Elle désaventages les personnes qui ont fait plus d'une khôlle par semaine

- Elle donne une utilité concrète en plus aux maths de prépa

## Désaventages :

- Même problème pour les deux premières semaines que le système de points linéaire
