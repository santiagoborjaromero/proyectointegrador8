usuario: lisah_user
contraseña: L1s4hUn14nd3


Esto se hace desd cmd
```
ssh lisah_user@localhost -p 2223 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null
```

Crear una red
```
docker network create mi_red
```


Pasa sacar un PEM

En el server ubuntu

```
mkdir -p ~/.ssh
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
```

En el cliente
```
docker cp ubuntu_server:/home/lisah_user/.ssh/id_rsa ./ubuntu_server.pem
```

Y se puede acceder 
```
ssh -i ubuntu_server.pem lisah_user@localhost -p 2223 
```


Copiar con power shell un recurso del contenedor y pasarlo a local 
```
docker cp beautiful_dijkstra:/workspaces/python-2/ .
```

