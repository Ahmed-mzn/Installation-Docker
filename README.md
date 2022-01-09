# Docker

Dans ce document on va expliquer comment installer Docker sur les différents systèmes d'exploitation.

## Installation sur Ubuntu


Désinstaller les anciennes versions.

```bash
$ sudo apt-get remove docker docker-engine docker.io containerd runc
```

Executer les commandes suivants respectivement l'une apres l'autre

```bash
$ sudo apt-get update
$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
  https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Vérifier si docker est bien installer avec la commande suivant
```bash
$ sudo docker version
```



## Installation sur Fedora

#### Configuration requise pour le système d’exploitation

- Fedora 34
- Fedora 35

Désinstaller les anciennes versions.
```bash
$ sudo dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine
```

Executer les commandes suivants respectivement l'une apres l'autre
```bash
$ sudo dnf -y install dnf-plugins-core
$ sudo dnf config-manager \
    --add-repo \
    https://download.docker.com/linux/fedora/docker-ce.repo
$ sudo dnf install docker-ce docker-ce-cli containerd.io
```

Start docker
```bash
$ sudo systemctl start docker
```

Vérifier si docker est bien installer avec la commande suivant
```bash
$ sudo docker version
```


## Installation docker-compose

Exécutez cette commande pour télécharger la version stable actuelle de Docker Compose

```bash
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" \
-o /usr/local/bin/docker-compose
```

Appliquer des autorisations exécutables au fichier binaire
```bash
$ sudo chmod +x /usr/local/bin/docker-compose
```

Test the installation
```bash
$ sudo docker-compose --version
```


# Installation des images pour les tp

Vous deviez executer les commandes suivants

```bash
$ sudo docker pull python:3
$ sudo docker pull node:alpine
$ sudo docker pull postgres
$ sudo docker pull php:apache
```

Apres avoir executer les commandes suivantes verifier si toutes les images sont installer

```bash
$ sudo docker images
```

## Source
Pour plus d'informations vous pouvez consulter [`page officiel du docker`](https://docs.docker.com/get-docker/)
