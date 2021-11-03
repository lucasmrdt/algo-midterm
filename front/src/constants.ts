export const ENDPOINT =
  process.env.NODE_ENV === "production"
    ? "https://algo-midterm.herokuapp.com"
    : "http://localhost:5000";
