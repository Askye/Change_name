# Change_name
Changer le nom de plusieurs épisodes d'une série automatiquement

Format : change_name([Chemin d'acces], [nouveau nom], saison = [Numero de la saison] , debut = [numero du 1er épisode])


Exemple : <br/>
change_name("/mnt/d/'Shingeki No Kyojin'/'Shingeki test'/", "Shingeki No Kyojin", saison = 3, debut = 5)

Resulat : 
<ul>
        <li>Shingeki No Kyojin S03E05</li>
        <li>Shingeki No Kyojin S03E06</li>
        <li>...</li>
</ul>
-------------------------- <br/>
change_name("/mnt/d/'Shingeki No Kyojin'/'Shingeki test'/", "Shingeki No Kyojin")

Resulat : 
<ul>
        <li>Shingeki No Kyojin 01</li>
        <li>Shingeki No Kyojin 02</li>
        <li>...</li>
</ul>

<H3> Important ! </H3>

- Utilisation du module Subprocess et Python3
