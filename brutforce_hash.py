import subprocess
import crypt

shadow = subprocess.check_output("cat /etc/shadow", shell=True).decode()
#print(shadow)

passwd_list = shadow.split("\n")
#print(passwd_list)

file = open("password.txt","r")

#kali:$y$j9T$AB7f3WOFqXBj299UsTEOR0$chjchh:19124:0:99999:7:::
#$y$ -> yescrypt algorithm
#j9T$AB7f3WOFqXBj299UsTEOR0 -> salt

##so we need convert to salt, password to salt 
for passwd in passwd_list:
	
	if "$" in passwd:
		s = passwd.split("$") # to split like a array
		salt = "$" + s[1] + "$" + s[2] + "$" + s[3]
				
		#create salt value for each password in file 
		for passwd_try in file:
			temp_password = crypt.crypt(passwd_try.strip(),salt)
			print(temp_password)

			if temp_password in passwd:
				print("Password is:",passwd_try.strip())
				break
