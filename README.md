# Docker and AWS SAM

## Prerequisites

| Prerequisites | Method |
|--------|---------|
| Python 3.6            | Windows msi from [https://www.python.org/downloads/](https://www.python.org/downloads/) |
| docker | `Docker version 18.09.2, build 6247962` |
| aws cli | `aws-cli/1.16.119 Python/3.6.0 Windows/10 botocore/1.12.109` |
| SAM cli | `SAM CLI, version 0.11.0`|


### Python Prerequisites

| Prerequisites | Method |
|--------|---------|
| Python 3.6            | Windows msi from [https://www.python.org/downloads/](https://www.python.org/downloads/) |
| Python libraries      | use `pip install` requirements scripts    |
|                       | Windows Powershell `requirements.ps1`     |

Install python virtual env.
If required add an alias to powershell profile so it is easy to switch to it. Warning this means changing powershell execution policy as admin user.

```powershell
cd ~
mkdir .\envs
cd envs
python -m venv docker_aws_sam
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
~\envs\docker_aws_sam\Scripts\Activate.ps1
# Optional add alias to profile
Add-Content $PROFILE "`nNew-Item -Path Alias:docker_aws_sam -Value ~\envs\docker_aws_sam\Scripts\Activate.ps1"
```


### Docker set-up

# Run Docker app

Build and test it works

```bash
cd app1
docker build -t app1 .
docker run -p 5000:5000/tcp - app1 # returns <container_id>
docker logs -ft <container_id> # Tail logs
```

```bash
curl -L http://127.0.0.1:5000/5 # returns {"success": true, "body": "id: 5"}
curl -L http://<host_ip_address>:5000/5 # returns {"success": true, "body": "id: 5"}
```

Add machine ip to hosts file

%WINDIR%\System32\drivers\etc\hosts `host_ip_address hostname`

```bash
curl -L http://<hostname>:5000/5 # returns {"success": true, "body": "id: 5"}
```





## Networking

To allow lambda running locally, in a docker container, and other docker containers to reference each other a hostname is required. Using docker version `18.03` under Windows and MacOS you can use `host.docker.internal`.
For Linux either you may use [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html) or a side car docker container such as [https://github.com/qoomon/docker-host](https://github.com/qoomon/docker-host).
Otherwise adjust your host file to have a hostname in it with the machine's ip address.

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