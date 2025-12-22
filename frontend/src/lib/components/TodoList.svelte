<script lang="ts">
    import TodoItem from './TodoItem.svelte';
    import type {TodoItemType} from '../types';

    interface Props {
        items: TodoItemType[];
        title: string;
        onToggle: (id: number) => void;
        onDelete: (id: number) => void;
        onEdit: (id: number, task: string) => void;
        onReorder: (items: TodoItemType[]) => void;
    }

    let { items, title, onToggle, onDelete, onEdit, onReorder }: Props = $props();
    let draggedId = $state<number | null>(null);

    function handleDragStart(id: number) {
        draggedId = id;
    }

    function handleDragEnd() {
        draggedId = null;
    }

    function handleDragOver(event: DragEvent, targetId: number) {
        event.preventDefault();

        if (draggedId === null || draggedId === targetId) return;

        const draggedIndex = items.findIndex(t => t.id === draggedId);
        const targetIndex = items.findIndex(t => t.id === targetId);

        if (draggedIndex === -1 || targetIndex === -1) return;

        const reorderedItems = [...items];
        const [draggedItem] = reorderedItems.splice(draggedIndex, 1);
        reorderedItems.splice(targetIndex, 0, draggedItem);

        onReorder(reorderedItems);
    }
</script>

{#if items.length > 0}
    <div class="mb-8">
        <h2 class="text-2xl font-bold text-gray-800 mb-4">{title}</h2>
        <ul class="space-y-3">
            {#each items as item (item.id)}
                <TodoItem
                    id={item.id}
                    task={item.task}
                    done={item.done}
                    isDragging={draggedId === item.id}
                    onToggle={() => onToggle(item.id)}
                    onDelete={() => onDelete(item.id)}
                    onEdit={(task) => onEdit(item.id, task)}
                    onDragStart={() => handleDragStart(item.id)}
                    onDragEnd={handleDragEnd}
                    onDragOver={(e) => handleDragOver(e, item.id)}
                />
            {/each}
        </ul>
    </div>
{/if}
