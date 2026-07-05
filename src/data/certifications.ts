import type { Locale } from '../i18n';

export interface Certification {
  name: string;
  issuer: string;
  badge: string; // path under public/
  proof: string;
  description: string;
  certId?: string;
}

const base = [
  {
    name: 'MCSA: Data Engineering with Azure',
    issuer: 'Microsoft',
    badge: 'img/badges/mcsa-data-engineering.png',
    proof: 'https://www.credly.com/badges/20cb6a5f-8ae8-44ca-8008-ab7f6febdc82',
  },
  {
    name: 'MCSE: Data Management and Analytics',
    issuer: 'Microsoft',
    badge: 'img/badges/mcse-data-management.png',
    proof: 'https://www.credly.com/badges/c5164531-b99f-4347-8ebe-55fa3c818e5f',
  },
  {
    name: 'dbt Fundamentals',
    issuer: 'dbt Labs',
    badge: 'img/badges/dbt-fundamentals.png',
    proof: 'https://www.credential.net/9eba8dfd-594e-4faf-b6b0-e1f46c6a057d#gs.shuwjt',
  },
  {
    name: 'Databricks Lakehouse Fundamentals',
    issuer: 'Databricks',
    badge: 'img/badges/databricks-lakehouse.png',
    proof: 'https://credentials.databricks.com/e8be9194-5f17-4cf0-b48c-5e85a2636858',
  },
  {
    name: 'dlt Fundamentals',
    issuer: 'dltHub',
    badge: 'img/badges/dlthub.png',
    proof: 'https://www.linkedin.com/in/misja-pronk/details/certifications/',
    certId: '69d288adea358dc31e0af3cc',
  },
];

const descriptions: Record<Locale, string[]> = {
  en: [
    'Demonstrates knowledge of designing and building analytics and operational solutions on Azure, and implementing big data engineering workflows on HDInsight.',
    'Demonstrates the skills required to build enterprise-scale data solutions and leverage business intelligence data, both on-premises and in cloud environments.',
    'Demonstrates fundamental understanding of models, sources, tests, docs and deployment in dbt.',
    'Demonstrates understanding of fundamental concepts related to the Databricks Lakehouse Platform.',
    'Certifies successful completion of the dlt Fundamentals course: building and deploying production-grade data pipelines with dlt, the open-source Python library for data loading. Certificate ID 69d288adea358dc31e0af3cc.',
  ],
  nl: [
    'Toont kennis aan van het ontwerpen en bouwen van analytics- en operationele oplossingen op Azure en het implementeren van big-data-engineering-workflows op HDInsight.',
    'Toont de vaardigheden aan die nodig zijn om enterprise-dataoplossingen te bouwen en business-intelligence-data te benutten, zowel on-premises als in de cloud.',
    'Toont fundamenteel begrip aan van models, sources, tests, docs en deployment in dbt.',
    'Toont begrip aan van de fundamentele concepten van het Databricks Lakehouse Platform.',
    'Certificeert de succesvolle afronding van de dlt Fundamentals-cursus: productiewaardige datapijplijnen bouwen en deployen met dlt, de open-source Python-bibliotheek voor data loading. Certificaat-ID 69d288adea358dc31e0af3cc.',
  ],
};

export function getCertifications(locale: Locale): Certification[] {
  return base.map((c, i) => ({ ...c, description: descriptions[locale][i]! }));
}

const courseworkText: Record<Locale, string> = {
  en: 'NOTE: ADDITIONAL COURSEWORK ON FILE — MICROSOFT PROFESSIONAL PROGRAM (BIG DATA & DATA SCIENCE TRACKS), 8 EDX CERTIFICATES, 2017–2019.',
  nl: 'OPMERKING: AANVULLENDE CURSUSSEN IN ARCHIEF — MICROSOFT PROFESSIONAL PROGRAM (BIG DATA- & DATA SCIENCE-TRACKS), 8 EDX-CERTIFICATEN, 2017–2019.',
};

export function getCoursework(locale: Locale): string {
  return courseworkText[locale];
}
