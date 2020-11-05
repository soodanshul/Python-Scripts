from netmiko import ConnectHandler # Module which enables SSH connection


platform = 'cisco_ios'
host = input('Enter the HostName or IP Address: ')
username = input('Enter the Login UserName: ')
password = input('Enter the password: ')
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

VLAN = input("Enter the VLAN ID: ")
Name = input("Name of VLAN: ")

device.send_command('conf t')
config_commands = [VLAN , Name]
output = net_connect.send_config_set(config_commands)
print(output)
input()
