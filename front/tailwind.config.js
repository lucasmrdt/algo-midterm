function createValues(from, to, step, keyFormater, valueFormater) {
  return [...new Array(Math.floor((to - from) / step + 1))].reduce(
    (acc, _, i) => ({
      ...acc,
      [keyFormater(from + i * step)]: valueFormater(from + i * step),
    }),
    {}
  );
}

module.exports = {
  purge: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        plum: "var(--plum)",
        pink: "var(--pink)",
        "pastel-pink": "var(--pastel-pink)",
        "pink-light": "var(--pink-light)",
        white: "var(--white)",
        violet: "var(--violet)",
        "light-black": "var(--light-black)",
        black: "var(--black)",
        gray: "var(--gray)",
      },
      spacing: {
        ...createValues(
          0,
          10,
          1,
          (k) => `${k}`,
          (v) => `${v}px`
        ),
        // creating spacing from 0px to 1000px
        ...createValues(
          0,
          1000,
          5,
          (k) => `${k}`,
          (v) => `${v}px`
        ),
        // creating spacing from 0% to 100%
        ...createValues(
          0,
          200,
          5,
          (k) => `${k}%`,
          (v) => `${v}%`
        ),
      },
      maxWidth: {
        // creating max width from 0px to 2000px
        ...createValues(
          0,
          2000,
          25,
          (k) => `${k}`,
          (v) => `${v}px`
        ),
        // creating spacing from 0% to 100%
        ...createValues(
          0,
          100,
          5,
          (k) => `${k}%`,
          (v) => `${v}%`
        ),
        screen: "100vw",
      },
      minWidth: {
        // creating max width from 0px to 2000px
        ...createValues(
          0,
          2000,
          25,
          (k) => `${k}`,
          (v) => `${v}px`
        ),
      },
      minHeight: {
        // creating max width from 0px to 2000px
        ...createValues(
          0,
          2000,
          25,
          (k) => `${k}`,
          (v) => `${v}px`
        ),
      },
      fontSize: {
        ...createValues(
          0,
          55,
          1,
          (k) => `${k}`,
          (v) => `${v}px`
        ),
      },
      fontFamily: {
        medium: "Sharp Grotesk Medium",
        book: "Sharp Grotesk Book",
      },
      screens: {
        sm: "640px",
        md: "800px",
        lg: "1024px",
      },
      boxShadow: {
        DEFAULT: "0px 4px 10px rgba(0, 0, 0, 0.07)",
        hover: "0px 4px 10px rgba(0, 0, 0, 0.3)",
      },
      outline: {
        "pink-light": "2px solid var(--pink-light)",
      },
      keyframes: {
        slideInDown: {
          "0%": { transform: "translateY(-100%)" },
          "100%": { transform: "translateY(0%)" },
        },
        slideOutDown: {
          "0%": { transform: "translateY(0%)" },
          "100%": { transform: "translateY(-100%)" },
        },
      },
      animation: {
        slideInDown: "slideInDown 1s ease-in-out",
        slideOutDown: "slideOutDown 1s ease-in-out",
      },
      translate: {
        "3/2": "150%",
        "2/1": "200%",
        "-3/2": "-150%",
        "-2/1": "-200%",
      },
      zIndex: {
        bg: -1,
      },
      transitionProperty: {
        width: "width",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/forms"), // import tailwind forms
  ],
};
