#basic pyhton script to show the running-configuration of Cisco Devices

from netmiko import ConnectHandler      # Module which enables SSH connection

def show_conf():

    platform = 'cisco_ios'
    host = input('Enter the HostName or IP Address: ')
    username = input('Enter the Login UserName: ')
    password = input('Enter the password: ') 
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    output = device.send_command('show running-config')
    print(output)
    input()

show_conf()

