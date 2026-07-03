import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://misja-pronk.github.io',
  base: '/resume',
  trailingSlash: 'ignore',
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'nl'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
});
