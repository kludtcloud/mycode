#!/usr/bin/env Python3


def main():
    print("Module #1 name=", __name__)

if __name__ == "__main__":
    print("Code is being run directly from Python.")
else:
    print("Code is being run indirectly from import.")