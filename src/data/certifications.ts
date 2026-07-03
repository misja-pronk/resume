import type { Locale } from '../i18n';

export interface Certification {
  name: string;
  issuer: string;
  badge: string; // path under public/
  proof: string;
  description: string;
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
];

const descriptions: Record<Locale, string[]> = {
  en: [
    'Demonstrates knowledge of designing and building analytics and operational solutions on Azure, and implementing big data engineering workflows on HDInsight.',
    'Demonstrates the skills required to build enterprise-scale data solutions and leverage business intelligence data, both on-premises and in cloud environments.',
    'Demonstrates fundamental understanding of models, sources, tests, docs and deployment in dbt.',
    'Demonstrates understanding of fundamental concepts related to the Databricks Lakehouse Platform.',
  ],
  nl: [
    'Toont kennis aan van het ontwerpen en bouwen van analytics- en operationele oplossingen op Azure en het implementeren van big-data-engineering-workflows op HDInsight.',
    'Toont de vaardigheden aan die nodig zijn om enterprise-dataoplossingen te bouwen en business-intelligence-data te benutten, zowel on-premises als in de cloud.',
    'Toont fundamenteel begrip aan van models, sources, tests, docs en deployment in dbt.',
    'Toont begrip aan van de fundamentele concepten van het Databricks Lakehouse Platform.',
  ],
};

export function getCertifications(locale: Locale): Certification[] {
  return base.map((c, i) => ({ ...c, description: descriptions[locale][i]! }));
}
