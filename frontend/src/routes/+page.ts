import { redirect } from '@sveltejs/kit';
import { authStore } from '$lib/stores/auth.svelte';

export const load = () => {

    if (!authStore.isAuthenticated) {
    throw redirect(302, '/login');
}
};