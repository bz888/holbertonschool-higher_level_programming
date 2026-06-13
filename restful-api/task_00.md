# HTTP and HTTPS Summary

HTTP is unencrypted communication between a client and server. HTTPS is HTTP plus TLS encryption, which protects data in transit, verifies the server's identity, and helps prevent tampering.

## HTTP Request and Response Structure

Request:

```http
GET /users/123 HTTP/1.1
Host: example.com
Authorization: Bearer token

optional body
```

Response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id":123}
```

## Common HTTP Methods

| Method | Description | Use Case |
|---|---|---|
| GET | Retrieves data | Fetch a web page or API data |
| POST | Creates or submits data | Submit a form or create a user |
| PUT | Replaces a resource | Update an entire profile |
| PATCH | Partially updates data | Change only a user's email |
| DELETE | Removes a resource | Delete an account or record |

## Common HTTP Status Codes

| Code | Description | Scenario |
|---|---|---|
| 200 | OK | Request succeeded |
| 201 | Created | New resource was created |
| 400 | Bad Request | Invalid input or malformed request |
| 401 | Unauthorized | Login or token required |
| 403 | Forbidden | User lacks permission |
| 404 | Not Found | Resource does not exist |
| 500 | Server Error | Unexpected server failure |