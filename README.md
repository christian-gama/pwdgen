
A simple and customizable command-line password generator written in Python.

## Features

- Generate random passwords of a specified length.
- Customize the character set by including or excluding uppercase letters, lowercase letters, numbers, and symbols.

## Installation

1. Clone the repository
```bash
git clone g
```

2. Make the `pwdgen.py` script executable by running:

```bash
chmod +x pwdgen.py
```

3. Create a symlink named pwdgen that points to the pwdgen.py script:
```bash
sudo ln -s /path/to/pwdgen.py /usr/local/bin/pwdgen
```

## Usage
Generate a random password by calling the pwdgen command:
```bash
pwdgen -l 16 -u -d -n -s
```

## Command-line options
| Short Option | Long Option  | Description                      | Default Value |
|--------------|--------------|----------------------------------|---------------|
| -l           | --length     | Length of the password           | 16            |
| -u           | --uppercase  | Include uppercase letters        | false         |
| -d           | --lowercase  | Include lowercase letters        | false         |
| -n           | --numbers    | Include numbers                  | false         |
| -s           | --symbols    | Include symbols                  | false         |
