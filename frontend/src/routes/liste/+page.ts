import {todosApi} from '$lib/api/todos';
import type {PageLoad} from './$types';
import {authApi} from "$lib/api/auth";

export const ssr = false;

export const load: PageLoad = async () => {
    await authApi.auth_or_login()
    const todos = await todosApi.getAll();
    return {todos};
};
