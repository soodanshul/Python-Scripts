from netmiko import ConnectHandler # Module which enables SSH connection

def show_conf():

    platform = 'cisco_ios'
    host = input('Enter the HostName or IP Address: ')
    username = input('Enter the Login UserName: ') # edit to reflect
    password = input('Enter the password: ') # edit to reflect
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    output = device.send_command('show running-config')
    print(output)
    input()

show_conf()

