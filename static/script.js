p = document.getElementById("response");

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
