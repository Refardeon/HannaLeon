<script lang="ts">
    import '$lib/css/style.css'
    import favicon from '$lib/assets/HL2_favicon.svg';
    import logo from '$lib/assets/HL2.svg';
    import {authStore} from '$lib/stores/auth.svelte';
    import {goto} from '$app/navigation';
    import {authApi} from "$lib/api/auth";


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


<header class="p-3 bg-amber-50">
    <div>
        <a href="/">
            <img src={logo} class="w-12 h-12 inline mx-5" alt="HL"/>
        </a>
        <h1 class="inline">Hanna und Leon</h1>
    </div>
    {#if authStore.isAuthenticated}
        <div class="flex items-center gap-4">
            <span class="text-gray-700">Hi, {authStore.user?.username}!</span>
            <button
                    onclick={handleLogout}
                    class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded"
            >
                Logout
            </button>
        </div>
    {/if}

</header>

<div class="flex flex-row">

    <nav class="flex-none bg-amber-50 w-1/6 h-screen *:width-full *:block *:p-5 *:hover:bg-amber-100">
        <a href="/liste">Liste</a>
    </nav>

    <div class="flex-auto">
        {@render children()}
    </div>

</div>
