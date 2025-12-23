import type {PageLoad} from "../../.svelte-kit/types/src/routes/liste/$types";
import {authApi} from "$lib/api/auth";

export const ssr = false;

export const load: PageLoad = async () => {
    await authApi.auth_or_login()
};