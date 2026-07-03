export interface Education {
  school: string;
  degree: string;
  range: string;
  diploma: string; // path under public/
  majors?: string[];
  minors?: string[];
}

export const education: Education[] = [
  {
    school: 'The Hague University of Applied Sciences',
    degree: 'Bachelor of Science in Information Technology',
    range: '2012 — 2017',
    diploma: 'docs/HBO-Bachelor-Informatica-EN.pdf',
    majors: [
      'Data architecture',
      'Software architecture',
      'Analysis and software design',
      'Application building and management',
      'Process management',
      'Requirements engineering',
    ],
    minors: [
      'Software security',
      'Business information management',
      'Intercultural communications',
      'Business cases',
      'Graph databases',
    ],
  },
  {
    school: 'ROC ID College',
    degree: 'MBO 4 Application Development',
    range: '2010 — 2012',
    diploma: 'docs/Mbo-Applicatieontwikkelaar-EN.pdf',
    majors: ['Implement, maintain, design and realize applications'],
  },
];
