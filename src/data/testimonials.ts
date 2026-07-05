import type { Locale } from '../i18n';

export interface Testimonial {
  quote: string;
  author: string;
  role: string;
  source: string;
  sourceUrl?: string;
}

const data: Record<Locale, Testimonial[]> = {
  en: [
    {
      quote:
        'Misja communicates clearly and directs teams effectively. He excels technically and solves problems quickly. Our year-long collaboration building a cloud platform was excellent.',
      author: 'Jaco van Gelder',
      role: 'Colleague — cloud platform engagement',
      source: 'LinkedIn recommendation',
      sourceUrl: 'https://www.linkedin.com/in/misja-pronk/',
    },
  ],
  nl: [
    {
      quote:
        'Misja communiceert helder en stuurt teams effectief aan. Technisch blinkt hij uit en hij lost problemen snel op. Onze jarenlange samenwerking aan een cloudplatform was uitstekend.',
      author: 'Jaco van Gelder',
      role: 'Collega — cloudplatform-traject',
      source: 'LinkedIn-aanbeveling',
      sourceUrl: 'https://www.linkedin.com/in/misja-pronk/',
    },
  ],
};

export function getTestimonials(locale: Locale): Testimonial[] {
  return data[locale];
}
