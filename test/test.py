import paramiko
import subprocess

#Datos de conexión
host = '172.17.0.2'
port = 22
username = 'lisah_user'
password = 'L1s4hUn14nd3'

PRIVATE_KEY_PATH = "ubuntu_server.pem"
REMOTE_COMMAND = "ls -la"



try:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh_client.connect(host, port=port, username=username, pkey=private_key)
    if (password!=""):
        ssh_client.connect(host, port=port, username=username, password=password)
    else:
        if (PRIVATE_KEY_PATH!=""):
            private_key = paramiko.RSAKey.from_private_key_file(filename=PRIVATE_KEY_PATH)
            ssh_client.connect(host, port=port, username=username, pkey=private_key)
        else:   
            print("No exite autenticacion")


    stdin, stdout, stderr = ssh_client.exec_command(REMOTE_COMMAND)

    output = stdout.read().decode("utf-8")
    error = stderr.read().decode("utf-8")

    print("Output:\n", output)

    if error:
        print("Error:\n", error)
    if ssh_client:
        ssh_client.close()

except Exception as e:
    print(f"Error al conectar o ejecutar el comando: {e}")
