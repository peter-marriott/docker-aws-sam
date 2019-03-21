# Docker and AWS SAM

Purpose of this project is to demonstrate using docker and AWS SAM together.

The scenarios the project demonstrates are:

- Lambda function via http api calling a docker web api.
- Lambda function via http api calling Lambda function directly.
- Lambda function called by SNS event.
- Docker web api calling a Lambda function via http api.
- Docker web api calling a Lambda function directly.
- Debugging Lambda function.
- Local change.

There are also docker containers running DynamoDB, Redis and PostgreSQL so the Lambda functions can be extended.

## Prerequisites

All paths used in this file are relative to this read me.

### Windows set-up

Windows set-up done from msi installers.

Beware of firewall issues. With access on port 443 and file sharing with Docker.

| Prerequisites | Method
|--------|---------
| Python 3.6 | Windows msi from [https://www.python.org/downloads/](https://www.python.org/downloads/)
| docker | `Docker version 18.09.2, build 6247962`
| aws cli | `aws-cli/1.16.119 Python/3.6.0 Windows/10 botocore/1.12.109`
| SAM cli | `SAM CLI, version 0.11.0`

Install a python virtual environment to allow editing and linting tools to use only those libraries required by the project. When using this in Powershell to run the _Activate_ script the powershell execution policy has to be changed to allow non signed scripts to be run.

```powershell
cd ~
mkdir .\envs
cd envs
python -m venv docker_aws_sam
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
~\envs\docker_aws_sam\Scripts\Activate.ps1
# Optional add alias to profile
Add-Content $PROFILE "`nNew-Item -Path Alias:docker_aws_sam -Value ~\envs\docker_aws_sam\Scripts\Activate.ps1"
cd <workspace>
pip install -r .\requirements.txt
```

After virtual environment has been activated use pip to install python requirements. `pip install -r .\requirements.txt`

#### VS Code

settings.json changes for using `unittest`

```json
{
    "pythonTestExplorer.testFramework": "unittest",
    "python.unitTest.unittestArgs": ["-s", "tests"],
}
```

## Build and test

Start four Powershell windows: docker, SAM api gateway, SAM lambda and one for running cli commands and web requests.

The Dynamodb container command line parameters have been changed to `-sharedDb` so 'DynamoDB uses a single database file instead of separate files for each credential and Region'. This avoids an issue if the aws context is different for the `sam local start-api --host 0.0.0.0` and the aws cli DynamoDB set-up.

Build and test it works. Paths are relative to this read me.

### Build

Shell 1

```powershell
cd .\docker
docker-compose build # Build containers
docker-compose up -d # Start containers
docker-compose logs -tf --tail=10 # View output
```

Shell 2

```powershell
cd .\sam\sam-api
sam build --use-container # This takes a while downloading container first time, need interest access to download Python libraries
sam local start-api --host 0.0.0.0 # --host allows requests from non localhost
```

Shell 3

```powershell
cd .\sam\sam-function
sam build --use-container
sam local start-lambda --host 0.0.0.0
```

### Test

```powershell
curl http://127.0.0.1:5000/4 # Docker end point
curl http://127.0.0.1:3000/api_function # Call Lambda function via API gateway
curl http://127.0.0.1:3000/call_api_function # Call Lambda function via API gateway
curl http://127.0.0.1:3000/call_docker # Call Lambda function via API gateway to call Docker
curl http://127.0.0.1:3000/call_function # Call Lambda function via API gateway to call another lambda function directly
curl http://127.0.0.1:5001 # Docker calling Lambda function directly
aws lambda invoke --function-name "CallByFunction" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt
cd ./sam/sam-function
sam local invoke --no-event CallByFunction # By Sam
sam local generate-event sns notification --message "Hello SNS" | sam local invoke CallBySNS
```

### Debugging

```powershell
cd .\sam\sam-api
sam build --use-container # This takes a while downloading container first time, need interest access to download Python libraries
sam local start-api --host 0.0.0.0 -d 5890 # open port
curl http://127.0.0.1:3000/call_debug
```

### Docker: Change code in container `function_user`

- Edit function_target and save
- `docker-compose stop function_user`
- `docker-compose build function_user`
- `docker-compose up -d --no-deps function_user`

Or do it all in one go

- `docker-compose stop function_user;docker-compose build function_user;docker-compose up -d --no-deps function_user`

## Networking

To allow lambda running locally, in a docker container, and other docker containers to reference each other a hostname is required. Using docker version `18.03` under Windows and MacOS you can use `host.docker.internal`.
For Linux either you may use [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html) or a side car docker container such as [https://github.com/qoomon/docker-host](https://github.com/qoomon/docker-host).
Otherwise adjust your host file to have a hostname in it with the machine's ip address.
