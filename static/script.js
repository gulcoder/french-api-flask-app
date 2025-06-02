document.getElementById('new-quote-btn').addEventListener('click', async () => {
    try {
        const response = await fetch('/new-quote');

        // Kolla först att svaret var OK (status 200)
        if (!response.ok) {
            throw new Error(`Serverfel: ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            alert(data.error);
            return;
        }

        // Uppdatera citatet på sidan
        document.getElementById('quote-text').textContent = `"${data.text}"`;
        document.getElementById('quote-author').textContent = `- ${data.author}`;
    } catch (error) {
        console.error("Fel vid hämtning av citat:", error);
        alert("Kunde inte hämta nytt citat just nu. Försök igen om en stund.");
    }
});
