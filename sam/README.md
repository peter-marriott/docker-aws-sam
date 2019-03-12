# Run Sam app

Build and test it works

```Powershell
cd sam-api
sam build --use-container # This takes a while downloading container first time
sam local start-api --host 0.0.0.0 # Allow requests from non localhost
```

```Powershell
cd sam-function
sam build --use-container # This takes a while downloading container first time
sam local start-lambda --host 0.0.0.0
```

```
curl -L http://127.0.0.1:3000/hello1
curl -L http://127.0.0.1:3000/hello2
curl -L http://127.0.0.1:3000/hello3
```