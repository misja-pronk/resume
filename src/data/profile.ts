import type { Locale } from '../i18n';

const shared = {
  firstName: 'Misja',
  lastName: 'Pronk',
  company: 'ProRex Consultancy',
  email: 'misja@prorexconsultancy.nl',
  linkedin: 'https://www.linkedin.com/in/misja-pronk',
  github: 'https://github.com/misja-pronk',
  photo: 'img/profile-picture.webp',
};

const text = {
  en: {
    title: 'Data & Platform Engineering Consultant',
    location: 'Friesland, The Netherlands',
    resumePdf: 'docs/mp_resume.pdf',
    tagline:
      'I design and build data platforms — Databricks-deep, open-source-first, automated end to end, and built to last.',
    bio: [
      'I am the owner of ProRex Consultancy and work as a freelance Data & Platform Engineering consultant. I am analytically strong, creative and have an eye for quality and results. I enjoy complex functional and technical challenges, work well under pressure and adapt quickly to new requirements.',
      'With more than a decade in IT — and over 8 years designing and building data solutions — I have grown from data engineer into a well-rounded platform professional: deep expertise on the Databricks platform, metadata-driven data solutions, and the full platform-engineering stack — Terraform, Terragrunt, GitHub, CI/CD and DevOps ways of working. I love open source and prefer open standards over vendor lock-in, both in what I build and in what I share.',
    ],
    interests:
      'Originally I wanted to become a chef — the kitchen is still where I unwind, from low & slow BBQ to fine dining. I am married, and the biggest project yet is underway: my wife and I are expecting — I am becoming a father. At home you will find Rex (my Scottish Collie), a heavily automated house, an ever-evolving desk setup with self-built PCs and mechanical keyboards, woodworking and furniture-design projects, guitars, a KTM 1190 — and the long-term dream of designing and building my own house.',
  },
  nl: {
    title: 'Data & Platform Engineering Consultant',
    location: 'Friesland, Nederland',
    resumePdf: 'docs/mp_resume_nl.pdf',
    tagline:
      'Ik ontwerp en bouw dataplatformen — Databricks-diep, open source eerst, end-to-end geautomatiseerd en gebouwd om lang mee te gaan.',
    bio: [
      'Ik ben eigenaar van ProRex Consultancy en werk als freelance Data & Platform Engineering consultant. Ik ben analytisch sterk, creatief en heb oog voor kwaliteit en resultaat. Ik geniet van complexe functionele en technische uitdagingen, werk goed onder druk en pas me snel aan nieuwe eisen aan.',
      'Met ruim tien jaar in de IT — waarvan meer dan 8 jaar in het ontwerpen en bouwen van dataoplossingen — ben ik gegroeid van data engineer naar een allround platformprofessional: diepgaande expertise op het Databricks-platform, metadata-gedreven dataoplossingen en de volledige platform-engineering-stack — Terraform, Terragrunt, GitHub, CI/CD en DevOps-werkwijzen. Ik hou van open source en verkies open standaarden boven vendor lock-in, in wat ik bouw én in wat ik deel.',
    ],
    interests:
      'Oorspronkelijk wilde ik chef-kok worden — de keuken is nog steeds waar ik ontspan, van low & slow BBQ tot fine dining. Ik ben getrouwd, en het grootste project tot nu toe is onderweg: mijn vrouw en ik verwachten een kindje — ik word vader. Thuis vind je Rex (mijn Schotse Collie), een zwaar geautomatiseerd huis, een altijd evoluerende desk setup met zelfgebouwde pc’s en mechanische toetsenborden, houtbewerkings- en meubelontwerpprojecten, gitaren, een KTM 1190 — en de langetermijndroom om ooit mijn eigen huis te ontwerpen en te bouwen.',
  },
} as const;

const statsData = {
  en: [
    { value: '11+', label: 'years in IT, 8+ in data & platforms' },
    { value: '21', label: 'projects delivered' },
    { value: '4', label: 'certifications' },
    { value: '25+', label: 'Azure services in production' },
  ],
  nl: [
    { value: '11+', label: 'jaar in IT, 8+ in data & platforms' },
    { value: '21', label: 'projecten opgeleverd' },
    { value: '4', label: 'certificeringen' },
    { value: '25+', label: 'Azure-services in productie' },
  ],
} as const;

export function getProfile(locale: Locale) {
  return { ...shared, ...text[locale] };
}

export function getStats(locale: Locale) {
  return statsData[locale];
}

/** @deprecated kept for compatibility; prefer getProfile(locale) */
export const profile = { ...shared, ...text.en };
export const stats = statsData.en;
