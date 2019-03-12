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
