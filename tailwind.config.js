/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./index.html",
        "./**/*.{html,js}"
    ],
    theme: {
        extend: {
            colors: {
                'neon-blue': '#00D4FF',
                'neon-violet': '#9D00FF',
            },
            animation: {
                'pulse-single': 'pulse-single 3s infinite',
            },
            keyframes: {
                'pulse-single': {
                    '0%': { transform: 'scale(1)', opacity: '0.6' },
                    '50%': { transform: 'scale(1.5)', opacity: '0' },
                    '100%': { transform: 'scale(1)', opacity: '0' },
                }
            }
        },
    },
    plugins: [],
}
