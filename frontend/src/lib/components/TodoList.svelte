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

    let {items, title, onToggle, onDelete, onEdit, onReorder}: Props = $props();
    let draggedIndex = $state<number | null>(null);

    function handleDragStart(e: DragEvent, index: number) {
        draggedIndex = index;
    }

    function handleDragEnd(e: DragEvent) {
        draggedIndex = null;
    }

    function handleDragOver(e: DragEvent, index: number) {
        e.preventDefault();

        if (draggedIndex === null || draggedIndex === index) return;

        const reorderedItems = [...items];
        const [draggedItem] = reorderedItems.splice(draggedIndex, 1);
        reorderedItems.splice(index, 0, draggedItem);

        onReorder(reorderedItems);
        draggedIndex = index;
    }
</script>

{#if items.length > 0}
    <div class="mb-8">
        <h2 class="text-2xl font-bold text-gray-800 mb-4">{title}</h2>
        <ul class="space-y-3">
            {#each items as item, index}
                <TodoItem
                        task={item.task}
                        done={item.done}
                        onToggle={() => onToggle(item.id)}
                        onDelete={() => onDelete(item.id)}
                        onEdit={(task)=>onEdit(item.id, task)}
                        onDragStart={(e) => handleDragStart(e, index)}
                        onDragEnd={(e) => handleDragEnd(e)}
                        onDragOver={(e) => handleDragOver(e, index)}
                />
            {/each}
        </ul>
    </div>
{/if}