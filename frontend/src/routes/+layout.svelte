<script lang="ts">
    import '$lib/css/style.css'
    import favicon from '$lib/assets/HL2_favicon.svg';
    import logo from '$lib/assets/HL2.svg';
    import {authStore} from '$lib/stores/auth.svelte.js';
    import {authApi} from '$lib/api/auth';
    import {goto} from '$app/navigation';
    import {LogOut, User, Menu, X} from 'lucide-svelte';

    let {children} = $props();
    let mobileMenuOpen = $state(false);

    async function handleLogout() {
        await authApi.logout();
        authStore.logout();
        goto('/login');
    }

    function closeMobileMenu() {
        mobileMenuOpen = false;
    }
</script>

<svelte:head>
    <link rel="icon" href={favicon} style="background-color: white"/>
</svelte:head>

<div class="min-h-screen bg-gradient-to-br from-amber-50 via-orange-50 to-yellow-50">
    <!-- Header -->
    <header class="bg-white/80 backdrop-blur-md border-b border-amber-200 sticky top-0 z-50 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
            <a href="/static" class="flex items-center gap-3 hover:opacity-80 transition-opacity">
                <img src={logo} class="w-10 h-10 md:w-12 md:h-12" alt="HL"/>
                <h1 class="text-xl md:text-2xl font-bold bg-gradient-to-r from-amber-600 to-orange-600 bg-clip-text text-transparent">
                    Hanna & Leon
                </h1>
            </a>

            {#if authStore.isAuthenticated}
                <div class="flex items-center gap-2 md:gap-4">
                    <!-- Desktop User Info -->
                    <div class="hidden md:flex items-center gap-2 px-4 py-2 bg-amber-100 rounded-full">
                        <User class="w-4 h-4 text-amber-700"/>
                        <span class="text-sm font-medium text-amber-900">{authStore.user?.username}</span>
                    </div>

                    <!-- Desktop Logout -->
                    <button
                            onclick={handleLogout}
                            class="hidden md:flex items-center gap-2 px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-lg transition-colors shadow-sm"
                    >
                        <LogOut class="w-4 h-4"/>
                        Logout
                    </button>

                    <!-- Mobile Hamburger -->
                    <button
                            onclick={() => mobileMenuOpen = !mobileMenuOpen}
                            class="md:hidden p-2 hover:bg-amber-100 rounded-lg transition-colors"
                            aria-label="Menu"
                    >
                        {#if mobileMenuOpen}
                            <X class="w-6 h-6 text-amber-900"/>
                        {:else}
                            <Menu class="w-6 h-6 text-amber-900"/>
                        {/if}
                    </button>
                </div>
            {/if}
        </div>

        <!-- Mobile Menu Dropdown -->
        {#if authStore.isAuthenticated && mobileMenuOpen}
            <div class="md:hidden border-t border-amber-200 bg-white">
                <nav class="px-4 py-4 space-y-2">
                    <a
                            href="/liste"
                            onclick={closeMobileMenu}
                            class="flex items-center gap-3 px-4 py-3 rounded-xl hover:bg-amber-50 transition-all text-amber-900 font-medium"
                    >
                        <span class="text-xl">📝</span>
                        Die Liste
                    </a>

                    <div class="border-t border-amber-100 my-2"></div>

                    <div class="flex items-center gap-2 px-4 py-2 bg-amber-50 rounded-lg">
                        <User class="w-4 h-4 text-amber-700"/>
                        <span class="text-sm font-medium text-amber-900">{authStore.user?.username}</span>
                    </div>

                    <button
                            onclick={handleLogout}
                            class="w-full flex items-center justify-center gap-2 px-4 py-3 bg-red-500 hover:bg-red-600 text-white rounded-lg transition-colors"
                    >
                        <LogOut class="w-4 h-4"/>
                        Logout
                    </button>
                </nav>
            </div>
        {/if}
    </header>

    <!-- Main Content -->
    {#if authStore.isAuthenticated}
        <div class="flex max-w-7xl mx-auto">
            <!-- Desktop Sidebar Navigation -->
            <nav class="hidden md:block w-64 p-6 space-y-2">
                <a
                        href="/liste"
                        class="flex items-center gap-3 px-4 py-3 rounded-xl hover:bg-white/60 transition-all text-amber-900 font-medium hover:shadow-sm"
                >
                    <span class="text-2xl">📝</span>
                    Die Liste
                </a>
            </nav>

            <!-- Content Area -->
            <main class="flex-1 p-4 md:p-6">
                {@render children()}
            </main>
        </div>
    {:else}
        <main>
            {@render children()}
        </main>
    {/if}
</div>

