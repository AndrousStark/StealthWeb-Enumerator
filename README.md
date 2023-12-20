# StealthWeb
DNS, Directories,virtual host, file enumeration and fingerprint tool

<h3>Modules</h3>
<li>dir         - Uses directory enumeration mode</li>
<li>dns         - Uses DNS subdomain enumeration mode</li>
<li>vhost       - Uses Virtual Host enumeration mode</li>
<li>file        - Uses file enumeration mode</li>
<li>fingerprint - Uses to detect web technologies</li>
<li>fuzz        - Uses fuzzing mode</li>
<li>help        - Help about any command</li>
<br>

install requirements
```
pip3 install -r requirements.txt
```

show module help menu
```
 python3 StealthWeb.py [module] -h 
 example: python3 StealthWeb.py dir -h
```
optional arguments:
```
  -u, --url                 set target url
  -d, --domain              set target domain
  -a, --user-agent          set user-agent 'StealthWeb v1.0' by default
  -x, --exts                set target extensions files (php,txt,html)
  -s, --status-code         set the status code to print (200,301)
  -w, --wordlist            set wordlist file
  -t, --threads             set threads
  -m, --method              set method (GET/POST/DELETE/OPTION/PUT/HEAD) for requests, GET by default.
  -h, --help                show this message
  -c, --cookie              set cookies to use for the requests
  -k, --no-tls-validation   skip TLS certificate verification
  -P, --password            Password for Basic Auth
  -U, --username            Username for Basic Auth
      --timeout             HTTP Timeout (default 15s)
  -o, --output              set filename to save data
                                 txt format  -o report.txt
                                 html format -o report.html
```
DNS Enumeration mode:
```
  python3 StealthWeb.py dns -d domain.com -w wordlist.txt
```

Dir enumeration mode:
```
  python3 StealthWeb.py dir -u https://www.domain.com/ -w wordlist.txt
```

Print only codes 200 and 301
```
  python3 StealthWeb.py dir -u https://www.domain.com/ -w wordlist.txt -s 200,301
```

Virtual host enumeration mode:
```
  python3 StealthWeb.py vhost -d domain.thm -u http://10.10.10.10 -t 30
```

Fuzz enumeration mode:
```
  python3 StealthWeb.py fuzz -u https://www.domain.com/FUZZ -w wordlist.txt
```

file discovery
```
  python3 StealthWeb.py file -u https://www.domain.com/ -w wordlist.txt -x php,txt
```

fingerprint for get web technology
```
  python3 StealthWeb.py fingerprint -u https://www.domain.com
```


