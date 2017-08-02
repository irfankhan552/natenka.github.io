import netmiko

def send_show_command(device_params):
    print('Opening connection to IP: {}'.format(device_params['ip']))
    conn = netmiko.ConnectHandler(**device_params)
    conn.enable()
    result = None
    while True:
        try:
            command = yield result
            result = conn.send_command(command)
        except GeneratorExit:
            conn.disconnect()
            print('Connection closed')
            break


DEVICE_PARAMS = {'device_type': 'cisco_ios',
                 'ip': '192.168.100.1',
                 'username': 'cisco',
                 'password': 'cisco',
                 'secret': 'cisco' }

ssh = send_show_command(DEVICE_PARAMS)
next(ssh)
r = ssh.send('sh ip int br')
print(r)
ssh.close()

