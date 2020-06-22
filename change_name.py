import subprocess

def take_extension (name) :
	lst = name.split('.')
	return '.'+lst[-1][:-1]

def change_saison (saison) :
	if saison != " " :
		saison_full = " S" + str(saison).zfill(2) + "E"
	else :
		saison_full = saison

	return saison_full

def change_name(path, new_name, saison = " ", debut = 1) :

	if path[-1] != "/" :
		path = path + "/"

	res = subprocess.run("ls " + path, shell = True, capture_output=True, encoding = 'UTF-8')
	lst = res.stdout.split('\n')
	lst.pop()

	lst = ["'" + elem + "'" for elem in lst]

	saison_full = change_saison (saison)

	for elem in lst :

		ext = take_extension (elem)
		new_file = "'" + new_name + saison_full + str(debut).zfill(2) + ext + "'"

		if (new_file in lst and new_file != elem) : #changer le nom du fichier si existe déjà
			index = lst.index (new_file)
			lst[index] = "'" + "xvtTMP" + str(debut) + take_extension (new_file) + "'"
			
			subprocess.run("mv " + path + new_file + " " + path + lst[index] , shell=True)

		subprocess.run("mv " + path + elem + " " + path + new_file + " -b", shell=True)

		index = lst.index (elem)
		lst[index] = new_file

		debut += 1


#change_name("/mnt/d/'Shingeki No Kyojin'/'Shingeki test'/", "Shingeki No Kyojin")