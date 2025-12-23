import {apiClient} from './client';
import {authStore} from "$lib/stores/auth.svelte";
import {redirect} from '@sveltejs/kit';


export interface LoginRequest {
    username: string;
    password: string;
}

export interface LoginResponse {
    user: UserResponse;
}

export interface TokenResponse {
    access_token: string;
    token_type: string;
}

export interface UserResponse {
    id: number;
    username: string;
    logo: number;
}

export interface UpdateUserLogo {
    logo: number;
}

export const authApi = {
    async login(credentials: LoginRequest): Promise<TokenResponse> {
        const formData = new URLSearchParams();
        formData.append('username', credentials.username);
        formData.append('password', credentials.password);

        const response = await fetch(`${apiClient['baseUrl']}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            credentials: 'include',
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Login failed');
        }

        return response.json();
    },

    async getMe(): Promise<UserResponse> {
        return apiClient.get<UserResponse>('/auth/me');
    },
    async logout(): Promise<void> {
        await apiClient.post<void>('/auth/logout', {});
    },

    async setLogo(user_id:number, logo: UpdateUserLogo): Promise<UserResponse> {
        return await apiClient.patch<UserResponse>(`/auth/${user_id}`, logo);
    },

    async auth_or_login() {
        try {
            const user = await authApi.getMe();
            authStore.setUser(user);
        } catch (error) {
            throw redirect(302, '/login');
        }
    },
};