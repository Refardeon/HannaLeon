interface User {
    username: string;
    logo: number;
}

class AuthStore {
    user = $state<User | null>(null);
    isAuthenticated = $derived(this.user !== null);

    setUser(user: User | null) {
        this.user = user;
    }

    logout() {
        this.user = null;
    }
}

export const authStore = new AuthStore();