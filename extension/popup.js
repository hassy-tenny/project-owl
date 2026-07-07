document
  .getElementById("analyzeBtn")
  .addEventListener("click", async () => {

    const response = await fetch("http://127.0.0.1:8000/analyze");

    const data = await response.json();

    alert(
      `🦉 Decision: ${data.decision}\n\nScore: ${data.score}\n\n${data.reason}`
    );

});