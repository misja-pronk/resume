import type { Locale } from '../i18n';

export interface Testimonial {
  quote: string;
  author: string;
  role: string;
  context: string;
  source: string;
  sourceUrl?: string;
}

const data: Record<Locale, Testimonial[]> = {
  en: [
    {
      quote:
        'With his strong, direct communication Misja quickly gets everyone moving in the right direction. He also has broad technical knowledge and arrives at the right technical solutions fast. I worked intensively with Misja for a year and built a fantastic cloud platform together with him. I found it an absolute pleasure.',
      author: 'Jaco van Gelder',
      role: 'Co-Founder @ Dtyped · Databricks MVP, Champion & Advisor',
      context: 'Worked with Misja in the same team · November 2021 · translated from Dutch',
      source: 'LinkedIn recommendation',
      sourceUrl: 'https://www.linkedin.com/in/misja-pronk/',
    },
  ],
  nl: [
    {
      quote:
        'Misja weet met zijn sterke en directe communicatie iedereen snel de juiste richting op te krijgen. Hij is daarnaast technisch breed onderlegd en komt snel tot de juiste technische oplossingen. Ik heb een jaar intensief samengewerkt met Misja en een fantastisch cloud platform opgezet samen met hem. Ik heb dat als uiterst plezierig ervaren.',
      author: 'Jaco van Gelder',
      role: 'Co-Founder @ Dtyped · Databricks MVP, Champion & Advisor',
      context: 'Werkte met Misja in hetzelfde team · november 2021',
      source: 'LinkedIn-aanbeveling',
      sourceUrl: 'https://www.linkedin.com/in/misja-pronk/',
    },
  ],
};

export function getTestimonials(locale: Locale): Testimonial[] {
  return data[locale];
}
