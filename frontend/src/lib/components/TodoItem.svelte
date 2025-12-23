<script lang="ts">
    import {Check, Trash2, Undo2, GripVertical, Pencil} from 'lucide-svelte';

    interface Props {
        id: number;
        task: string;
        done: boolean;
        isDragging?: boolean;
        onToggle: () => void;
        onDelete: () => void;
        onEdit: (task: string) => void;
        onDragStart?: () => void;
        onDragEnd?: () => void;
        onDragOver?: (event: DragEvent) => void;
    }

    let { id, task, done, isDragging = false, onToggle, onDelete, onEdit, onDragStart, onDragEnd, onDragOver }: Props = $props();
    let showDeleteConfirm = $state<boolean>(false);
    let editing = $state<boolean>(false);
    let editedTask = $state<string>(task);
    let showButtons = $state<boolean>(false); // Für Mobile: Buttons immer sichtbar

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

    function startEdit() {
        editing = true;
        editedTask = task;
    }

    function saveEdit() {
        if (editedTask.trim()) {
            onEdit(editedTask.trim());
        }
        editing = false;
    }

    function cancelEdit(event: KeyboardEvent) {
        if (event.key === 'Escape') {
            editing = false;
            editedTask = task;
        } else if (event.key === 'Enter') {
            saveEdit();
        }
    }

    function toggleButtons() {
        showButtons = !showButtons;
    }
</script>

<li
    class="bg-white rounded-xl shadow-md p-4 transition-all border-2 border-transparent hover:border-amber-200 {isDragging ? 'opacity-50 scale-95' : ''} {showButtons ? 'border-amber-300' : ''}"
    draggable="true"
    ondragstart={onDragStart}
    ondragend={onDragEnd}
    ondragover={onDragOver}
>
    {#if showDeleteConfirm}
        <!-- Bestätigungs-Ansicht -->
        <div class="flex flex-col sm:flex-row items-center justify-between gap-3">
            <span class="text-red-600 font-medium">Wirklich löschen?</span>
            <div class="flex gap-2 w-full sm:w-auto">
                <button
                    onclick={confirmDelete}
                    class="flex-1 sm:flex-none bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg text-sm font-medium transition-colors"
                >
                    Ja, löschen
                </button>
                <button
                    onclick={cancelDelete}
                    class="flex-1 sm:flex-none bg-gray-300 hover:bg-gray-400 text-gray-700 px-4 py-2 rounded-lg text-sm font-medium transition-colors"
                >
                    Abbrechen
                </button>
            </div>
        </div>
    {:else if editing}
        <!-- Edit-Ansicht -->
        <div class="flex gap-2">
            <input
                type="text"
                bind:value={editedTask}
                onkeydown={cancelEdit}
                onblur={saveEdit}
                class="flex-1 bg-amber-50 px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500"
            />
        </div>
    {:else}
        <!-- Normale Ansicht -->
        <div class="flex items-center gap-3">
            <!-- Drag Handle - Nur Desktop -->
            <button
                class="hidden sm:block cursor-grab active:cursor-grabbing touch-none"
                aria-label="Drag"
            >
                <GripVertical class="w-5 h-5 text-gray-400" />
            </button>

            <!-- Task Text -->
            <button
                onclick={toggleButtons}
                class="flex-1 text-left {done ? 'text-gray-400 line-through' : 'text-gray-700'}"
            >
                {task}
            </button>

            <!-- Buttons - Desktop: hover, Mobile: toggle -->
            <div class="flex gap-2 {showButtons ? 'opacity-100' : 'opacity-0 sm:group-hover:opacity-100'} transition-opacity">
                <button
                    onclick={onToggle}
                    class="{done ? 'bg-yellow-500 hover:bg-yellow-600' : 'bg-green-500 hover:bg-green-600'} text-white p-2 rounded-lg transition-colors shadow-sm"
                    aria-label={done ? 'Rückgängig' : 'Erledigt'}
                >
                    {#if done}
                        <Undo2 class="w-4 h-4" />
                    {:else}
                        <Check class="w-4 h-4" />
                    {/if}
                </button>
                <button
                    onclick={startEdit}
                    class="bg-blue-600 hover:bg-blue-700 text-white p-2 rounded-lg transition-colors shadow-sm"
                    aria-label="Bearbeiten"
                >
                    <Pencil class="w-4 h-4" />
                </button>
                <button
                    onclick={handleDelete}
                    class="bg-red-500 hover:bg-red-600 text-white p-2 rounded-lg transition-colors shadow-sm"
                    aria-label="Löschen"
                >
                    <Trash2 class="w-4 h-4" />
                </button>
            </div>
        </div>
    {/if}
</li>
