import subprocess

def change_name(path, saison, debut, new_name) :
	i = debut
	res = subprocess.run("ls " + path, shell = True, capture_output=True, encoding = 'UTF-8')
	lst = res.stdout.split('\n')
	for elem in lst :
		print (elem)
		subprocess.run("mv " +path+"'"+elem+"'"+ " "+ path +
			"'"+new_name+str(saison)+"'"+str(i).zfill(2)+".mkv", shell=True)
		i += 1

#change_name("/mnt/d/'Shingeki No Kyojin'/'Shingeki No Kyojin S03/'", 3, 38)
change_name("/mnt/d/'Fullmetal Alchemist Brotherhood'/", " ", 1, "Fullmetal Alchemist Brotherhood")