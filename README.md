# big-peer
combination of wirehole and wg-easy

## API
### Authentication
```bash
curl --url <your server ip>:<port>/api/session -X POST -H "Content-Type: application/json" \
-d "{\"password\": \"<your password>\"}" --cookie-jar cookies.txt
```
below curl command will create file with session required for api authorization

### Get clients list example
```bash
curl --url <your server ip>:<port>/api/wireguard/client -X GET "Content-Type: application/json"
--cookie cookies.txt
```
