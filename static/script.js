const p = document.getElementById("response");
const scan_btn = document.querySelector(".scan-btn");  //start scanning button
const scanner_line = document.querySelector(".scanner-line");  //animating scanner line moving up to down when start scanning button is clicked

async function get_backend() {
    console.log("Instruction received....... contacting backend....")
    const res = await fetch('/test', {
        method: "GET",
    })

    const data = await res.json()
    console.log(data);
    console.log(data.message);
    p.innerText = data.message
}

function updateTime() {
    document.getElementById("clock").innerText = "Time : " + new Date().toLocaleTimeString();
}

function updateDate() {
    document.getElementById("date").innerText = "Date : " + new Date().toLocaleDateString();
}

async function callBackend(url_to_call, options) {
    try {
        const response = await fetch(url_to_call, options);
        data = await response.json();
        return data;
    } catch (error) {
        console.log(error)
        alert(error);
        return null;
    }
}


scan_btn.addEventListener("click", async () => {
    scanner_line.classList.add("is-scanning");
    scanner_line.style.opacity = "1";
    btn_text = scan_btn.querySelector(".btn-content");
    btn_text.innerText = "Scanning.........";
    scan_btn.disabled = true;
    instruction_text = document.querySelector(".instruction-text");
    // instruction_text.innerText = "Scanning.........";

    fetch_options = {
        method: "GET"
    }
    output = await callBackend("/test", fetch_options);
    if (output) {
        scanner_line.classList.remove("is-scanning");
        scanner_line.style.opacity = "0";
        btn_text.innerText = "Start Scanning";
        scan_btn.disabled = false;
        user_info = document.querySelector(".fingerprint-details");
        user_info.style.opacity = "1";
        // alert(output.message);
    }

})

setInterval(updateTime, 1000);
setInterval(updateDate, 1000);
updateTime();
updateDate();

