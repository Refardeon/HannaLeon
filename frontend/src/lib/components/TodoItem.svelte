<script lang="ts">
    import {Check, Trash2, Undo2, GripVertical, Pencil} from 'lucide-svelte';

    interface Props {
        task: string;
        done: boolean;
        onToggle: () => void;
        onDelete: () => void;
        onEdit: (task: string) => void;
        onDragStart?: (event: DragEvent) => void;
        onDragEnd?: (event: DragEvent) => void;
        onDragOver?: (event: DragEvent) => void;
    }

    let {task, done, onToggle, onDelete, onEdit, onDragStart, onDragEnd, onDragOver}: Props = $props();
    let showDeleteConfirm = $state<boolean>(false);
    let dragging = $state<boolean>(false);
    let editing = $state<boolean>(false);

    function handleDelete() {
        showDeleteConfirm = true;
    }

    function confirmDelete() {
        onDelete();
        showDeleteConfirm = false;
    }

    function cancelDelete() {
        showDeleteConfirm = false;
    }

    function handleDragStart(event: DragEvent) {
        dragging = true;
        onDragStart?.(event);
    }

    function handleDragEnd(event: DragEvent) {
        dragging = false;
        onDragEnd?.(event);
    }

    function edit() {
        editing = true;
    }

    function executeEdit(event: KeyboardEvent) {
        if (event.key === 'Enter') {
            onEdit(task)
            editing = false;
        }
        else if (event.key === 'Escape') {
            editing = false;
        }

    }
</script>

<li
        class="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow group {dragging ? 'opacity-50' : ''}"
        draggable="true"
        ondragstart={handleDragStart}
        ondragend={handleDragEnd}
        ondragover={onDragOver}
>
    <div class="flex items-center justify-between">
        {#if showDeleteConfirm}

            <span class="text-red-600 font-medium px-4">Wirklich löschen?</span>
            <div class="flex gap-2">
                <button
                        onclick={confirmDelete}
                        class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md text-sm font-medium transition-colors"
                >
                    Ja, löschen
                </button>
                <button
                        onclick={cancelDelete}
                        class="bg-gray-300 hover:bg-gray-400 text-gray-700 px-4 py-2 rounded-md text-sm font-medium transition-colors"
                >
                    Abbrechen
                </button>
            </div>

        {:else if editing}
            <input type="text" class="bg-gray-100 px-4 py-2 rounded-md w-full focus:outline-none" bind:value={task}
                   onkeydown={executeEdit}/>
        {:else}
            <!-- Normale Ansicht -->
            <div class="flex items-center gap-3 flex-1">
                <GripVertical class="w-5 h-5 text-gray-400 cursor-grab active:cursor-grabbing"/>
                <span class="flex-1 {done ? 'text-gray-400 line-through' : 'text-gray-700'}">
                {task}
            </span>
            </div>
            <div class="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <button
                        onclick={onToggle}
                        class="{done ? 'bg-yellow-500 hover:bg-yellow-600' : 'bg-green-500 hover:bg-green-600'} text-white px-3 py-1 rounded-md text-sm font-medium transition-colors"
                >
                    {#if done}
                        <Undo2 class="w-4 h-4"/>
                    {:else}
                        <Check class="w-4 h-4"/>
                    {/if}
                </button>
                <button
                        onclick={edit}
                        class="bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded-md text-sm font-medium transition-colors"
                >
                    <Pencil class="w-4 h-4"/>
                </button>
                <button
                        onclick={handleDelete}
                        class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-md text-sm font-medium transition-colors"
                >
                    <Trash2 class="w-4 h-4"/>
                </button>
            </div>
        {/if}
    </div>
</li>