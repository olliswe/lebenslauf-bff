# Models

## User


```
interface User {
    id:string;
    email:string;
    password:string;
    profile: UserProfile,
}
```

## UserProfile


```
interface UserProfile {
    first_name:string;
    last_name:string;
    subscription: 'FREE' | 'PAID'
    subscription_start_date?: date;
    subscription_end_date?: date;
}

```


## CV

```
interface CV {
    name:string;
    position?:string;
    bio?:string;
    location?:string;
    email?:string;
    phone?:string;
    homepage_url?:string;
    linkedin_url?:string;
    education_entries:EducationJSON[];
    experience_entries: ExperienceJSON[];
    personal_project_entries: PersonalProjectJSON[];
    skills?: string[]
}
```



## EducationJSON

```
interface EducationJSON {
    institution:string;
    degree:string;
    start_year:integer;
    end_year?:integer;
    description?:string;
    current:boolean (default=false);
}
```


## ExperienceJSON

```
interface ExperienceJSON {
    role:string;
    company:string;
    start_month:integer;
    start_year:integer;
    end_month?:integer;
    current:boolean (default=false);
    tech_stack: string[];
    github_project_url?: string;
}
```



## PersonalProjectJSON


```.env
interface PersonalProjectJSON {
    name:string;
    description?:string;
    tech_stack: string[];
    github_project_url?: string;
}
```





