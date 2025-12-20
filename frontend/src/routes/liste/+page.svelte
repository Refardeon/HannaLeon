<script lang="ts">
    import TodoList from '$lib/components/TodoList.svelte';
    import type {TodoItemType} from '$lib/types';

    let todos = $state<TodoItemType[]>([]);
    let newItem = $state<string>("");
    let nextId = $state<number>(0);

    let activeTodos = $derived(todos.filter(t => !t.done));
    let doneTodos = $derived(todos.filter(t => t.done));

    function addItem(event: KeyboardEvent) {
        if (event.key === "Enter" && newItem.trim()) {
            todos.push({
                id: nextId++,
                task: newItem.trim(),
                done: false
            });
            newItem = "";
        }
    }

    function toggleTodo(id: number) {
        const todo = todos.find(t => t.id === id);
        if (todo) {
            todo.done = !todo.done;
        }
    }

    function deleteTodo(id: number) {
        todos = todos.filter(t => t.id !== id);
    }

    function reorderActive(reorderedItems: TodoItemType[]) {
        const doneItems = todos.filter(t => t.done);
        todos = [...reorderedItems, ...doneItems];
    }

    function reorderDone(reorderedItems: TodoItemType[]) {
        const activeItems = todos.filter(t => !t.done);
        todos = [...activeItems, ...reorderedItems];
    }

    function editTodo(id: number, task: string) {
        let todo = todos.find(t=>t.id===id);
        if (todo){
            todo.task = task;
        }
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