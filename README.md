# PARROT AI API Documentation

## 1. Introduction

Welcome to the PARROT AI API! This API provides a robust set of endpoints for user authentication, account management, and user interactions, enabling developers to integrate XYZ features into their applications efficiently.

## 2. Config

- **Version**: 1.0
- **Base URL**: `http://joinparrot.ai:8499/api/v1.0`

## 3. API

### 3.1 User

#### Register User

- **Path**: `/rest/user/register`
- **Method**: POST
- **Body** (application/json): Includes `username`, `name`, `full_name`, `email`, `phone_number`, `avatar`, `metadata`, and `password`.
- **Responses**:
  - `200 OK` for success.
  - `400 Validation Error` for invalid inputs.

#### Logging In

- **Endpoint**: `/rest/user/login`
- **Method**: POST
- **Authorization**: HTTPBasic
- **Response**: Returns a token on successful authentication.

#### Refresh Token

- **Endpoint**: `/rest/user/refresh_token`
- **Method**: POST
- **Authorization**: OAuth2PasswordBearer
- **Body**: `refresh_token=<your_refresh_token>`
- **ContentType**: `application/x-www-form-urlencoded`

#### User Profile

- **POST**: `/rest/user/me`
- **Authorization**: OAuth2PasswordBearer
- **Responses**: `200 OK` on success.

### 3.2 Task Management

#### Create SD Task

- **Path**: `/rest/task/create_sd_task`
- **Authorization**: OAuth2PasswordBearer
- **Body** (application/json): Requires `prompt` and `config` object.

#### Create SDXL Task

- **POST**: `/rest/task/create_sdxl_task`
- **Authorization**: OAuth2PasswordBearer
- **Body** (application/json): Requires `prompt` and `config` object.

#### Get SD Task Result

- **POST**: `/rest/task/get_result_sd_task`
- **Authorization**: OAuth2PasswordBearer
- **Body** (application/json): Requires `task_id`.

#### Task History

- **GET**: `/rest/task/get_task_history`
- **Responses**: `200 OK` on success.

#### Result Feedback

- **POST**: `/rest/task/user_feedback`
- **Authorization**: OAuth2PasswordBearer
- **Body** (application/json): Requires `image_id`, optionally includes `is_like`, `is_dislike`, and `feedback`.

## 4. Example Usage

### Register User

```bash
curl -X POST http://joinparrot.ai:8499/api/v1.0/rest/user/register \
-H "Content-Type: application/json" \
-d '{
  "username": "user",
  "password": "pass",
  "email": "user@example.com"
}'
```

### Login User

```bash
curl -X POST http://joinparrot.ai:8499/api/v1.0/rest/user/login \
-H "Authorization: Basic <base64-encoded-credentials>"
```

### Refresh Token

```bash
curl -X POST http://joinparrot.ai:8499/api/v1.0/rest/user/refresh_token \
-H "Authorization: Bearer <your_access_token>" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "refresh_token=<your_refresh_token>"
```

## 5. Error Handling

The API uses standard HTTP response codes to indicate the success or failure of requests. In case of errors, a detailed message will be returned in the format:

```json
{
  "detail": [
    {
      "loc": ["body", "username"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## Support

For further assistance or to report issues, please contact our support team at support@joinparrot.ai.

This README provides a concise overview of how to interact with the PARROT AI API. For a complete reference, including all endpoints and detailed request/response models, please refer to the full API documentation.
