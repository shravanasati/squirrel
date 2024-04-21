function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

async function copyToClipboard() {
	let resultURL = document.getElementById("result-url").innerText
	await navigator.clipboard.writeText(resultURL)
	let copybtn = document.getElementById("copyBtn")
	copybtn.innerText = "Copied!"
	await sleep(3000)
	copybtn.innerText = "Copy"
}
