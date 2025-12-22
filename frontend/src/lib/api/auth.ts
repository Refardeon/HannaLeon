import {apiClient} from './client';

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
};