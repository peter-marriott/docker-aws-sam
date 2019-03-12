# Docker and AWS SAM

## Set-up

I am planning to do this work on Windows and Linux to see if there are any differences in behaviour. Starting with windows first.

### Windows set-up

| Installed | Version
|-|-|
|docker | `Docker version 18.09.2, build 6247962` |
| aws cli | `aws-cli/1.16.119 Python/3.6.0 Windows/10 botocore/1.12.109` |
| SAM cli | `SAM CLI, version 0.11.0`|
|Optional | |
| WSL | `Linux Z2 4.4.0-17763-Microsoft #253-Microsoft Mon Dec 31 17:49:00 PST 2018 x86_64 x86_64 x86_64 GNU/Linux`
| Docker client | `Docker version 18.06.3-ce, build d7080c1` |
| Docker compose | `docker-compose version 1.23.2, build 1110ad01` |

#### WSL docker client installation

```bash
wget https://download.docker.com/linux/static/stable/x86_64/docker-18.06.3-ce.tgz
tar -xzvf docker-18.06.3-ce.tgz
sudo cp docker/docker /usr/local/bin/
sudo chmod +x /usr/local/bin/docker
sudo curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Set docker daemon

![Docker Daemon setting](/images/DockerDaemonSetting.png)