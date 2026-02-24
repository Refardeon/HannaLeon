<script>
    import logo1 from "$lib/assets/HL1.svg"
    import logo2 from "$lib/assets/HL2.svg"
    import logo3 from "$lib/assets/HL3.svg"
    import {authStore} from '$lib/stores/auth.svelte.js';
    import {authApi} from "$lib/api/auth";


    let logos = [logo1, logo2, logo3];
    let selectedLogo = $state(0);

    async function selectLogo() {
        let user = await authApi.getMe()
        user = await authApi.setLogo(user.id, {logo: selectedLogo})
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
            <p class="text-2xl">24.02.2026</p>
            Liebe Hanna,<br/>
            wann hat eigentlich unsere Freundschaft angefangen? Das ist nicht ganz einfach zu beantworten, aber du hast
            schon was vorgegeben. Mit dem Puzzelrahmen, den du mir zu Weihnachten geschenkt hast, hast du den heutigen
            Tag
            als Jahrestag gesetzt! Damit möchte ich ein paar Meilensteine unserer Freundschaft hier abbilden:<br/><br/>
            <table>
                <thead class="text-xl">
                <tr>
                    <td>Datum</td>
                    <td>Ereignis</td>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td class="px-2">07.03.2024</td>
                    <td>Buddy-Wahl BR-Klausur, erstes echtes Treffen</td>
                </tr>
                <tr>
                    <td class="px-2">28.03.2024</td>
                    <td>Erstes BR-Onboarding</td>
                </tr>
                <tr>
                    <td class="px-2">15.-17.4.2024</td>
                    <td>Betriebsräteversammlung in Stuttgart</td>
                </tr>
                <tr>
                    <td class="px-2">11-14.02.2025</td>
                    <td>Kommunikationsschulung Magdeburg, Teil 1 mit anschließender Demo und Gespräch im Auto, als Hanna Leon nach Hause bringt</td>
                </tr>
                <tr>
                    <td class="px-2">ab 18.02.2025</td>
                    <td>Nahezu täglicher Kontakt über Signal</td>
                </tr>
                <tr>
                    <td class="px-2">24.02.2025</td>
                    <td>Essen bei Yumini</td>
                </tr>
                <tr>
                    <td class="px-2">31.03.-04.04.2025</td>
                    <td>Betriebsräteversammlung Wolfsburg</td>
                </tr>
                <tr>
                    <td class="px-2">08.04.2025</td>
                    <td>Anmeldung zum Tanzen abgegeben</td>
                </tr>
                <tr>
                    <td class="px-2">13.04.2025</td>
                    <td>Spaziergang um den See, Essen im Lakeside, richtig langes Gespräch, ab hier spätestens gut befreundet</td>
                </tr>
                <tr>
                    <td class="px-2">27.04.-30.04.2025</td>
                    <td>Kommunikationsschulung Magdeburg, Teil 2</td>
                </tr>
                <tr>
                    <td class="px-2">04.05.2025</td>
                    <td>Erstes Mal Tanzen und spazieren gehen und quatschen</td>
                </tr>
                <tr>
                    <td class="px-2">09.06.2025</td>
                    <td>Hanna lernt Ska kennen</td>
                </tr>
                <tr>
                    <td class="px-2">14.-15.06.2025</td>
                    <td>Kurztrip zum Meer</td>
                </tr>
                <tr>
                    <td class="px-2">19.06.2025</td>
                    <td>Hanna lernt (teilweise) Leons Familie im Garten kennen</td>
                </tr>

                <tr>
                    <td class="px-2">22.06.2025</td>
                    <td>Erstes Mal Kletterwald in Haltern, holt Hanna aus einem fiesen Loch</td>
                </tr>
                <tr>
                    <td class="px-2">17.07.2025</td>
                    <td>Hanna löst die Rätselbox und findet einen Brief vom besten Freund</td>
                </tr>
                <tr>
                    <td class="px-2">06.09.2025</td>
                    <td>Zusammen beim Heimatfest</td>
                </tr>
                <tr>
                    <td class="px-2">11.09.2025</td>
                    <td>Essen bei Imlee vorm Urlaub in Afrika</td>
                </tr>
                <tr>
                    <td class="px-2">16.09.2025</td>
                    <td>Die ersten Hörgeschichten für Hanna</td>
                </tr>
                <tr>
                    <td class="px-2">09.10.2025</td>
                    <td>Hanna wird Leons Modeberaterin und geht mit ihm Shoppen</td>
                </tr>
                <tr>
                    <td class="px-2">12.10.2025</td>
                    <td>2. und letztes Klettern der Saison</td>
                </tr>

                <tr>
                    <td class="px-2">08.-09.11.2025</td>
                    <td>König der Löwen und geile Zeit in Hamburg</td>
                </tr>
                <tr>
                    <td class="px-2">10.11.2025</td>
                    <td>Bestes Geburtstagsgeschenk dieses Jahr kommt von Hanna</td>
                </tr>
                <tr>
                    <td class="px-2">20.11.2025</td>
                    <td>Pralinen!</td>
                </tr>
                <tr>
                    <td class="px-2">21.11.2025</td>
                    <td>Leon lernt Hannas Familie (teilweise) kennen</td>
                </tr>
                <tr>
                    <td class="px-2">11.12.2025</td>
                    <td>Weihnachtsmarkt-Krimi in Essen</td>
                </tr>
                <tr>
                    <td class="px-2">14.12.2025</td>
                    <td>Kekse backen und quatschen auf Hannas Sofa</td>
                </tr>

                <tr>
                    <td class="px-2">24.12.2025</td>
                    <td>Weihnachtsgeschenke werden ausgetauscht!</td>
                </tr>
                <tr>
                    <td class="px-2">29.12.2025</td>
                    <td>Jahresrückblick ❤️</td>
                </tr>
                <tr>
                    <td class="px-2">20.01.2026</td>
                    <td>Chor</td>
                </tr>
                <tr>
                    <td class="px-2">25.01.-06.02.2026</td>
                    <td>Schulungen in Inzell, Sauna, Sport und Spiele</td>
                </tr>

                </tbody>

            </table>
            <br/>
            Wir beiden haben echt schon unheimlich viel zusammen erlebt. Beim Durchscrollen durch unsere Chats, konnte ich
            mich immer wieder genau an die Situationen erinnern, in denen ich dir die Dinge geschrieben habe. Es sind so
            unheimlich viele tolle Nachrichten dabei. <br/>
            Ich habe dich so tief in mein Herz geschlossen, ich habe dich so
            unheimlich lieb, Hanna! Ich freue mich schon auf die nächsten Jahre mit dir.

            <br/><br/>
            <p class="text-2xl">23.12.2025</p>
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
            gemeinsame Dinge zu planen, zu organisieren und zu dokumentieren. Möglicherweise wird sich das
            Anforderungsprofil
            allerdings noch ändern, man weiß ja wie Kunden sind. <br/>
            Das MVP umfasst bisher lediglich eine interaktive Liste mit allen geplanten Aktivitäten. Für ein konkretes
            Logo
            konnte ich mich nicht entscheiden, aber da hast du ja schon die Zügel in die Hand genommen. Gut!<br/>
            <br/>
            Das Ganze ist in einem GitHub-Repo aufgesetzt, da könnten wir auch die Planungen vornehmen und die Issues
            tracken.
            Die Anwendung besteht aus Back- und Frontend mit entsprechender <a class="text-blue-500"
                                                                               href="https://api.hanna-und-leon.de">API</a>
            für das
            Backend und der Frontendseite, die du gerade vor dir siehst. Back- und Frontend laufen jeweils in eigenen
            Docker-Containern mit entsprechender Build-Pipeline, ich habe bereits einen Server für die Container
            aufgesetzt,
            wie du siehst. Der Backend-Stack besteht aus dem FastAPI-Framework in Python mit sqlite-Datenbank auf einem
            uvicorn-Server. Das Frontend ist eine Anwendung im Sveltekit-Framework, läuft derzeit auf node.js und ist in
            Typescript geschrieben. Da ich mit nicht einmal der Hälfte der genannten Technologien vertraut war, habe ich
            die letzten Tage genutzt und mich ein bisschen fit gemacht - wie du siehst mit wackeligem ersten
            Erfolg.<br/>
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