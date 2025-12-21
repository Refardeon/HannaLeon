<script lang="ts">
    import favicon from '$lib/assets/HL2_favicon.svg';
    import logo from '$lib/assets/HL2.svg';

    let {children} = $props();
</script>

<svelte:head>
    <link rel="icon" href={favicon} style="background-color: white"/>
</svelte:head>


<header class="p-3 bg-amber-50">
    <a href="/">
        <img src={logo} class="w-12 h-12 inline mx-5" alt="HL"/>
    </a>
    <h1 class="inline">Hanna und Leon</h1>
</header>

<div class="flex flex-row">

    <nav class="flex-none bg-amber-50 w-1/6 h-screen *:width-full *:block *:p-5 *:hover:bg-amber-100">
        <a href="/liste">Liste</a>
    </nav>

    <div class="flex-auto">
        {@render children()}
    </div>

</div>
