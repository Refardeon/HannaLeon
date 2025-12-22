<script lang="ts">
    import TodoList from '$lib/components/TodoList.svelte';
    import type {TodoItemType} from '$lib/types';
    import {todosApi} from "$lib/api/todos";
    import type {PageData} from './$types'
    import {Plus} from 'lucide-svelte';


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

<div class="max-w-4xl mx-auto">
    <!-- Header -->
    <div class="mb-6 md:mb-8">
        <h1 class="text-4xl font-bold text-gray-800 mb-2">Die Liste</h1>
    </div>

    <!-- Input Card -->
    <div class="bg-white rounded-2xl shadow-lg p-4 md:p-6 mb-6 md:mb-8 border border-amber-100">
        <div class="flex gap-3">
            <div class="relative flex-1">
                <input
                        bind:value={newItem}
                        onkeydown={addItem}
                        placeholder="Neuen Punkt hinzufügen..."
                        class="w-full px-4 py-3 md:py-4 pr-12 border-2 border-gray-200 rounded-xl focus:outline-none focus:border-amber-500 transition-colors text-base md:text-lg"
                />
                <div class="absolute right-4 top-1/2 -translate-y-1/2">
                    <Plus class="w-5 h-5 md:w-6 md:h-6 text-gray-400" />
                </div>
            </div>
        </div>
        <p class="text-xs md:text-sm text-gray-500 mt-2 md:mt-3">💡 Drücke Enter zum Hinzufügen</p>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-2 gap-3 md:gap-4 mb-6 md:mb-8">
        <div class="bg-gradient-to-br from-green-100 to-emerald-100 rounded-xl p-3 md:p-4 border border-green-200">
            <p class="text-xs md:text-sm text-green-700 font-medium mb-1">Noch vor uns</p>
            <p class="text-2xl md:text-3xl font-bold text-green-900">{activeTodos.length}</p>
        </div>
        <div class="bg-gradient-to-br from-blue-100 to-indigo-100 rounded-xl p-3 md:p-4 border border-blue-200">
            <p class="text-xs md:text-sm text-blue-700 font-medium mb-1">Schon gemacht</p>
            <p class="text-2xl md:text-3xl font-bold text-blue-900">{doneTodos.length}</p>
        </div>
    </div>

    <div class="space-y-6 md:space-y-8">
        <TodoList
                items={activeTodos}
                title="Noch vor uns"
                onToggle={toggleTodo}
                onDelete={deleteTodo}
                onEdit={editTodo}
                onReorder={reorderActive}
        />

        <TodoList
                items={doneTodos}
                title="Schon gemacht"
                onToggle={toggleTodo}
                onDelete={deleteTodo}
                onEdit={editTodo}
                onReorder={reorderDone}
        />
    </div>
</div>