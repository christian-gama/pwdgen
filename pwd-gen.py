#!/usr/bin/env python3
import argparse

from generator.password_generator import password_generator

def main():
    parser = argparse.ArgumentParser(description="A password generator.")

    parser.add_argument('-l', '--length', required=True, help='Password length')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-d', '--lowercase', action='store_true', help='Include lowercase letters')
    parser.add_argument('-n', '--numbers', action='store_true', help='Include numbers')
    parser.add_argument('-s', '--symbols', action='store_true', help='Include symbols')
    
    args = parser.parse_args()
    
    if not args.uppercase and not args.lowercase and not args.numbers and not args.symbols:
        print('You must select at least one of the options: -u, -l, -n, -s')
        exit(1)
    
    password = password_generator(
        length=int(args.length),
        uppercase=args.uppercase,
        lowercase=args.lowercase,
        numbers=args.numbers,
        symbols=args.symbols,
    )
    
    print(password)
    
if __name__ == '__main__':
    main()