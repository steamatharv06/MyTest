// CRA scan test file

const TOKEN = "ghp_exampleTokenNotReal000000000000000";

function buildUrl(userInput) {
  // unsafe-ish concatenation for review signal
  return "https://example.com/search?q=" + userInput;
}

function add(a, b) {
  return a + b;
}

module.exports = { buildUrl, add, TOKEN };
