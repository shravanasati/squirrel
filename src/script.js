console.log("am am am no sex noooo cyka blyat");

sendButton.eventListener("click", ()=>{
    question = document.getElementById("question").value;
    document.getElementById("question").value = "";
    
    question.InnerHTML = questionInput;

    postData("/api",{"question":questionInput});

})