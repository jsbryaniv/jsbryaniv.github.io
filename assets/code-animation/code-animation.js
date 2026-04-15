
document.addEventListener("DOMContentLoaded", () => {
  const demos = document.querySelectorAll(".code-animation");

  demos.forEach((demo) => {
    const code = demo.querySelector("pre code");
    const output = demo.querySelector(".cell-output");

    if (!code) return;

    const originalText = code.innerText;
    const lines = originalText.split("\n");

    function runAnimation() {
      // Reset
      code.innerText = "";
      demo.classList.add("show-code");
      demo.classList.remove("show-output");

      let i = 0;

      function typeLine() {
        if (i < lines.length) {
          code.innerText += (i === 0 ? "" : "\n") + lines[i];
          i++;
          setTimeout(typeLine, 300);
        } else {
          demo.classList.add("show-output");

          // Loop
          setTimeout(runAnimation, 1500);
        }
      }

      typeLine();
    }

    runAnimation();
  });
});
