from netmiko import ConnectHandler
import getpass

username = input('Username: \n')
password = getpass.getpass()

with open('access_sw_ip_add') as f:
    ip_addresses = f.read().splitlines()    

all_devices = []

for ip_add in ip_addresses:
    all_devices.append(
        {
        'device_type': 'cisco_ios',
        'ip': ip_add,
        'username': username,
        'password': password.encode('ascii')
        }
    )

with open('access_sw_config') as f:
    lines = f.read().splitlines()
print (lines)

for device in all_devices:
    print(f'Connecting to device: {device["ip"]}')
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print (output)

