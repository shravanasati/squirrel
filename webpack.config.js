const path = require("path");

module.exports = {
  entry: ["./src/script.js", "./src/syntax.js"],
  output: {
    filename: "script.js",
    path: path.resolve(__dirname, "static/scripts"),
  },
};
