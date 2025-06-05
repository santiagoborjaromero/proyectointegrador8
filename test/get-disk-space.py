import paramiko
import subprocess

# Datos de conexión
# host = '172.17.0.2'
# port = 22
# username = 'lisah_user'
# password = 'L1s4hUn14nd3'

# PRIVATE_KEY_PATH = "ubuntu_server.pem"
# REMOTE_COMMAND = "ls -la"

def saveFile(file, content):
    fileb = open(file, "w")
    fileb.write(f'{content}')
    fileb.close()


def getData(server, cmd):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh_client.connect(host, port=port, username=username, pkey=private_key)
        if (server["password"]!=""):
            ssh_client.connect(server["host"], port=server["port"], username=server["user"], password=server["password"])
        else:
            if (server["pkey"]!=""):
                private_key = paramiko.RSAKey.from_private_key_file(filename=server["pkey"])
                ssh_client.connect(server["host"], port=server["port"], username=server["user"], pkey=private_key)
            else:   
                print("No exite autenticacion")
                return 


        stdin, stdout, stderr = ssh_client.exec_command(cmd["cmd"])

        output = stdout.read().decode("utf-8")
        error = stderr.read().decode("utf-8")

        print("Output:\n", output)
        saveFile(cmd["file"], output)

        if error:
            print("Error:\n", error)

        if ssh_client:
            ssh_client.close()
    except Exception as e:
        print(f"Error al conectar o ejecutar el comando: {e}")

    


if __name__ == '__main__':
    servers = [
        {"host": "172.17.0.2", "port": 22, "user": "lisah_user", "password": "L1s4hUn14nd3" , "pkey": ""},
        # {"host": "172.17.0.2", "port": "22", "username": "lisah_user", "password": "" , "key": "ubuntu_server.pem"},
    ]

    commands = [
        {"cmd":"ls -la", "file": "ls.txt"},
        {"cmd":"df -h", "file": "espacio_disco.txt"},
        {"cmd":"users", "file": "usuarios_conectados.txt"},
        {"cmd":"getent passwd", "file": "listado_usuarios.txt"},
        {"cmd":"vmstat", "file": "memoria.txt"},
        {"cmd":"w", "file": "load.txt"},
        {"cmd":"uname", "file": "distro.txt"},
    ]

    for server in servers:
        for cmd in commands:
            # print(server, cmd)
            getData(server, cmd)
