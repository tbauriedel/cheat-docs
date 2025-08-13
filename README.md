# Cheat Docs

Simple command-line tool to print cheatsheets.  
Requires Python3.

The available cheats (and thus a list of them) can be viewed [here](docs/).

## Acknowledgments
This cheatsheet is insipred by the one created by [martialblog](https://github.com/martialblog/cheatsheet).

## Installation

Clone the repository into your home:
```shell
git clone https://github.com/tbauriedel/cheat-docs.git ~/.cheat-docs
```

Add an alias to have it more comfortable:
```shell
alias cheatdocs="python3 ~/.cheat-docs/docs.py"
```

## Usage

List all available cheat docs:
```shell
cheatdocs --list
```

Print cheat doc:
```shell
cheatdocs <cheat>
```

### Example output
```shell
☁  ~  cheatdocs --list
--------------------------------------------------------------------------------------------------------------------------------------------------------------
List of available cheat docs:

utils	=> list of useful utils for debugging, etc.
openssl	=> openssl command-lint util
git	=> git command-line util
...
```

```shell
☁  ~  cheatdocs openssl
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Cheat: openssl
Description: openssl command-lint util
Sections: ['keys', 'csr', 'x509', 'debugging']
Source: /root/.cheat-docs/docs/openssl.ini
--------------------------------------------------------------------------------------------------------------------------------------------------------------

[x509]
create self-signed x509 => openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
create self-signed from key and csr => openssl x509 -req -in foobar.csr -signkey foobar.key -out foobar.crt -days 365

[debugging]
print x509 details => openssl x509 -text -noout -in <certificate-file>
verify x509 is signed by ca => openssl verify -CAfile <ca-file> <certificate-file>
check pkcs12 => openssl pkcs12 -info -in <pkcs12-file>
check an ssl connection => openssl s_client -connect localhost:443
...
```

## Custom cheat docs
You can add custom cheat docs by creating a new <cheat>.ini inside the docs folder. The cheat-docs tool will read all .ini files inside of this directory and make it available.  
Please ensure to have the `cheat` section as well (This is used to print the meta information in `--list` and the cheatdoc itself).  
If you want to add some free text, use `text` inside of your `cheat` section.

## License
MIT License - Copyright (c) 2025 Tobias Bauriedel