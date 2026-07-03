import type { Locale } from '../i18n';

export type BookStatus = 'read' | 'reading' | 'wishlist';

export interface Book {
  title: string;
  author: string;
  discipline: string;
  status: BookStatus;
  cover?: string; // path under public/, e.g. img/books/lotr.jpg
  note?: string;
}

/**
 * The library — books read, in hand, or on order.
 * status: 'read' · 'reading' · 'wishlist'
 * discipline is a { en, nl } pair; everything else is shared.
 */
const books: (Omit<Book, 'discipline'> & { discipline: Record<Locale, string> })[] = [
  {
    title: 'The Lord of the Rings',
    cover: 'img/books/lotr.jpg',
    author: 'J.R.R. Tolkien',
    discipline: { en: 'Fiction', nl: 'Fictie' },
    status: 'read',
  },
  {
    title: 'The Alchemist',
    cover: 'img/books/alchemist.jpg',
    author: 'Paulo Coelho',
    discipline: { en: 'Fiction', nl: 'Fictie' },
    status: 'read',
  },
  {
    title: 'Innocent Code',
    cover: 'img/books/innocent-code.jpg',
    author: 'Sverre H. Huseby',
    discipline: { en: 'Software Security', nl: 'Softwarebeveiliging' },
    status: 'read',
  },
  {
    title: 'Dressing the Man',
    cover: 'img/books/dressing-the-man.jpg',
    author: 'Alan Flusser',
    discipline: { en: 'Style', nl: 'Stijl' },
    status: 'read',
  },
];

export function getLibrary(locale: Locale): Book[] {
  return books.map((b) => ({ ...b, discipline: b.discipline[locale] }));
}
