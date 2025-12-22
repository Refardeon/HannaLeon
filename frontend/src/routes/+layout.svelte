<script lang="ts">
    import '$lib/css/style.css'
    import favicon from '$lib/assets/HL2_favicon.svg';
    import logo from '$lib/assets/HL2.svg';
    import {authStore} from '$lib/stores/auth.svelte';
    import {goto} from '$app/navigation';
    import {authApi} from "$lib/api/auth";
    import {LogOut, User} from 'lucide-svelte';


    let {children} = $props();

    async function handleLogout() {
        await authApi.logout();
        authStore.logout();
        goto('/login');
    }
</script>

<svelte:head>
    <link rel="icon" href={favicon} style="background-color: white"/>
</svelte:head>

<div class="min-h-screen bg-gradient-to-br from-amber-50 via-orange-50 to-yellow-50">
    <header class="bg-white/80 backdrop-blur-md border-b border-amber-200 sticky top-0 z-10 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
            <a href="/" class="flex items-center gap-3 hover:opacity-80 transition-opacity">
                <img src={logo} class="w-12 h-12" alt="HL"/>
                <h1 class="text-2xl font-bold bg-gradient-to-r from-amber-600 to-orange-600 bg-clip-text text-transparent">
                    Hanna & Leon
                </h1>
            </a>


            {#if authStore.isAuthenticated}
                <div class="flex items-center gap-4">
                    <div class="flex items-center gap-2 px-4 py-2 bg-amber-100 rounded-full">
                        <User class="w-4 h-4 text-amber-700"/>
                        <span class="text-sm text-amber-900 font-bold">{authStore.user?.username}</span>
                    </div>
                    <button
                            onclick={handleLogout}
                            class="flex items-center gap-2 px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-lg transition-colors shadow-sm">
                        <LogOut class="w-4 h-4"/>
                    </button>
                </div>
            {/if}
        </div>
    </header>

    {#if authStore.isAuthenticated}
        <div class="flex max-w-7xl mx-auto">
            <!-- Sidebar Navigation -->
            <nav class="w-64 p-6 space-y-2">
                <a
                    href="/liste"
                    class="flex items-center gap-3 px-4 py-3 rounded-xl hover:bg-white/60 transition-all text-amber-900 font-medium hover:shadow-sm"
                >
                    <span class="text-2xl">📝</span>
                    Die Liste
                </a>
                <!-- Weitere Links hier -->
            </nav>

            <!-- Content Area -->
            <main class="flex-1 p-6">
                {@render children()}
            </main>
        </div>
    {:else}
        <main>
            {@render children()}
        </main>
    {/if}
</div>

