import { apiPost } from "./api.js";

upload.onclick = async () => {
    const form = new FormData();
    form.append("file", file.files[0]);

    const res = await apiPost("/speakers/upload", form, true);
    msg.innerText = res.message;
};
