## Create CA

openssl req -nodes -new -x509 -days 365 -keyout ca.key -out ca-crt.pem

This will generate private key of your CA (ca.key) and root cert (ca-crt.pem).

## Generate Server Certs

### create server private key and server CSR
```bash openssl req -nodes -new -keyout server.key -out server.csr```

### generate certicate based on server's CSR using CA root certificate and CA private key
```bash openssl x509 -req -days 365 -in server.csr -CA ca-crt.pem -CAkey ca.key -CAcreateserial -out server.crt```

### verify the certificate (optionally)
```bash openssl verify -CAfile ca-crt.pem server.crt```

## Generate Client Certs
### create client private key and client CSR
```bash openssl req -nodes -new -keyout client.key -out client.csr```

### generate certicate based on client's CSR using CA root certificate and CA private key
```bash openssl x509 -req -days 365 -in client.csr -CA ca-crt.pem -CAkey ca.key -CAcreateserial -out client.crt```

### verify the certificate (optionally)
```bash openssl verify -CAfile ca-crt.pem client.crt```


## Testing against Flask dev server
```bash curl --insecure --cacert ca-crt.pem --key client.key --cert client.crt https://localhost:8080/ping```

## Leveraging Gunicorn
```bash gunicorn --bind :8080 --keyfile server.key --certfile server.crt --ca-certs ca-crt.pem --cert-reqs 2 app:app```

