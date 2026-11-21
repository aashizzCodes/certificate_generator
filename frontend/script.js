// variables
let submitButton = document.getElementById("submit_btn");

// functions

// function to send data to the server
async function send_collected_data(data) {
  const response = await fetch("http://127.0.0.1:8000/send", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
}

// handleing Null properity error
document.addEventListener("DOMContentLoaded", () => {
  if (submitButton) {
    // form submit trigger event
    submitButton.addEventListener("click", () => {
      let data = {
        middle_name: document.getElementById("middle-name").value,
        first_name: document.getElementById("first-name").value,
        surname: document.getElementById("surname").value,
        roll_number: document.getElementById("roll-number").value,
        selected_subject: document.getElementById("subject-1").value,
      };

      // send collected data to server using /send --> route
      send_collected_data(data);
    });
  }
});
