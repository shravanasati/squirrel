function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


var modalStatus = false;
function toggleModal(text) {
  modalStatus = !modalStatus;
  const modalText = document.querySelector("#modalText");
  modalText.innerText = text;
  if (!modalStatus) {
    modal.classList.add("hidden");
  } else {
    modal.classList.remove("hidden");
  }
}

async function copyToClipboard(copyBtn, text) {
  await navigator.clipboard.writeText(text);
  copyBtn.innerText = "Copied!";
  await sleep(3000);
  copyBtn.innerText = "Copy";
}

let copyBtn = document.querySelector("#copyQuery");
copyBtn.addEventListener("click", () => {
  copyToClipboard(copyBtn, document.querySelector("#generatedQuery").innerText);
});

let form = document.querySelector("#form");
form.addEventListener("submit", async (ev) => {
  ev.preventDefault();
  ev.stopPropagation();

  for (const elem of form.elements) {
    elem.disabled = true;
  }

  let submitBtn = document.querySelector("#submit");
  submitBtn.innerText = "Please Wait...";

  let formObj = {
    username: document.querySelector("#username").value,
    password: document.querySelector("#password").value,
    host: document.querySelector("#host").value,
    port: parseInt(document.querySelector("#port").value),
    dbname: document.querySelector("#dbname").value,
    question: document.querySelector("#query").value,
  };

  const jsonData = JSON.stringify(formObj);

  try {
    let response = await fetch("/query/build", {
      method: "POST",
      body: jsonData,
      headers: { "Content-Type": "application/json" },
    });
    let jsonResp = await response.json();
    console.log(jsonResp);
    if (jsonResp.ok) {
      document.querySelector("#generatedQuery").innerHTML = jsonResp.message;
    } else {
      console.log("show the goddamn error modal");
      toggleModal(`Unable to build the query: ${jsonResp.message}`);
      setTimeout(() => toggleModal("error"), 5000);
    }
  } catch (e) {
    toggleModal(`Unable to build the query: ${e}`);
    setTimeout(() => toggleModal("error"), 5000);
  } finally {
    for (const elem of form.elements) {
      elem.disabled = false;
    }
    submitBtn.innerText = "Submit";
  }
});
