<script lang="ts">
    import { authApi } from '$lib/api/auth';
    import { authStore } from '$lib/stores/auth.svelte';
    import { goto } from '$app/navigation';

    let username = $state('');
    let password = $state('');
    let error = $state('');
    let loading = $state(false);

    async function handleLogin() {
        loading = true;
        error = '';

        try {
            const response = await authApi.login({ username, password });

            authStore.setUser(response.user)
            goto('/liste');
        } catch (err) {
            console.error('Login failed:', err);
            error = 'Login fehlgeschlagen.';
        } finally {
            loading = false;
        }
    }
</script>

<div class="min-h-screen flex items-center justify-center bg-gray-50">
    <div class="max-w-md w-full bg-white rounded-lg shadow-lg p-8">
        <h1 class="text-3xl font-bold text-center mb-8">Login</h1>

        {#if error}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                {error}
            </div>
        {/if}

        <form onsubmit={(e) => { e.preventDefault(); handleLogin(); }}>
            <div class="mb-4">
                <label class="block text-gray-700 mb-2" for="username">Username</label>
                <input
                        name="username"
                        type="text"
                        bind:value={username}
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-indigo-500"
                        required
                />
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 mb-2" for="password_field">Password</label>
                <input
                        name="password_field"
                        type="password"
                        bind:value={password}
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-indigo-500"
                        required
                />
            </div>

            <button
                    type="submit"
                    disabled={loading}
                    class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg disabled:opacity-50"
            >
                {loading ? 'Logging in...' : 'Login'}
            </button>
        </form>
    </div>
</div>