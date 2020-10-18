# Endpoints


## `/accounts`


## `/me`

### `POST /me/register`

```.env
Request

{
    email:string;
    gitHub:????
}
```

### `GET /me`

For getting user info 

```.env
Response

{
    user: User,
    profile: UserProfile,
    githubData: ???
}
```

### `PUT /me`

For updating UserProfile

```.env
Request 

{
    profile: UserProfile
}


Response 

{   
    user: User,
    profile: UserProfile,
    githubData: ???
}
```



## `/cv`

### `GET /cv`

```.env
Response

CV

```

### `PUT /cv`

If there is a CV already => update it

If there is not a CV => create one

```.env
Request

CV


Response

CV

```

