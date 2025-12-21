
import { todosApi } from '$lib/api/todos';
import type { PageLoad } from './$types';

export const load: PageLoad = async () => {
    try {
        const todos = await todosApi.getAll();
        return { todos };
    } catch (error) {
        console.error('Failed to load todos:', error);
        return { todos: [] };
    }
};
