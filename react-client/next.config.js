const path = require('path');

/** @type {import('next').NextConfig} */
const nextConfig = {
  // Add the Sass options
  sassOptions: {
    includePaths: [path.join(__dirname, 'styles')],
  },
};

module.exports = nextConfig
