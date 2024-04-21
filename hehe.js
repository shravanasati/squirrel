console.log("am am am no sex noooo cyka blyat");

let sendButton = document.getElementById();

sendButton.eventListener("click", () => {
  question = document.getElementById("question").value;
  document.getElementById("question").value = "";

  question.InnerHTML = questionInput;

  postData("/api", { question: questionInput });
});
function submitForm(event) {
  // Prevent default form submission behavior
  event.preventDefault();

  // Collect form data
  const formData = {
    username: document.getElementById("username").value,
    password: document.getElementById("password").value,
    host: document.getElementById("host").value,
    port: document.getElementById("port").value,
    dbname: document.getElementById("dbname").value,
    query: document.getElementById("query").value,
  };

  // Send form data to the backend using fetch API
  fetch("/process-form", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Handle response from the backend
      console.log("Success:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
runQuery.eventListener("click", () => {});
