# Suggestions App - Whop


## Installing Suggestions App


1. Open a terminal in the directory where you downloaded the repo and activate the Python enviroment
    ```
    python3 -m venv .venv
    ```
    ```
    source .venv/bin/activate
    ```
2. Install Python libraries

    ```
   pip3 install -r requirements.txt
    ```
2. Initialize settings and setup database
    ```
    export FLASK_APP=suggestions
    ```
    ```
    flask shell
    ```
    ```
    from settings import db
    db.create_all()
    ```
    ```
    exit()
    ```
3. Run Flask

    ```
    export FLASK_APP=suggestions
    ```
    ```
    flask run
    ```
## Categories
## Show all categories

**URL** : `/api/categories/all`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
  "categories": [
    {
      "category": "General"
    }, 
    {
      "category": "Feature"
    }, 
    {
      "category": "Bug"
    }, 
    {
      "category": "Other"
    }
  ]
}
```

## Create new category

**URL** : `/api/categories/create`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
  "id": 1
}
```

## Get category by id

**URL** : `/api/categories/<id>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
  "categeory": "General", 
  "suggestions": []
}
```

## Delete category by id

**URL** : `/api/categories/<id>/delete`

**Method** : `DELETE`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

`Deleted Category - {category.title}`

## Suggestions

## Show all suggestions

**URL** : `/api/suggestions/all`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
  "suggestions": [
    {
      "author": "example"
    }
  ]
}
```

## Create new suggestion

**URL** : `/api/suggestions/create`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
  "id": 1
}
```

## Get suggestion by id

**URL** : `/api/suggestions/<id>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
  "author": "", 
  "body": "", 
  "comments": [
    {
      "comment": ""
    }
  ], 
  "downvotes": 0, 
  "upvotes": 0
}

```
## Edit suggestion by id

**URL** : `/api/suggestions/<id>/edit`

**Method** : `PUT`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
  "id": 1
}
```
## Upvote/downvote suggestion by id

**URL** : `/api/suggestions/<id>/vote`

**Method** : `PUT`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
  "votes": {
    "upvotes":0,
    "downvotes":0
    }
  }
```

## Delete suggestion by id

**URL** : `/api/suggestions/<id>/delete`

**Method** : `DELETE`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

`Deleted Suggestion #{suggestion.id} and {len(suggestion.comments)} comments`

## Comments
## Show all comments

**URL** : `/api/comments/all`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
    "suggestions": [

    ]
}
```

## Create new comment

**URL** : `/api/comments/create`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content examples**

```json
{
  "id": 1
}
```
