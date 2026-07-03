import type { Locale } from '../i18n';

export interface Job {
  role: string;
  company: string;
  companyUrl?: string;
  range: string;
  summary: string;
  clients?: { name: string; url?: string }[];
}

const clients = {
  prorex: [
    { name: 'Heijmans', url: 'https://www.heijmans.nl' },
    { name: 'TBI', url: 'https://www.tbi.nl' },
    { name: 'Vattenfall', url: 'https://vattenfall.com' },
  ],
  gdd: [
    { name: 'Nationale-Nederlanden', url: 'https://www.nn.nl' },
    { name: 'Stedin', url: 'https://www.stedin.net' },
    { name: 'Witteveen+Bos', url: 'https://www.witteveenbos.com/nl/' },
    { name: 'Intergamma', url: 'https://www.intergamma.nl' },
    { name: 'VeiligheidNL', url: 'https://www.veiligheid.nl' },
  ],
  macaw: [
    { name: 'SamenGezond', url: 'https://www.samengezond.nl' },
    { name: 'Sustainovate' },
    { name: 'Henkel', url: 'https://www.henkel.nl' },
  ],
  motion10: [
    { name: 'De Goudse Verzekeringen', url: 'https://www.goudse.nl' },
    { name: 'Het Nieuwe Instituut', url: 'https://hetnieuweinstituut.nl' },
    { name: 'Van Gogh Museum', url: 'https://www.vangoghmuseum.nl/en' },
    { name: 'Samskip', url: 'https://www.samskip.com' },
    { name: 'ABN AMRO', url: 'https://www.abnamro.nl/en/personal/index.html' },
    { name: 'Croonwolter&dros', url: 'https://www.croonwolterendros.nl/en' },
    { name: 'TBI', url: 'https://www.tbi.nl' },
    { name: 'Marlink', url: 'https://marlink.com' },
  ],
  ogd: [
    { name: 'Van Nieuwpoort Groep', url: 'https://van-nieuwpoort.com' },
    { name: 'CED', url: 'https://www.ced.nl' },
  ],
};

const data: Record<Locale, Job[]> = {
  en: [
    {
      role: 'Owner · Data & Platform Engineering Consultant',
      company: 'ProRex Consultancy',
      range: 'March 2022 — Present',
      summary:
        'As a freelance consultant I help clients design, build and run data platforms — from Databricks lakehouse architecture to the full platform-engineering stack (Terraform, Terragrunt, GitHub, CI/CD). A multi-year engagement as lead data & platform engineer at construction group TBI broadened me into a well-rounded platform professional; currently building the Heijmans data platform and agentic AI use cases.',
      clients: clients.prorex,
    },
    {
      role: 'Data & Analytics Consultant',
      company: 'GoDataDriven',
      companyUrl: 'https://godatadriven.com',
      range: 'September 2020 — February 2022',
      summary:
        'Designed and built data solutions for major Dutch enterprises. Built the infrastructure for a reusable data platform that is sold to customers, supported sales in improving their offerings and gave presentations to share knowledge about new technologies.',
      clients: clients.gdd,
    },
    {
      role: 'Data & Analytics Consultant',
      company: 'Macaw',
      companyUrl: 'https://www.macaw.nl',
      range: 'September 2019 — August 2020',
      summary:
        'Designed and built data solutions for enterprise clients. As part of the technology committee I was additionally responsible for revising the Macaw data platform, recording best practices and mentoring juniors.',
      clients: clients.macaw,
    },
    {
      role: 'Data & Analytics Consultant',
      company: 'Motion10',
      companyUrl: 'https://motion10.nl',
      range: 'January 2018 — August 2019',
      summary:
        'Designed and built data solutions for a broad portfolio of clients. Also created training materials, trained clients and consultants, and developed a reusable data platform.',
      clients: clients.motion10,
    },
    {
      role: 'Full Stack Developer',
      company: 'Vixion',
      companyUrl: 'https://vixion.nl',
      range: 'May 2017 — December 2017',
      summary:
        'Worked on a single sign-on (SSO) solution for small and medium-sized enterprises, building the API, database and application.',
    },
    {
      role: 'IT Support Specialist',
      company: 'OGD',
      range: 'April 2015 — October 2016',
      summary:
        'First-line support: registering incoming incidents and escalating to second-line where needed. At Van Nieuwpoort Groep I was responsible for upgrading Track It! and improving the change management process. Also worked for CED.',
      clients: clients.ogd,
    },
  ],
  nl: [
    {
      role: 'Eigenaar · Data & Platform Engineering Consultant',
      company: 'ProRex Consultancy',
      range: 'Maart 2022 — heden',
      summary:
        'Als freelance consultant help ik klanten met het ontwerpen, bouwen en beheren van dataplatformen — van Databricks-lakehouse-architectuur tot de volledige platform-engineering-stack (Terraform, Terragrunt, GitHub, CI/CD). Een meerjarige opdracht als lead data & platform engineer bij bouwconcern TBI maakte mij tot een allround platformprofessional; momenteel bouw ik het Heijmans-dataplatform en agentic-AI-toepassingen.',
      clients: clients.prorex,
    },
    {
      role: 'Data & Analytics Consultant',
      company: 'GoDataDriven',
      companyUrl: 'https://godatadriven.com',
      range: 'September 2020 — februari 2022',
      summary:
        'Ontwierp en bouwde dataoplossingen voor grote Nederlandse ondernemingen. Bouwde de infrastructuur voor een herbruikbaar dataplatform dat aan klanten wordt verkocht, ondersteunde sales bij het verbeteren van hun aanbod en gaf presentaties om kennis over nieuwe technologieën te delen.',
      clients: clients.gdd,
    },
    {
      role: 'Data & Analytics Consultant',
      company: 'Macaw',
      companyUrl: 'https://www.macaw.nl',
      range: 'September 2019 — augustus 2020',
      summary:
        'Ontwierp en bouwde dataoplossingen voor enterprise-klanten. Als lid van de technologiecommissie was ik daarnaast verantwoordelijk voor het herzien van het Macaw-dataplatform, het vastleggen van best practices en het begeleiden van juniors.',
      clients: clients.macaw,
    },
    {
      role: 'Data & Analytics Consultant',
      company: 'Motion10',
      companyUrl: 'https://motion10.nl',
      range: 'Januari 2018 — augustus 2019',
      summary:
        'Ontwierp en bouwde dataoplossingen voor een brede portefeuille van klanten. Maakte daarnaast trainingsmateriaal, trainde klanten en consultants en ontwikkelde een herbruikbaar dataplatform.',
      clients: clients.motion10,
    },
    {
      role: 'Fullstack-developer',
      company: 'Vixion',
      companyUrl: 'https://vixion.nl',
      range: 'Mei 2017 — december 2017',
      summary:
        'Werkte aan een single sign-on (SSO)-oplossing voor het mkb en bouwde daarbij de API, de database en de applicatie.',
    },
    {
      role: 'IT-supportspecialist',
      company: 'OGD',
      range: 'April 2015 — oktober 2016',
      summary:
        'Eerstelijnssupport: binnenkomende incidenten registreren en waar nodig escaleren naar de tweede lijn. Bij Van Nieuwpoort Groep was ik verantwoordelijk voor het upgraden van Track It! en het verbeteren van het changemanagementproces. Werkte daarnaast voor CED.',
      clients: clients.ogd,
    },
  ],
};

export function getExperience(locale: Locale): Job[] {
  return data[locale];
}
