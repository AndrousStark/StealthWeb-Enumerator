class HELP_MODULE:
	def main():
		print("""
                                                                                       
              ░█▀█░█▀█░█▀▄░█▀▄░█▀█░█░█░█▀▀░░░░░█▀▀░▀█▀░█▀█░█▀▄░█░█
              ░█▀█░█░█░█░█░█▀▄░█░█░█░█░▀▀█░░░░░▀▀█░░█░░█▀█░█▀▄░█▀▄
              ░▀░▀░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀░▀░▀░▀

Coded by:{TerminalColor.Red} Aniruddh Atrey{TerminalColor.Reset} Email:{TerminalColor.Purple} aniruddh.atrey111101@gmail.com {TerminalColor.Reset}
LinkedIn: {TerminalColor.Red}https://www.linkedin.com/in/aniruddhatrey/{TerminalColor.Reset}
 [{TerminalColor.Green}Welcome to StealthWeb v1.0{TerminalColor.Reset}]
======================================================================================================

Usage:
    python3 StealthWeb.py [module] [args]

Modules
	dir          Uses directory enumeration mode
	dns          Uses DNS subdomain enumeration mode
	vhost        Uses Virtual Host enumeration mode
	file         Uses file enumeration mode
	fingerprint  Uses to detect web technologies
	fuzz         Uses fuzzing mode
	help         Help about any command

Optional args:
  -h, --help              help for StealthWeb
  -o, --output            Set filename to save data,
                              txt format :  -o report.txt
                              html format : -o report.html
  -w, --wordlist string   Path to the wordlist

Examples:
	dns enumeration
	use: python3 StealthWeb.py dns -d domain.com -w wordlist.txt

	dns enumeration with TXT output
	use: python3 StealthWeb.py dns -d domain.com -w wordlist.txt -o dns-output.txt

	dir enumeration
	use: python3 StealthWeb.py dir -u https://www.domain.com/ -w wordlist.txt

	vhost enumeration with 30 threads
	use: python3 StealthWeb.py vhost -d domain.com -u http://10.10.10.10 -t 30

	print only status code 200 and 301
	use: python3 StealthWeb.py dir -u https://www.domain.com/ -w wordlist.txt -s 200,301

	file detection by extensions
	use: python3 StealthWeb.py file -u https://www.domain.com/ -w wordlist.txt -x php,txt

	fingerprint
	use: python3 StealthWeb.py fingerprint -u https://www.domain.com 

	fuzz 
	use: python3 StealthWeb.py fuzz -u https://www.domain.com/FUZZ -w wordlist.txt

""")
