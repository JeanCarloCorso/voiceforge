const gerarBtn = document.getElementById("gerar");
const statusDiv = document.getElementById("status");
const player = document.getElementById("player");
const speakerSelect = document.getElementById("speaker");

let pollingInterval = null;

/* 🔹 Carregar speakers da API */
async function loadSpeakers() {
    const res = await fetch("/tts/speakers");
    const speakers = await res.json();

    speakerSelect.innerHTML = "";

    speakers.forEach(speaker => {
        const option = document.createElement("option");
        option.value = speaker;
        option.textContent = speaker;
        speakerSelect.appendChild(option);
    });
}

/* 🔹 Gerar áudio */
gerarBtn.onclick = async () => {
    gerarBtn.disabled = true;
    player.style.display = "none";
    statusDiv.innerText = "⏳ Enviando texto...";

    const texto = document.getElementById("texto").value;
    const speaker = speakerSelect.value;

    const res = await fetch("/tts/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto, speaker })
    });

    const data = await res.json();
    const taskId = data.task_id;

    statusDiv.innerText = "🎧 Gerando áudio...";
    pollingInterval = setInterval(() => checkStatus(taskId), 2000);
};

/* 🔹 Polling */
async function checkStatus(taskId) {
    const res = await fetch(`/tts/status/${taskId}`);
    const data = await res.json();

    if (data.status === "done") {
        clearInterval(pollingInterval);
        gerarBtn.disabled = false;
        statusDiv.innerText = "✅ Áudio pronto!";

        player.src = `/audios/${data.audio}`;
        player.style.display = "block";
        player.play();
    }

    if (data.status === "error") {
        clearInterval(pollingInterval);
        gerarBtn.disabled = false;
        statusDiv.innerText = "❌ Erro ao gerar áudio";
    }
}

/* 🔹 Init */
loadSpeakers();
