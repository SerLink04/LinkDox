import os, ctypes, time, re, requests, json
from terminaltables import SingleTable
from colorama import init, Fore,  Back,  Style

name_cmd = "LinkDox - #LinkSquad - #CodedBySerLink04"

#Coded By SerLink04#9999 on discord | My server of discord >> https://discord.gg/linksquad

ctypes.windll.kernel32.SetConsoleTitleW(name_cmd)

os.system("cls")
menu_principal = """


	 ██▓     ██▓ ███▄    █  ██ ▄█▀▓█████▄  ▒█████  ▒██   ██▒
	▓██▒    ▓██▒ ██ ▀█   █  ██▄█▒ ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░
	▒██░    ▒██▒▓██  ▀█ ██▒▓███▄░ ░██   █▌▒██░  ██▒░░  █   ░
	▒██░    ░██░▓██▒  ▐▌██▒▓██ █▄ ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ 
	░██████▒░██░▒██░   ▓██░▒██▒ █▄░▒████▓ ░ ████▓▒░▒██▒ ▒██▒
	░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
	░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░ ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░
	  ░ ░    ▒ ░   ░   ░ ░ ░ ░░ ░  ░ ░  ░ ░ ░ ░ ▒   ░    ░  
	    ░  ░ ░           ░ ░  ░      ░        ░ ░   ░    ░  
	                               ░                        """

class leaked:

	def hash(self, hash):
		text = requests.get("https://hashtoolkit.com/reverse-hash/?hash="+hash).text
		passw = re.findall(r"/generate-hash/\?text=(.*?)\"", text)

		if len(passw) != 0:
			passw = passw[0]
		else:
			passw = None

		return(passw)

	def email(self, email):
		dataList = []

		try:
			req = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/"+email, headers={"Content-Type":"application/json", "Accept":"application/json", "User-Agent":"LittleBr0ther"})
			if req.status_code == 200:
				data = json.loads(req.text)
				for d in data:
					name = d['Title']
					domain = d['Domain']
					date = d['BreachDate']
					dataDic = {'Title':name, 'Domain':domain, 'Date':date}
					dataList.append(dataDic)

				return(dataList)

		except:
			return(None)

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def searchGoogle(requete='', requete2=''):

	# encodeList = [
	# 	"%21","%23","%24","%26","%27","%28","%29","%2A","%2B","%2C","%2F","%3A","%3B","%3D","%3F","%40","%5B","%5D",
	# 	"%20","%22","%25","%2D","%2E","%3C","%3E","%5C","%5E","%5F","%60","%7B","%7C","%7D","%7E"
	# ]

	encodeDic = {
		"%21": "!",
		"%23": "#",
		"%24": "$",
		"%26": "&",
		"%27": "'",
		"%28": "(",
		"%29": ")",
		"%2A": "*",
		"%2B": "+",
		"%2C": ",",
		"%2F": "/",
		"%3A": ":",
		"%3B": ";",
		"%3D": "=",
		"%3F": "?",
		"%40": "@",
		"%5B": "[",
		"%5D": "]", 
		"%20": " ",
		"%22": "\"",
		"%25": "%",
		"%2D": "-",
		"%2E": ".",
		"%3C": "<",
		"%3E": ">",
		"%5C": "\\",
		"%5E": "^",
		"%5F": "_",
		"%60": "`",
		"%7B": "{",
		"%7C": "|",
		"%7D": "}",
		"%7E": "~",
	}

	if requete2 != '':
		content = requete2.text #.content.decode('utf-8')
		urls = re.findall('url\\?q=(.*?)&', content)
		for url in urls:
			for char in encodeDic:
				find = re.search(char, url)
				if find:
					charDecode = encodeDic.get(char)
					url = url.replace(char, charDecode)
			if not "googleusercontent" in url:
				if not "/settings/ads" in url:
					if not "/policies/faq" in url:
					# if "insta" in url or "twitter" in url or "facebook" in url:
						print(Fore.RED + "[++] Possible connection: "+ Fore.GREEN + url)
	else:
		pass

	content = requete.text
	urls = re.findall('url\\?q=(.*?)&', content)
	for url in urls:
		for char in encodeDic:
			find = re.search(char, url)
			if find:
				charDecode = encodeDic.get(char)
				url = url.replace(char, charDecode)
		if not "googleusercontent" in url:
			if not "/settings/ads" in url:
				if not "/policies/faq" in url:
				# if "insta" in url or "twitter" in url or "facebook" in url:
					print(Fore.RED + "[+] Possible connection: "+ Fore.GREEN + url)

def google():
	print("\n"+information+" Ingresa un nombre, apellido, ciudad, deporte, colegio ... \n (Cuanta más información introduzcas, la búsqueda será más específica)\n")
	nom = input(Fore.RED + "  [LinkDox] " + Fore.CYAN + "Introduzca datos: " + Fore.WHITE)
	print("\n"+wait+" Buscando información...")
	url = "https://www.google.com/search?num=20&q=\\%s\\"
	try:
		lista = ""
		nom2 = nom.split()
		if len(nom2) == 0:
			print()
			print(Fore.RED + "[!]" + Fore.GREEN + " Faltan parámetros...")
			print()
			return
		longi = str(nom2[-1])
		for argumento in nom2:
			if argumento == longi:
				lista += str(argumento)
				continue
			lista += str(argumento) + "+"
	except:
		pass
	requete = requests.get(url % (lista))
	searchGoogle(requete=requete)


def SearchEmail():
	print()
	email = input(Fore.RED + "  [LinkDox] " + Fore.CYAN + "Introduce un correo: " + Fore.WHITE)
	print("\n"+wait+" Intentando obtener información del correo '%s'..." % (email))
	lkd = leaked()
	leak = lkd.email(email)

	if leak:
		TABLE_DATA = [
			('Title', 'Domain', 'Date'),
		]

		for lk in leak:
			name = lk['Title']
			domain = lk['Domain']
			date = lk['Date']

			tuples = (name, domain, date)
			TABLE_DATA.append(tuples)

		table = SingleTable(TABLE_DATA, " Leaked Site ")
		print(table.table)


		print("\n"+wait+" Buscando la contraseña...")

	table_dump = [
		('Email', 'Password'),
	]

	url = "https://www.google.fr/search?num=100&q=\\intext:\"%s\"\\"
	content = requests.get(url % (email)).text
	urls = re.findall('url\\?q=(.*?)&', content)
	cout = len(urls)
	if cout == 0:
		print(warning+" No se encontró ningún resultado...")
	else:
		contador = str(cout)
		if contador == "1":
			print(wait+" Revisando 1 Link...")
		else:
			print(wait+" Revisando %s Links..." % (str(cout)))
		x = 1
		countPassword = 0
		for url in urls:
			if not "googleusercontent" in url:
				if not "/settings/ads" in url:
					if not "webcache.googleusercontent.com/" in url:
						if not "/policies/faq" in url:
							try:
								texte = requests.get(url).text
								combo = re.search(email+r":([a-zA-Z0-9_ & * $ - ! / ; , ? + =  | \. ]+)", texte).group()
								if combo:
									passw = combo.split(":")[1]
									tuples = (email, passw)
									countPassword += 1
									table_dump.append(tuples)
							except:
								pass
		if countPassword > 0:
			table = SingleTable(table_dump, " Dump ")
			print("\n"+table.table)
		else:
			print(warning+" No se encontraron datos del correo '%s' " % (email))

def searchUserName():
	print()
	username = input(Fore.RED + "  [LinkDox]" + Fore.CYAN + " Introduce un nick: " + Fore.WHITE)
	print("\n  "+wait+" Buscando información de '%s'..." % (username))

	# url = "https://www.google.com/search?num=100&q=\\\"%s\"\\"
	url = "https://www.google.com/search?num=100&q=\\%s\\"
	url2 = "https://www.google.com/search?num=100&q=\\intitle:\"%s\"\\"
	requete = requests.get(url % (username))
	requete2 = requests.get(url2 % (username))
	searchGoogle(requete=requete, requete2=requete2)

menu = """

 {0} [1] {1}Esto intentará conseguir la contraseña de un email (Funciona a veces)
 {0} [2] {1}Buscar información a partir de un nick
 {0} [3] {1}Obtener información de una IP
 {0} [4] {1}Buscar información a partir de varios parámetros (Nick,nombre,ciudad...)
 {0} [5] {1}Esta opción nos ayudará a obtener el historial de nicks de un nick de minecraft

 {0} cls {1}Esto servirá para limpiar la pantalla
 {0} ctrl + c {1}Para salir de la Tool

""".format(Fore.RED, Fore.CYAN)

print(Fore.RED + menu_principal)
print()
print(Fore.YELLOW + " " * 2 + " Official Doxing Tool of LinkSquad Private #CodedBySerLink04")
print(menu)
try:
	while True:
		parametros = input(Fore.MAGENTA + "  root@linksquad ═> " + Fore.WHITE)
		if parametros == "1":
			SearchEmail()
		elif parametros == "2":
			searchUserName()
		elif parametros == "3":
			print()
			try:
				target = input(Fore.RED + "  [LinkDox] " + Fore.CYAN + " Introduce una ip: " + Fore.WHITE)
				url = ("http://ip-api.com/json/")
				response = requests.get(url + target)
				data = response.text
				jso = json.loads(data)
				print()
				print(f"{Fore.WHITE} IP: "+(target))
				print(f"{Fore.WHITE} ISP: "+(jso["isp"]))
				print()
				print(f" {Fore.MAGENTA}[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE} Country: "+(jso["country"])+" - TZ: "+(jso["timezone"]))
				print(f"  {Fore.WHITE}║")
				print(f"  {Fore.WHITE}╚═{Fore.MAGENTA}[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE} Region: "+(jso["regionName"])+" - "+(jso["zip"]))
				print(f"     {Fore.WHITE}║")
				print(f"     {Fore.WHITE}╚═{Fore.MAGENTA}[{Fore.WHITE}#{Fore.MAGENTA}]{Fore.WHITE} City: "+(jso["city"]))
				print()
			except:
				pass
		elif parametros == "4":
			google()
		elif parametros == "5":
			print()
			user = input(Fore.RED + "  [LinkDox] " + Fore.CYAN + "Introduce un nick de minecraft: " + Fore.WHITE)
			nick = user.lower()
			url = "https://api.mojang.com/users/profiles/minecraft/"
			text123 = requests.get((url)+(nick))
			texto_json = text123.text
			if texto_json == "":
				print()
				print(Fore.RED + "  NICK: " + Fore.YELLOW + str(nick))
				print(Fore.RED + "  TYPE: " + Fore.YELLOW + "Cracked")
				print()
			else:
				texto_json_2 = json.loads(texto_json)
				uuid = texto_json_2.get("id")
				other_response = requests.get("https://api.mojang.com/user/profiles/" + uuid + "/names")
				textoo = other_response.text
				jsonxd = json.loads(textoo)
				lista = []
				for i in jsonxd:
					lista.append(i)
				lista3 = ""
				for elemento in lista:
					get = elemento.get("name")
					lista3 += "  " + str(get) + "\n"
				print()
				print(Fore.RED + "  NICK: " + Fore.YELLOW + str(nick))
				print(Fore.RED + "  TYPE: " + Fore.YELLOW + "Premium")
				print(Fore.RED + "  UUID: " + Fore.GREEN + str(uuid))
				print(Fore.RED + "  HISTORY NICKS:\n" + Fore.CYAN + "{}".format(lista3))
				print()
		elif parametros == "cls":
			os.system("cls")
			print(Fore.RED + menu_principal)
			print()
			print(Fore.YELLOW + " " * 2 + " Official Doxing Tool of LinkSquad Private #CodedBySerLink04")
			print(menu)
except KeyboardInterrupt:
	print(Fore.RED + "\n\n  [LinkDox]" + Fore.GREEN + " Saliendo de la tool..." + Fore.WHITE)
	time.sleep(1.5)
except:
	pass
