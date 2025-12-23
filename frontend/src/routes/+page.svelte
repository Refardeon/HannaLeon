<script>
    import logo1 from "$lib/assets/HL1.svg"
    import logo2 from "$lib/assets/HL2.svg"
    import logo3 from "$lib/assets/HL3.svg"
    import {authStore} from '$lib/stores/auth.svelte.js';
    import {authApi} from "$lib/api/auth";


    let logos = [logo1, logo2, logo3];
    let selectedLogo = $state(0);

    async function selectLogo(){
        let user = await authApi.getMe()
        user = await authApi.setLogo(user.id, {logo:selectedLogo})
        authStore.setUser(user)
    }
</script>

<div class="min-h-screen flex items-center flex-col p-4">
    <div class="max-w-4xl mx-auto text-center">

        <div class="mb-12">
            <h1 class="text-6xl font-bold mb-4 bg-gradient-to-r from-amber-600 to-orange-600 bg-clip-text text-transparent">
                Hanna & Leon
            </h1>
        </div>
    </div>
    <div class="text-amber-900 text-left">
        {#if !authStore.user?.logo}
            Liebe Hanna,
            bevor alles losgeht, wähle bitte ein Logo aus:<br/>
            {#each [1, 2, 3] as number}
                <label>
                    <input
                            type="radio"
                            name="logo"
                            value={number}
                            bind:group={selectedLogo}
                    />

                    <img src={logos[number-1]} alt="Logo {number}" class="inline-block w-16 h-16 mx-2"/>
                </label><br/>
            {/each}
                <button
                    onclick={selectLogo}
                    class="bg-green-600 hover:bg-green-700 text-white p-2 rounded-lg transition-colors shadow-sm"
                    aria-label="Ok"
                >
                    Ok
                </button>
        {:else}
            Liebe Hanna,<br/>
            <br/>
            was habe ich mir denn da jetzt ausgedacht? Naja, da waren beim lieben Leon die Ambitionen vielleicht ein
            kleines bisschen größer als die zur Verfügung stehende Zeit. <br/>
            Das soll uns aber nicht weiter stören, denn wir wissen: in der Softwarewelt funktioniert das einfach
            alles per OTA-Update und genau wird das auch hier sein! Wir haben hier quasi ein MVP.<br/>
            <br/>
            Aber ich hole dich mal als zukünftige Softwareprojektleiterin, Product Ownerin und eine von 2
            Architekturverantwortlichen dieses Projekts ab, was hier schon passiert ist und was noch fehlt.<br/>
            Die Vision unseres Kunden (das sind künftig wir beide) ist ein Tool, das uns hilft,
            gemeinsame Dinge zu planen, zu organisieren und zu dokumentieren. Möglicherweise wird sich das Anforderungsprofil
            allerdings noch ändern, man weiß ja wie Kunden sind. <br/>
            Das MVP umfasst bisher lediglich eine interaktive Liste mit allen geplanten Aktivitäten. Für ein konkretes Logo
            konnte ich mich nicht entscheiden, aber da hast du ja schon die Zügel in die Hand genommen. Gut!<br/>
            <br/>
            Das Ganze ist in einem GitHub-Repo aufgesetzt, da könnten wir auch die Planungen vornehmen und die Issues tracken.
            Die Anwendung besteht aus Back- und Frontend mit entsprechender <a class="text-blue-500" href="https://api.hanna-und-leon.de">API</a> für das
            Backend und der Frontendseite, die du gerade vor dir siehst. Back- und Frontend laufen jeweils in eigenen
            Docker-Containern mit entsprechender Build-Pipeline, ich habe bereits einen Server für die Container aufgesetzt,
            wie du siehst. Der Backend-Stack besteht aus dem FastAPI-Framework in Python mit sqlite-Datenbank auf einem
            uvicorn-Server. Das Frontend ist eine Anwendung im Sveltekit-Framework, läuft derzeit auf node.js und ist in
            Typescript geschrieben. Da ich mit nicht einmal der Hälfte der genannten Technologien vertraut war, habe ich
            die letzten Tage genutzt und mich ein bisschen fit gemacht - wie du siehst mit wackeligem ersten Erfolg.<br/>
            <br/>
            Schau dir doch an dieser Stelle gern schonmal das Listen-Feature an, damit du einschätzen kannst, wo wir
            derzeit stehen.
            <br/>
            Was ist nun noch geplant? Der Kunde wünscht sich einiges und du weißt, eigentlich brauchen wir noch eine
            anständige Architektur und Softwaretests, sonst ist das ganze hier ganz schnell eine Totgeburt! Coding only
            hat noch nie irgendwo vernünftig funktioniert, aber wem sage ich das.<br/>
            Was steht nun also auf der Liste unseres Kunden?
            <ul class="list-disc list-inside">
                <li>Logo festlegen (✓)</li>
                <li>Design überarbeiten</li>
                <li>Weitere Listen anlegen</li>
                <li>Listen mit Daten ausstatten (wann erstellt, wann gemacht)</li>
                <li>Listenitems wiederholbar machen</li>
                <li>Kalender erstellen</li>
                <li>Sync für den Kalender mit den üblichen Formaten</li>
                <li>Listenitems in Kalender einplanen</li>
                <li>Einbinden von Dokumenten und Fotos als Archiv</li>
                <li>Zeitstrahl der Freundschaft erstellen, den alle (beide) User bearbeiten können</li>
            </ul>
            Du siehst, wir haben viel zu tun. Lass uns das Backlog priorisieren und loslegen, wir haben ja nicht unser
            ganzes Leben Zeit dafür!
            <br/><br/>
            Hab dich lieb,<br/>
            Dein Leon
            <br/><br/>
            P.S.: Na toll, ich schenke dir Arbeit zu Weihnachten, good job! Hast ja sonst nix zu tun 😅
        {/if}
    </div>
</div>