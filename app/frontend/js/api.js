export async function apiGet(url) {
    const res = await fetch(url);
    if (!res.ok) throw new Error("Erro API");
    return res.json();
}

export async function apiPost(url, data, isForm = false) {
    const res = await fetch(url, {
        method: "POST",
        body: isForm ? data : JSON.stringify(data),
        headers: isForm ? {} : { "Content-Type": "application/json" }
    });

    if (!res.ok) throw new Error("Erro API");
    return res.json();
}
