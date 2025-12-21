import {apiClient} from './client';
import type {TodoItemType} from '$lib/types';

export interface TodoCreate {
    task: string;
    done?: boolean;
}

export interface TodoUpdate {
    task?: string;
    done?: boolean;
}

export interface TodoReorder {
    id: number;
    order: number;
}

export const todosApi = {
    async getAll(): Promise<TodoItemType[]> {
        return apiClient.get<TodoItemType[]>('/todos');
    },

    async getById(id: number): Promise<TodoItemType> {
        return apiClient.get<TodoItemType>(`/todos/${id}`);
    },

    async create(todo: TodoCreate): Promise<TodoItemType> {
        return apiClient.post<TodoItemType>('/todos', todo);
    },

    async update(id: number, todo: TodoUpdate): Promise<TodoItemType> {
        return apiClient.patch<TodoItemType>(`/todos/${id}`, todo);
    },

    async delete(id: number): Promise<void> {
        return apiClient.delete<void>(`/todos/${id}`);
    },

    async toggle(id: number, done: boolean): Promise<TodoItemType> {
        return this.update(id, {done});
    },

    async reorder(items: TodoReorder[]): Promise<void> {
        return apiClient.patch<void>('/todos/reorder', items);
    },
};
