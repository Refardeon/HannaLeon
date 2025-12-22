import {authStore} from '$lib/stores/auth.svelte';

import {env} from '$env/dynamic/public'
import {browser} from '$app/environment';

class Client {

    private get baseUrl() {
        if (browser) {
            return env.PUBLIC_CLIENT_API_URL || 'http://localhost:8000';
        }
        return env.PUBLIC_SERVER_API_URL || 'http://backend:8000';
    }


    private async request<T>(
        endpoint: string,
        options?: RequestInit
    ): Promise<T> {
        const url = `${this.baseUrl}${endpoint}`;

        const config: RequestInit = {
            ...options,
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                ...options?.headers,
            },
        };

        try {
            const response = await fetch(url, config);

            if (response.status === 401) {
                if (browser) {
                    window.location.href = '/login';
                }
                throw new Error(`Unauthorized access to ${response.url}`);
            }

            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} ${response.statusText}`);
            }

            if (response.status === 204) {
                return null as T;
            }

            return await response.json();
        } catch (error) {
            console.error('API Request failed:', error);
            throw error;
        }
    }

    async get<T>(endpoint: string): Promise<T> {
        return this.request<T>(endpoint, {method: 'GET'});
    }

    async post<T>(endpoint: string, data: unknown): Promise<T> {
        return this.request<T>(endpoint, {
            method: 'POST',
            body: JSON.stringify(data),
        });
    }

    async patch<T>(endpoint: string, data: unknown): Promise<T> {
        return this.request<T>(endpoint, {
            method: 'PATCH',
            body: JSON.stringify(data),
        });
    }

    async delete<T>(endpoint: string): Promise<T> {
        return this.request<T>(endpoint, {method: 'DELETE'});
    }
}

export const apiClient = new Client();
