# Universidad Autónoma de los Andes - Uniandes
> Proyecto Integrador <br>
8vo Software <br>
Mayo - Septiembre 2025  <br><br>
**Autores:** <br>
Hugo <br>
Jaime <br>
Jorge <br>





![](https://img.shields.io/badge/Docker-4.41.2-blue) 
![](https://img.shields.io/badge/Python-3.12.bullseye-blue) 


Esto se hace desde cmd
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

