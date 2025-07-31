# pythonday04
Ce lab m'a permis majoritairement à comprendre l'importance des **modules** dans l'organisation d'un projet informatique.
Ce read_me va porter majoritairement alors sur l'imporatnce des **modules/namespace** et ce qui les rends meilleures face à l'utilisation des inners classes.
## Modules
# Avantages
- Lisibilité (Tu sépares ton code dans plusieurs fichiers : plus propre et clair.)
- Réutilisable (Tu peux importer tes modules n’importe où dans d'autres projets.)
- Organisation logique (Facilite les gros projets avec plusieurs parties bien distinctes.)
- Facile à tester (Chaque module peut être testé indépendamment.)
- Evite les gros fichiers (Tu divises le code en plusieurs petits blocs logiques.)

# Inconvenients
- Plus de fichiers = plus de gestion
- Mauvais découpage = confusion

## Inner classes
# Avantages
- Code groupé (Tu montres clairement que la classe interne est liée à la classe externe.)
- Utilisation très locale (Idéal si la classe interne est uniquement utilisée par la classe externe.)
- Encapsulation logique (Tu caches les détails internes si besoin)

# Inconvenients
- Moins lisible
- Pas très flexible 
- Noms plus longs
- Peu utilisé en Python

## Conclusion
Utiliser des **modules** en Python permet de mieux organiser le code en le divisant en blocs logiques, faciles à maintenir.
Cela améliore la **lisibilité**, **facilite la réutilisation** et **rend les projets plus scalables**.
Les modules évitent les fichiers trop longs et encouragent un travail collaboratif propre.
Contrairement aux inner classes, ils offrent plus de clarté et de flexibilité.
C’est une pratique essentielle pour tout projet structuré et professionnel.