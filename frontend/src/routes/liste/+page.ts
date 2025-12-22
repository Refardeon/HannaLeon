import {redirect} from '@sveltejs/kit';
import {authStore} from '$lib/stores/auth.svelte';
import {todosApi} from '$lib/api/todos';
import type {PageLoad} from './$types';
import {authApi} from "$lib/api/auth";

export const ssr = false;

export const load: PageLoad = async () => {
    try {
        const user = await authApi.getMe();
        authStore.setUser(user);

        const todos = await todosApi.getAll();
        return {todos};
    } catch (error) {
        throw redirect(302, '/login');
    }
};
