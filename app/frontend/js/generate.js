import { apiGet, apiPost } from "./api.js";

const bar = document.getElementById("bar");
const player = document.getElementById("player");
const gerarBtn = document.getElementById("gerar");
const speakerSelect = document.getElementById("speaker");
const texto = document.getElementById("texto");
const progressContainer = document.getElementById("progress-container");
const statusMsg = document.getElementById("status-msg");

async function loadSpeakers() {
    const speakers = await apiGet("/tts/speakers");
    speakerSelect.innerHTML = "";
    speakers.forEach(s => speakerSelect.add(new Option(s, s)));
}

gerarBtn.onclick = async () => {
    // Reset Inicial
    gerarBtn.disabled = true;
    gerarBtn.innerHTML = `<span class="spinner"></span> Gerando...`;
    player.style.display = "none";
    statusMsg.style.display = "block";
    progressContainer.style.display = "block";
    progressContainer.classList.add("active");
    bar.style.width = "5%";

    try {
        const res = await apiPost("/tts/generate", {
            texto: texto.value,
            speaker: speakerSelect.value
        });

        const taskId = res.task_id;

        const interval = setInterval(async () => {
            const data = await apiGet(`/tts/status/${taskId}`);

            // MAPEAMENTO DE STATUS
            switch (data.status) {
                case "queued":
                    statusMsg.innerText = "Aguardando na fila...";
                    statusMsg.style.color = "#94A3B8"; // Cinza
                    bar.style.width = "15%";
                    break;

                case "processing":
                    statusMsg.innerText = "Transformando texto em voz...";
                    statusMsg.style.color = "#38BDF8"; // Azul
                    bar.style.width = "60%";
                    break;

                case "done":
                    clearInterval(interval);
                    statusMsg.innerText = "Áudio gerado com sucesso!";
                    statusMsg.style.color = "#10B981"; // Verde
                    bar.style.width = "100%";
                    progressContainer.classList.remove("active");

                    setTimeout(() => {
                        finalizarGeracao(data.audio);
                    }, 500);
                    break;

                case "error":
                    clearInterval(interval);
                    statusMsg.innerText = "Erro: " + (data.error || "Falha no processamento.");
                    statusMsg.style.color = "#EF4444"; // Vermelho
                    resetBotao();
                    break;
            }
        }, 1500);

    } catch (e) {
        statusMsg.innerText = "Erro de conexão com o servidor.";
        resetBotao();
    }
};

function finalizarGeracao(audioName) {
    gerarBtn.disabled = false;
    gerarBtn.innerHTML = "Gerar novo áudio";
    player.src = `/audios/${audioName}`;
    player.style.display = "block";
    player.play();
}

function resetBotao() {
    gerarBtn.disabled = false;
    gerarBtn.innerHTML = "Tentar novamente";
    progressContainer.classList.remove("active");
}

loadSpeakers();