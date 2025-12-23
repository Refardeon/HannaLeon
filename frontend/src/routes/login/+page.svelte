<script lang="ts">
    import {authApi} from '$lib/api/auth';
    import {authStore} from '$lib/stores/auth.svelte';
    import {goto} from '$app/navigation';
    import {LogIn, User, Lock} from 'lucide-svelte';

    let username = $state('');
    let password = $state('');
    let error = $state('');
    let loading = $state(false);

    async function handleLogin() {
        loading = true;
        error = '';

        try {
            const response = await authApi.login({username, password});
            authStore.setUser(response.user)
            goto('/');
        } catch (err) {
            console.error('Login failed:', err);
            error = 'Login fehlgeschlagen. Bitte überprüfe deine Daten.';
        } finally {
            loading = false;
        }
    }
</script>

<div class="min-h-screen flex items-center justify-center p-4">
    <div class="max-w-md w-full">
        <!-- Card -->
        <div class="bg-white rounded-3xl shadow-2xl p-8 border border-amber-100">
            <!-- Logo/Titel -->
            <div class="text-center mb-8">
                <div class="inline-block p-4 bg-gradient-to-br from-amber-100 to-orange-100 rounded-2xl mb-4">
                    <LogIn class="w-12 h-12 text-amber-600"/>
                </div>
                <h1 class="text-3xl font-bold text-gray-800 mb-2">Willkommen!</h1>
                <p class="text-gray-600">Melde dich an, um fortzufahren</p>
            </div>

            {#if error}
                <div class="bg-red-50 border-l-4 border-red-500 text-red-700 px-4 py-3 rounded-lg mb-6">
                    <p class="text-sm">{error}</p>
                </div>
            {/if}

            <form onsubmit={(e) => { e.preventDefault(); handleLogin(); }} class="space-y-5">
                <!-- Username -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2" for="user_input">Benutzername</label>
                    <div class="relative">
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <User class="w-5 h-5 text-gray-400"/>
                        </div>
                        <input
                                name="user_input"
                                type="text"
                                bind:value={username}
                                class="w-full pl-10 pr-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:border-amber-500 transition-colors"
                                placeholder="Dein Benutzername"
                                required
                        />
                    </div>
                </div>

                <!-- Password -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2" for="pw_input">Passwort</label>
                    <div class="relative">
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <Lock class="w-5 h-5 text-gray-400"/>
                        </div>
                        <input
                                name="pw_input"
                                type="password"
                                bind:value={password}
                                class="w-full pl-10 pr-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:border-amber-500 transition-colors"
                                placeholder="••••••••"
                                required
                        />
                    </div>
                </div>

                <!-- Submit Button -->
                <button
                        type="submit"
                        disabled={loading}
                        class="w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white font-semibold py-3 rounded-xl transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg hover:shadow-xl"
                >
                    {loading ? 'Anmeldung läuft...' : 'Anmelden'}
                </button>
            </form>
        </div>

        <!-- Footer -->
        <p class="text-center mt-6 text-gray-500 text-sm">
            © 2025 Hanna & Leon
        </p>
    </div>
</div>