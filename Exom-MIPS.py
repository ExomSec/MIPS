import socket
from colorama import Fore, Style, Back
import platform
import os
from netaddr import iter_iprange
import emoji
import traceback
import keyboard
import custom_range
import time




def mass_scan():
	def main(*args):
		def main_scanner(domain, port):
			b_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			location = (str(domain), int(port))
			b_socket.settimeout(timeout)
			try:
				result_of_check = b_socket.connect_ex(location)
			except:
				pass
			b_socket.close()
			if result_of_check == 0:
				twiaf.append(f'{domain}:{port}'.format(domain=domain, port=port))
		generator = args[0]
		twiaf = []
		path = os.getcwd() + r'\results.txt'
		timer = 0
		os.system(c)
		print(CYAN + logo)
		print(WARNING + "(If you got an error during the scan or if you just wanted to abort, the results should still be written into the results.txt file.)" + Style.RESET_ALL, Fore.RESET)
		while True:
			try:
				time_s = time.time()
				ip_in_check = next(generator)
				if keyboard.is_pressed('ctrl + c'):
					print("Quitting...")
					time.sleep(3)
					exit()
				print(f"{GREEN}Trying: {ip_in_check}                     Speed:  One check in {str(timer)[0:6]}        Found open ports:  {str(len(twiaf))}        ", end='\r')
				main_scanner(ip_in_check, scan_port)
				time_end = time.time()
				timer = time_end - time_s
				if len(twiaf) != 0:
					twiaf_open = open(path, 'w')
					for x in twiaf:
						twiaf_open.writelines(x)
			except StopIteration:
				pass


	while True:
		os.system(c)
		print(CYAN + logo)
		scan_port = input(GREEN + "Port to find\n------>  ")
		if scan_port.isnumeric():
			os.system(c)
			print(CYAN + logo)
			class_to_scan = input(GREEN + f"Class to scan for\n[A] Class A   (0 - 127)\n[B] Class B   (128 - 191)\n[C] Class C   (192 - 223)\n[D] Class D   (224 - 239)\n[E] Class E   (240 - 255)\n\n[ALL] All Classes (Takes for ages, others take only a few hours)\n\n[CUSTOM] Choose the range yourself\n\n{MAGENTA}-------->   ")
			class_to_scan = class_to_scan.lower()
			if class_to_scan == "a":
				class_to_scan = CLASS_A
				break
			if class_to_scan == "b":
				class_to_scan = CLASS_B
				break
			if class_to_scan == "c":
				class_to_scan = CLASS_C
				break
			if class_to_scan == "d":
				class_to_scan = CLASS_D
				break
			if class_to_scan == "e":
				class_to_scan = CLASS_E
				break
			if class_to_scan == "all":
				class_to_scan = CLASS_ALL
				break
			if class_to_scan == "custom":
				class_to_scan = custom()
				break
	main(class_to_scan)


def isfloat(num):
    try:
        float(num)

        return True
    except ValueError:
        return False


def check():
	os.system(c)
	print(GREEN + logo)
	domain = input("Domain or IP address\n------>  ")
	os.system(c)
	print(logo)
	type_domain = domain.replace(".", "")
	while True:
		port = input("Port to Check For\n------>  ")
		if port.isnumeric():
			port = int(port)
			break
	if type_domain.isnumeric() == False:
		try:
			domain = socket.gethostbyname(domain)
		except:
			os.system(c)
			print(f"{ERROR}Error getting ip address from domain!")
			exit()
	a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	location = (domain, port)
	a_socket.settimeout(timeout)
	try:
		result_of_check = a_socket.connect_ex(location)
	except:
		os.system(c)
		print(ERROR)
		exit()
	if result_of_check == 0:
		os.system(c)
		print(GREEN + Back.BLACK + """ ██████  ██████  ███████ ███    ██ 
██    ██ ██   ██ ██      ████   ██ 
██    ██ ██████  █████   ██ ██  ██ 
██    ██ ██      ██      ██  ██ ██ 
 ██████  ██      ███████ ██   ████ 
								   """)
		
	else:
		os.system(c)
		print(Style.DIM + Fore.YELLOW + Back.RED + """                                                                                                                           
  ██████   ██████  ██████  ████████     ██ ███████     ███    ██  ██████  ████████      ██████  ██████  ███████ ███    ██  
  ██   ██ ██    ██ ██   ██    ██        ██ ██          ████   ██ ██    ██    ██        ██    ██ ██   ██ ██      ████   ██  
  ██████  ██    ██ ██████     ██        ██ ███████     ██ ██  ██ ██    ██    ██        ██    ██ ██████  █████   ██ ██  ██  
  ██      ██    ██ ██   ██    ██        ██      ██     ██  ██ ██ ██    ██    ██        ██    ██ ██      ██      ██  ██ ██  
  ██       ██████  ██   ██    ██        ██ ███████     ██   ████  ██████     ██         ██████  ██      ███████ ██   ████  
																														   """)
	print(Style.RESET_ALL)
	a_socket.close()
	exit()
logo = """███████ ██   ██  ██████  ███    ███     ███    ███ ██ ██████  ███████ 
██       ██ ██  ██    ██ ████  ████     ████  ████ ██ ██   ██ ██      
█████     ███   ██    ██ ██ ████ ██     ██ ████ ██ ██ ██████  ███████ 
██       ██ ██  ██    ██ ██  ██  ██     ██  ██  ██ ██ ██           ██ 
███████ ██   ██  ██████  ██      ██     ██      ██ ██ ██      ███████ 

"""


def custom():
	os.system(c)
	print(logo)
	print(f"{Fore.YELLOW}{Style.BRIGHT}Examples:\n             - 192.x.x.x (Loops trough all of the x until 192.255.255.255)\n             - 148-150.x.x.x (Loops trough all of the x {RED}AND{Fore.YELLOW} 148-150 from octet group A)\n             - 192.168.x.x (Loops trough all of the x, and ends in 192.168.255.255)")
	r = input(Fore.LIGHTBLACK_EX + "\nCustom Range ------->   ")
	if "-" in r:
		starting, ending = custom_range.lined_range(r)
		CUSTOM_ITER = iter_iprange(starting, ending, step=1)
	else:
		starting, ending = custom_range.normal_range(r)
		CUSTOM_ITER = iter_iprange(starting, ending, step=1)
	return CUSTOM_ITER
		
		


def settings():
	while True:
		os.system(c)
		print(r""" __      _   _   _                 
/ _\ ___| |_| |_(_)_ __   __ _ ___ 
\ \ / _ \ __| __| | '_ \ / _` / __|
_\ \  __/ |_| |_| | | | | (_| \__ \
\__/\___|\__|\__|_|_| |_|\__, |___/
                         |___/     """)
		timeout = input("Set timeout time for connect_ex:   ")
		if timeout.isnumeric():
			timeout = int(timeout)
			break
		if isfloat(timeout):
			timeout = float(timeout)
			break
		

try:
	if __name__ == "__main__":
		os.system("title ExomSec - MIPS")
		GREEN = Style.BRIGHT + Fore.GREEN
		ERROR = Style.BRIGHT + Fore.RED + Back.BLACK + "ERROR!"
		WARNING = Style.BRIGHT + Fore.YELLOW + Back.RED
		CYAN = Style.BRIGHT + Fore.CYAN
		RED = Style.DIM + Fore.RED
		BLUE = Style.BRIGHT + Fore.BLUE
		MAGENTA = Style.BRIGHT + Fore.MAGENTA
		CLASS_A = iter_iprange('0.0.0.0', '127.255.255.255', step=1)
		CLASS_B = iter_iprange('128.0.0.0', '191.255.255.255', step=1)
		CLASS_C = iter_iprange('192.0.0.0', '223.255.255.255', step=1)
		CLASS_D = iter_iprange('224.0.0.0', '239.255.255.255', step=1)
		CLASS_E = iter_iprange('240.0.0.0', '255.255.255.255', step=1)
		CLASS_ALL = iter_iprange('0.0.0.0', '255.255.255.255', step=1)
		CLASS_CUSTOM = "custom"
		timeout = 0.5
		star = emoji.emojize(':glowing_star:')
		green_heart = emoji.emojize(':green_heart:')
		c = ''
		if platform.system() == 'Linux':
			c = "clear"
		if platform.system() == 'Windows':
			c = "cls"
		print(platform.system())
		
		
		while True:
			os.system(c)
			print(GREEN + """___  ___                 
|  \/  |                 
| .  . | ___ _ __  _   _ 
| |\/| |/ _ \ '_ \| | | |
| |  | |  __/ | | | |_| |
\_|  |_/\___|_| |_|\__,_|\n""")
			print(Fore.YELLOW + """Select An option:
	[1] Check for a single host port.
	[2] Find lots of hosts with a certain open port.\n
	[3] Settings.   (Set timeout (Default is 0.5 seconds.))""")
			o = input(f"{CYAN}-------------------------> ")
			if int(o) == 1:
				check()
			if int(o) == 2:
				mass_scan()
			if int(o) == 3:
				settings()
			else:
				exit()






except Exception:
	os.system(c)
	#traceback.print_exc()  ### Only uncomment this if you know what you're doing and are interested in the exception!
	print(Fore.MAGENTA + logo)
	print(f"\n{GREEN}User exit {RED}OR {Fore.YELLOW}unexpected error occurred{Style.RESET_ALL}{Fore.RESET}")
	if platform.system() == "Windows":
		os.system("color")
	socket.close()
	exit()



		