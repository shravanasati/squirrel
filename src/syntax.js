const { highlight } = require("sql-highlight");

const nhlRes =
  "SELECT `id`, `username` FROM `users` WHERE `email` = 'test@example.com'"; //* save response as a string in this variable
const hlRes = highlight(nhlRes); //* use this string to display on the site

console.log(nhlRes);
console.log(hlRes);
