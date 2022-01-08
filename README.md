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


## Installation sur Windows

### Installer Docker sur Windows 7/8/10 Home

Si vous avez Windows 7/8 ou 10 Home, vous devez installer Docker Toolbox.

- Tout d’abord, rendez-vous sur le [référentiel officiel Docker Toolbox](https://github.com/docker-archive/toolbox/releases) sur Github et téléchargez le dernier exécutable disponible‎
- Exécutez le programme d’installation de Docker Toolbox pour Windows.

![](https://devconnected.com/wp-content/uploads/2019/08/step-1-toolbox.png)

Cliquez sur next, next... puis install

Après un court moment, votre installation devrait se terminer. Laissez la case cochée pour voir les raccourcis créés par Docker.

- Exécuter le démarrage rapide de Docker pour Windows‎

![](https://devconnected.com/wp-content/uploads/2019/08/shortcuts.png)

Double-clique sur l’icône pour démarrer _**Docker Quickstart**_ .‎

Un shell de terminal s’ouvre et commence à exécuter certaines commandes sur votre ordinateur pour configurer correctement Docker. Cette étape d’installation créera une machine virtuelle VirtualBox à l’aide de l’ISO Boot2Docker téléchargée

![](https://devconnected.com/wp-content/uploads/2019/08/docker-quickstart-step-1.png)

Attendez quelques instants que la configuration se termine.‎

Après quelques instants, vous devriez voir Moby (la baleine de Docker!), ce qui signifie que votre installation a réussi

![](https://devconnected.com/wp-content/uploads/2019/08/docker-toolbox-exe-2.png)

Pour vérifier votre version actuelle de Docker, exécutez la commande suivante‎
```bash
$ docker version
```

![](https://devconnected.com/wp-content/uploads/2019/08/docker-version-1.png)


### Installer Docker sur Windows 10 Pro / Entreprise

- Vous deviez vérifiez vos paramètres de virtualisation
- ‎Pour télécharger Docker Desktop, rendez-vous sur [cette page](https://docs.docker.com/desktop/windows/install/) et cliquez sur _**« Docker Desktop for Windows »**_.
## Source
Pour plus d'informations vous pouvez consulter [`page officiel du docker`](https://docs.docker.com/get-docker/)
