import { apiGet } from "./api.js";

async function load() {
    const audios = await apiGet("/tts/audios");
    const ul = document.getElementById("lista");
    ul.innerHTML = "";

    audios.forEach(a => {
        const li = document.createElement("li");
        li.className = "audio-item";

        const displayName = a.replace('.wav', '').replace(/_/g, ' ');

        li.innerHTML = `
            <div class="audio-info">
                <span class="audio-name">${displayName}</span>
                <span class="audio-date">Arquivo: ${a}</span>
            </div>
            <div class="audio-player">
                <audio controls src="/audios/${a}"></audio>
            </div>
        `;
        ul.appendChild(li);
    });
}

load();