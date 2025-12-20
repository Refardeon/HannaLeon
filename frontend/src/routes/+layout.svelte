<script lang="ts">
    import favicon from '$lib/assets/HL2.svg';

    let {children} = $props();
</script>

<svelte:head>
    <link rel="icon" href={favicon}/>
</svelte:head>


<header class="p-3">
    <a href="/">
        <img src={favicon} class="w-12 h-12 inline mx-5" alt="HL"/>
    </a>
    <h1 class="inline">Hanna und Leon</h1>
</header>

<div class="flex flex-row">

    <nav class="flex-none bg-amber-500 w-1/6 h-screen *:width-full *:block *:p-5 *:hover:bg-amber-100">
        <a href="/liste">Liste</a>
        <a href="/liste">Liste</a>
    </nav>

    <div class="flex-auto bg-blue-500">
        {@render children()}
    </div>

</div>
