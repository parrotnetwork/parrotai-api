# PARROT AI API Documentation

## 1. Introduction

Welcome to the PARROT AI API! This API provides a robust set of endpoints for account management, image generation and model interactions, enabling developers to integrate Parrot AI features into their applications efficiently.

## 2. Getting Started
To use the PARROT AI API, you need an API key. Please visit joinparrot.ai to register and obtain your key. Include this key in the HTTP Authorization header for all your API requests.

## 3. API Document
All details and usage instructions for the APIs are thoroughly documented in our Gitbook. To explore the capabilities of the Parrot AI API, please visit the following link: Parrot AI API Documentation.

## 4. Examples
We have curated a collection of examples demonstrating the integration of the Parrot AI API. These examples cover a range of functionalities, from user management to the creation and retrieval of image generation tasks. You can find these examples in the "Examples" directory for reference and guidance.

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
