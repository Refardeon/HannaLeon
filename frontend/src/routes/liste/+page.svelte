<script lang="ts">
    import TodoList from '$lib/components/TodoList.svelte';
    import type {TodoItemType} from '$lib/types';
    import {todosApi} from "$lib/api/todos";
    import type {PageData} from './$types'

    interface Props {
        data: PageData;
    }

    let {data}: Props = $props();
    let todos = $state<TodoItemType[]>(data.todos);
    let newItem = $state<string>("");

    let activeTodos = $derived(todos.filter(t => !t.done));
    let doneTodos = $derived(todos.filter(t => t.done));

    async function addItem(event: KeyboardEvent) {
        if (event.key === "Enter" && newItem.trim()) {
            todos.push(await todosApi.create({task: newItem.trim()}));
            newItem = "";
        }
    }

    async function toggleTodo(id: number) {
        const todo = todos.find(t => t.id === id);
        if (todo) {
            await todosApi.toggle(id, !todo.done);
            todo.done = !todo.done;
        }
    }

    async function editTodo(id: number, task: string) {
        await todosApi.update(id, {task});
        const todo = todos.find(t => t.id === id);
        if (todo) todo.task = task;
    }

    async function deleteTodo(id: number) {
        await todosApi.delete(id);
        todos = todos.filter(t => t.id !== id);
    }

    async function reorderActive(items: typeof activeTodos) {
        todos = [...items, ...doneTodos];

        const reorders = todos.map((todo, index) => ({
            id: todo.id,
            order: index
        }));
        await todosApi.reorder(reorders);
    }

    async function reorderDone(items: typeof doneTodos) {
        todos = [...activeTodos, ...items];

        const reorders = todos.map((todo, index) => ({
            id: todo.id,
            order: index
        }));
        await todosApi.reorder(reorders);
    }
</script>

<div class="min-h-screen py-8 px-4">
    <div class="max-w-3xl mx-auto">
        <h1 class="text-4xl font-bold text-gray-800 mb-8 text-center">Die Liste</h1>

        <!-- Input -->
        <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
            <input
                    bind:value={newItem}
                    onkeydown={addItem}
                    placeholder="Neues cooles Ding"
                    class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:outline-none focus:border-indigo-500 transition-colors"
            />
            <p class="text-sm text-gray-500 mt-2">Drücke Enter zum Hinzufügen</p>
        </div>

        <!-- Active Todos -->
        <TodoList
                items={activeTodos}
                title="Der Spaß liegt noch vor uns"
                onToggle={toggleTodo}
                onDelete={deleteTodo}
                onEdit={editTodo}
                onReorder={reorderActive}
        />

        <!-- Done Todos -->
        <TodoList
                items={doneTodos}
                title="Schon gemacht"
                onToggle={toggleTodo}
                onDelete={deleteTodo}
                onEdit={editTodo}
                onReorder={reorderDone}
        />

        {#if todos.length === 0}
            <div class="text-center text-gray-500 bg-white rounded-lg shadow-md p-8">
                <p class="text-lg">Hier ist noch nichts, füge was cooles hinzu!</p>
            </div>
        {/if}
    </div>
</div>