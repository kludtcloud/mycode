#!/usr/bin/env Python3

ipchk = input("Apply an IP address:" '\n')

if ipchk == "192.168.70.1":
    print(f"Looks like the IP address was set to the Gateway {ipchk}, This is not recommended")
elif ipchk:
    print(f"Looks like the IP address was set: {ipchk}")
else:
    print("You did not provide input.")