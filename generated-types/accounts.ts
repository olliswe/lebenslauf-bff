export interface ReadEducationEntrySerializer {
    id?: number;
    institution: string;
    degree: string;
    start_date: string;
    end_date?: string;
    description?: string;
    current?: boolean;
    cv: any;
}

export interface ReadExperienceEntrySerializer {
    id?: number;
    role: string;
    company: string;
    location: string;
    start_date: string;
    end_date?: string;
    current?: boolean;
    description?: string;
    cv: any;
}

export interface ReadPersonalProjectSerializer {
    id?: number;
    name: string;
    description?: string;
    start_date?: string;
    end_date?: string;
    github_project_url?: string;
    cv: any;
}

export interface ReadSkillsSerializer {
    id?: number;
    name: string;
}

export interface ReadCVSerializer {
    id?: number;
    user: any;
    name: string;
    position: string;
    bio: string;
    location: string;
    email: string;
    phone: string;
    homepage_url?: string;
    linkedin_url?: string;
    created_at?: string;
    updated_at?: string;
    education_entries: ReadEducationEntrySerializer[];
    experience_entries: ReadExperienceEntrySerializer[];
    personal_project_entries: ReadPersonalProjectSerializer[];
    skills: ReadSkillsSerializer[];
}

export interface WriteCVSerializer {
    user: any;
    name: string;
    position: string;
    bio: string;
    location: string;
    email: string;
    phone: string;
    homepage_url?: string;
    linkedin_url?: string;
}

export interface WriteSkillSerializer {
    name: string;
}

export interface WriteExperienceEntriesSerializer {
    id?: number;
    cv: any;
    role: string;
    company: string;
    location: string;
    start_date: string;
    end_date?: string;
    current?: boolean;
    description?: string;
}

export interface WritePersonalProjectsSerializer {
    id?: number;
    cv: any;
    name: string;
    description?: string;
    start_date?: string;
    end_date?: string;
    github_project_url?: string;
}

export interface WriteEducationEntriesSerializer {
    id?: number;
    cv: any;
    institution: string;
    degree: string;
    start_date: string;
    end_date?: string;
    description?: string;
    current?: boolean;
}

export interface UserProfileSerializer {
    subscription?: any;
}

export interface UserSerializer {
    id?: number;
    last_login?: string;
    is_superuser?: boolean;
    username: string;
    first_name?: string;
    last_name?: string;
    email?: string;
    is_staff?: boolean;
    is_active?: boolean;
    date_joined?: string;
    user_profile: UserProfileSerializer;
}

