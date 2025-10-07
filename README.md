# 🕵️ StealthWeb Enumerator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Pentesting-red?style=for-the-badge&logo=hackaday)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**A Versatile Cybersecurity Arsenal for Web Analysis & Security Testing**

*Stealth. Precision. Intelligence.*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Modules](#-modules) • [Examples](#-examples)

</div>

---

## 📋 Overview

**StealthWeb Enumerator** is a powerful, multi-functional cybersecurity reconnaissance tool designed for professional penetration testers, security researchers, and ethical hackers. Built with Python, it provides a comprehensive suite of enumeration capabilities to assess web application security posture through intelligent information gathering and vulnerability discovery.

### 🎯 Key Capabilities

StealthWeb combines multiple reconnaissance techniques into a single, streamlined tool:

- 🌐 **DNS Enumeration** - Discover subdomains and DNS records
- 📁 **Directory Enumeration** - Bruteforce hidden directories and files
- 🖥️ **Virtual Host Discovery** - Identify virtual hosts on target servers
- 🔍 **Fuzzing Engine** - Inject payloads to discover vulnerabilities
- 📄 **File Discovery** - Locate specific file types and extensions
- 🔬 **Technology Fingerprinting** - Identify web technologies and frameworks

---

## ✨ Features

### 🚀 Performance & Efficiency
- **Multi-threaded Operations** - Blazing fast concurrent requests
- **Customizable Request Methods** - Support for GET, POST, PUT, DELETE, OPTIONS, HEAD
- **Smart Status Code Filtering** - Focus on relevant responses
- **Timeout Management** - Configurable HTTP timeouts

### 🛡️ Security & Stealth
- **Custom User-Agent** - Avoid detection with configurable UA strings
- **Cookie Support** - Maintain session state for authenticated scans
- **Basic Authentication** - Username/Password support
- **TLS Certificate Bypass** - Skip certificate validation for testing
- **Proxy Support** - Route traffic through proxies

### 📊 Output & Reporting
- **Multiple Export Formats** - TXT and HTML reports
- **Detailed Results** - Comprehensive enumeration data
- **Real-time Feedback** - Live progress monitoring

### 🎨 Modular Architecture
- **Six Specialized Modules** - Each optimized for specific tasks
- **Extensible Design** - Easy to add new features
- **Wordlist Integration** - Use custom wordlists for enumeration

---

## 🔧 Installation

### Prerequisites
- Python 3.x
- pip3

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/AndrousStark/StealthWeb-Enumerator.git

# Navigate to directory
cd StealthWeb-Enumerator

# Install dependencies
pip3 install -r requirements.txt
```

### Dependencies
StealthWeb relies on the following Python packages:
- `requests` - HTTP library
- `argparse` - Command-line parsing
- `threading` - Concurrent operations
- `beautifulsoup4` - Web scraping
- `colorama` - Terminal colors

---

## 📖 Usage

### Basic Syntax

```bash
python3 StealthWeb.py [module] [options]
```

### Global Options

| Flag | Long Form | Description | Default |
|------|-----------|-------------|---------|
| `-u` | `--url` | Target URL | - |
| `-d` | `--domain` | Target domain | - |
| `-w` | `--wordlist` | Wordlist file path | - |
| `-t` | `--threads` | Number of threads | 10 |
| `-a` | `--user-agent` | Custom User-Agent | StealthWeb v1.0 |
| `-x` | `--exts` | File extensions | - |
| `-s` | `--status-code` | Filter status codes | All |
| `-m` | `--method` | HTTP method | GET |
| `-c` | `--cookie` | Cookie string | - |
| `-k` | `--no-tls-validation` | Skip TLS verification | False |
| `-U` | `--username` | Basic Auth username | - |
| `-P` | `--password` | Basic Auth password | - |
| `--timeout` | `--timeout` | HTTP timeout (seconds) | 15 |
| `-o` | `--output` | Output file (txt/html) | - |
| `-h` | `--help` | Show help menu | - |

### Module Help

```bash
python3 StealthWeb.py [module] -h
```

Example:
```bash
python3 StealthWeb.py dir -h
```

---

## 🧩 Modules

### 1. 🌐 DNS Enumeration (`dns`)

Discover subdomains through wordlist-based enumeration.

**Purpose:** Identify valid subdomains to expand attack surface

**Key Features:**
- Subdomain bruteforce
- DNS resolution verification
- A/AAAA record lookup

**Example:**
```bash
python3 StealthWeb.py dns -d example.com -w subdomains.txt
```

---

### 2. 📁 Directory Enumeration (`dir`)

Bruteforce directories and paths on web servers.

**Purpose:** Discover hidden directories, admin panels, backup files

**Key Features:**
- Recursive directory scanning
- Status code filtering
- Custom HTTP methods
- Authentication support

**Example:**
```bash
python3 StealthWeb.py dir -u https://example.com/ -w directories.txt
```

**Advanced Usage:**
```bash
# Filter for 200 and 301 status codes only
python3 StealthWeb.py dir -u https://example.com/ -w directories.txt -s 200,301

# Use POST method with authentication
python3 StealthWeb.py dir -u https://example.com/ -w dirs.txt -m POST -U admin -P password
```

---

### 3. 🖥️ Virtual Host Discovery (`vhost`)

Identify virtual hosts configured on a web server.

**Purpose:** Discover multiple websites hosted on the same IP

**Key Features:**
- Host header manipulation
- IP-based scanning
- Multi-threaded discovery

**Example:**
```bash
python3 StealthWeb.py vhost -d example.com -u http://192.168.1.1 -t 30
```

---

### 4. 🔍 Fuzzing Engine (`fuzz`)

Inject payloads into URL parameters to discover vulnerabilities.

**Purpose:** Test for injection points, parameter manipulation

**Key Features:**
- FUZZ keyword replacement
- Custom payload lists
- Vulnerability identification

**Example:**
```bash
python3 StealthWeb.py fuzz -u https://example.com/page?id=FUZZ -w payloads.txt
```

**Use Cases:**
- SQL Injection testing
- XSS vulnerability discovery
- Path traversal detection
- Parameter fuzzing

---

### 5. 📄 File Discovery (`file`)

Enumerate specific file types on web servers.

**Purpose:** Locate sensitive files, backups, config files

**Key Features:**
- Extension-based filtering
- Multiple file type support
- Common filename patterns

**Example:**
```bash
python3 StealthWeb.py file -u https://example.com/ -w filenames.txt -x php,txt,bak
```

**Common Extensions:**
- `php, asp, aspx, jsp` - Server-side scripts
- `txt, log, bak` - Configuration and backup files
- `sql, db` - Database files
- `xml, json, yaml` - Configuration files

---

### 6. 🔬 Technology Fingerprinting (`fingerprint`)

Identify web technologies, frameworks, and server configurations.

**Purpose:** Gather intelligence on target technology stack

**Key Features:**
- Framework detection
- Server identification
- CMS recognition
- Header analysis

**Example:**
```bash
python3 StealthWeb.py fingerprint -u https://example.com
```

**Detected Technologies:**
- Web servers (Apache, Nginx, IIS)
- Programming languages (PHP, Python, Ruby)
- CMS platforms (WordPress, Joomla, Drupal)
- JavaScript frameworks (React, Angular, Vue)
- CDN services (Cloudflare, Akamai)

---

## 💡 Examples

### Basic Reconnaissance Workflow

```bash
# 1. Fingerprint the target
python3 StealthWeb.py fingerprint -u https://target.com

# 2. Enumerate subdomains
python3 StealthWeb.py dns -d target.com -w wordlists/subdomains.txt -o subdomains.txt

# 3. Directory enumeration
python3 StealthWeb.py dir -u https://target.com/ -w wordlists/directories.txt -s 200,301,403

# 4. File discovery
python3 StealthWeb.py file -u https://target.com/ -w wordlists/files.txt -x php,txt,bak,sql

# 5. Virtual host discovery
python3 StealthWeb.py vhost -d target.com -u http://192.168.1.100 -t 50
```

### Advanced Scenarios

#### Authenticated Directory Scan with Cookies
```bash
python3 StealthWeb.py dir \
  -u https://admin.target.com/ \
  -w wordlists/admin-dirs.txt \
  -c "session=abc123; auth=xyz789" \
  -s 200,302 \
  -o admin-scan.html
```

#### Multi-threaded Subdomain Enumeration
```bash
python3 StealthWeb.py dns \
  -d target.com \
  -w wordlists/massive-subdomains.txt \
  -t 100 \
  -o discovered-subdomains.txt
```

#### Fuzzing for SQL Injection
```bash
python3 StealthWeb.py fuzz \
  -u "https://target.com/search?q=FUZZ" \
  -w wordlists/sqli-payloads.txt \
  -s 200,500 \
  -o sqli-results.txt
```

#### File Discovery with Custom Extensions
```bash
python3 StealthWeb.py file \
  -u https://target.com/ \
  -w wordlists/common-files.txt \
  -x php,inc,conf,config,bak,old,sql,zip,tar.gz \
  -t 50
```

---

## 🎓 Use Cases

### 🛡️ Penetration Testing
- Initial reconnaissance and information gathering
- Attack surface mapping
- Vulnerability discovery
- Security assessment documentation

### 🔍 Bug Bounty Hunting
- Subdomain enumeration for expanded scope
- Hidden endpoint discovery
- Technology stack analysis
- Vulnerability validation

### 🏢 Enterprise Security
- Internal web application auditing
- Asset inventory and discovery
- Configuration validation
- Compliance testing

### 📚 Educational & Research
- Learning web security concepts
- Understanding enumeration techniques
- Practicing ethical hacking
- Security research projects

---

## 📊 Output Formats

### Text Format
```bash
python3 StealthWeb.py dir -u https://example.com -w dirs.txt -o report.txt
```

**Output Structure:**
```
[200] https://example.com/admin/
[301] https://example.com/backup/
[403] https://example.com/private/
[200] https://example.com/api/
```

### HTML Format
```bash
python3 StealthWeb.py dir -u https://example.com -w dirs.txt -o report.html
```

**Features:**
- Colored status codes
- Sortable tables
- Responsive design
- Professional formatting

---

## ⚠️ Legal Disclaimer

**StealthWeb Enumerator is designed for legal security testing and educational purposes only.**

### Important Notes:

- ✅ **Authorized Testing Only** - Only use this tool on systems you own or have explicit written permission to test
- ⚖️ **Legal Compliance** - Unauthorized access to computer systems is illegal in most jurisdictions
- 🎯 **Responsible Disclosure** - If you discover vulnerabilities, follow responsible disclosure practices
- 🛡️ **Ethical Use** - Use this tool ethically and professionally
- 📝 **Documentation** - Keep records of all authorized testing activities

**The authors are not responsible for any misuse or damage caused by this tool. Users are solely responsible for their actions.**

---

## 🗺️ Roadmap

### Upcoming Features
- [ ] API endpoint discovery
- [ ] SSRF detection module
- [ ] WebSocket enumeration
- [ ] Advanced payload generation
- [ ] Machine learning-based filtering
- [ ] GraphQL endpoint discovery
- [ ] JSON/XML output formats
- [ ] Integration with vulnerability scanners
- [ ] Enhanced stealth mode with rate limiting
- [ ] Custom module plugin support

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Areas for Contribution
- New enumeration modules
- Performance optimizations
- Bug fixes and improvements
- Documentation enhancements
- Wordlist additions
- Testing and QA

---

## 🐛 Known Issues

- Large wordlists may cause memory issues on systems with limited RAM
- Some CDNs may rate-limit or block aggressive scanning
- SSL/TLS bypass may not work with certificate pinning

Report issues at: [GitHub Issues](https://github.com/AndrousStark/StealthWeb-Enumerator/issues)

---

## 📚 Resources

### Recommended Wordlists
- [SecLists](https://github.com/danielmiessler/SecLists) - Comprehensive wordlist collection
- [FuzzDB](https://github.com/fuzzdb-project/fuzzdb) - Attack patterns and payloads
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - Useful payloads

### Learning Resources
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [HackerOne Disclosure Guidelines](https://www.hackerone.com/disclosure-guidelines)
- [Bug Bounty Platforms](https://www.bugcrowd.com/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

<div align="center">

**Aniruddh Atrey** | **Madhav Singh Rawat**

*Cybersecurity Researchers & Developers*

[GitHub](https://github.com/AndrousStark) • [Report Issues](https://github.com/AndrousStark/StealthWeb-Enumerator/issues)

</div>

---

## 🙏 Acknowledgments

- Inspired by industry-standard enumeration tools like Gobuster, Ffuf, and Wfuzz
- Built for the cybersecurity community
- Special thanks to all security researchers and ethical hackers

---

## 📞 Support

- 📧 **Issues**: [GitHub Issues](https://github.com/AndrousStark/StealthWeb-Enumerator/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/AndrousStark/StealthWeb-Enumerator/discussions)
- 📖 **Documentation**: [Wiki](https://github.com/AndrousStark/StealthWeb-Enumerator/wiki)

---

<div align="center">

**⭐ Star this repository if you find it useful!**

**Made with ❤️ for the Cybersecurity Community**

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=AndrousStark.StealthWeb-Enumerator)

</div>

---

## 🔐 Security Notice

If you discover a security vulnerability within StealthWeb Enumerator, please send an email to the maintainers. All security vulnerabilities will be promptly addressed.

**Do not open public issues for security vulnerabilities.**

---

*StealthWeb Enumerator - Empowering security professionals with intelligent reconnaissance capabilities.*
