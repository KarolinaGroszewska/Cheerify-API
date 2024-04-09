# Cheerify API
Welcome to the Cheerify API documentation! This API allows you to integrate positive affirmations into your applications. Spread joy and positivity effortlessly with Cheerify!

Built with Flask, hosted on PythonAnywhere.

## Table of Contents
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
  - [1. Get Random Message](#1-get-message)
  - [2. Get Random Message by Category](#2-get-message-by-category)
  - [3. Get Random Favorite Message for User Category](#3-get-favorite-by-UserID)
  - [4. Get Random Custom Message for User Category](#4-get-custom-by-UserID)
- [Response Formats](#response-formats)
- [Contributing](#contributing)
  
## Getting Started

To use the Cheerify API, head to the [website](http://karigroszewska.pythonanywhere.com/)

## Endpoints

### 1. Get Message
```
GET /
```
Returns a random affirmation.

### 2. Get Message by Category
```
GET /{category_name}
```
Returns an affirmation from the specified category. The current categories in Cheerify are
- Acceptance
- Gratitude
- Self-love
- Love
- Friendship
- Family
- Work
- School
- Health
- Wealth
- Happiness
- Success

### 3. Get Favorite by UserID
```
GET /users/{user_id}/favorite
```
Return a random affirmation marked as a favorite for the given user ID.

### 4. Get Custom by UserID
```
GET /users/{user_id}/custom
```
Return a random custom affirmationfor the given user ID.

## Response Formats
The API responses are returned in JSON format, with the following structure:
```json
{
  "category": "{category_name}", "id": "{number}", "string": "{affirmation}"
}
```

## Contributing
We welcome contributions from the community! If you have any ideas for improvements or would like to report a bug, please submit an issue or a pull request on our GitHub repository.
