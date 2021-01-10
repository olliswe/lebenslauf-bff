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

