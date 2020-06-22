import subprocess

def take_extension (name) :
	lst = name.split('.')
	return '.'+lst[-1]


def change_name(path, saison, debut, new_name) :
	i = debut
	res = subprocess.run("ls " + path, shell = True, capture_output=True, encoding = 'UTF-8')
	lst = res.stdout.split('\n')
	lst.pop()

	for elem in lst :
		print (elem)
		ext = take_extension (elem)

		subprocess.run("mv " + path + "'" + elem + "'" + " " + 
			path + "'" + new_name + " S" + str(saison).zfill(2) + "E" + str(i).zfill(2) + ext + "'"
			, shell=True)

		i += 1


change_name("/mnt/d/'Shingeki No Kyojin'/'Shingeki No Kyojin S03'/", 3, 1, "Shingeki No Kyojin")
#change_name("/mnt/d/'Fullmetal Alchemist Brotherhood'/", " ", 1, "Fullmetal Alchemist Brotherhood")