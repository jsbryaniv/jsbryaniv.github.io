(function () {
  "use strict";

  function languageFor(codeEl) {
    var match = Array.from(codeEl.classList).find(function (className) {
      return /^language-/.test(className) && className !== "language-sourceCode";
    });

    if (match) return match.replace(/^language-/, "");
    if (codeEl.classList.contains("python")) return "python";
    return null;
  }

  function highlightLine(lineSpan, grammar, language) {
    var anchor = lineSpan.querySelector("a:first-child");
    var source = lineSpan.textContent;
    var highlighted = Prism.highlight(source, grammar, language);

    lineSpan.innerHTML = "";
    if (anchor) lineSpan.appendChild(anchor);
    lineSpan.insertAdjacentHTML("beforeend", highlighted);
  }

  function highlightBlock(codeEl) {
    var language = languageFor(codeEl);
    var grammar = language && Prism.languages[language];

    if (!grammar) return;

    codeEl.classList.add("language-" + language);

    Array.from(codeEl.querySelectorAll("span[id]"))
      .filter(function (span) { return /^cb\d+-\d+$/.test(span.id); })
      .forEach(function (span) {
        highlightLine(span, grammar, language);
      });
  }

  function highlightTutorialCode() {
    if (Prism.languages.python && !Prism.languages.python["function-call"]) {
      Prism.languages.insertBefore("python", "punctuation", {
        "function-call": {
          pattern: /\b[a-zA-Z_]\w*(?=\s*\()/,
          alias: "function"
        }
      });
    }

    document.querySelectorAll("code.sourceCode").forEach(highlightBlock);
    window.tutorialCodeHighlighted = true;
    document.dispatchEvent(new Event("tutorial:code-highlighted"));
  }

  document.addEventListener("DOMContentLoaded", highlightTutorialCode);
}());
