# Cheat Docs

Simple command-line tool to print cheatsheets.

Requires Python3.

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

## Custom cheat docs
You can add custom cheat docs by creating a new <cheat>.ini inside the docs folder. The cheat-docs tool will read all .ini files inside of this directory and make it available.  
Please ensure to have the `cheat` section as well (This is used to print the meta information in `--list` and the cheatdoc itself)

## License
MIT License - Copyright (c) 2025 Tobias Bauriedel
