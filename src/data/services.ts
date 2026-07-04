import type { Locale } from '../i18n';

export interface Service {
  title: string;
  blurb: string;
  deliverables: string;
}

export interface ServicesContent {
  sheetNo: string;
  title: string;
  intro: string;
  items: Service[];
  ctaLabel: string;
  ctaSubject: string;
  ctaNote: string;
}

const data: Record<Locale, ServicesContent> = {
  en: {
    sheetNo: '02A',
    title: 'SCOPE OF WORKS — ENGAGEMENTS',
    intro: 'FOUR STANDARD WORK PACKAGES. COMBINATIONS AND CUSTOM SCOPES BY AGREEMENT.',
    items: [
      {
        title: 'Data platform build & architecture',
        blurb:
          'Design and build your data platform end to end: data-mesh or lakehouse architecture on Azure and Databricks, all infrastructure as code, governance and CI/CD included — production-ready, and owned by your team when I leave.',
        deliverables: 'TARGET ARCHITECTURE · TERRAFORM/TERRAGRUNT IAC · CI/CD · DOCUMENTATION',
      },
      {
        title: 'Databricks enablement',
        blurb:
          'Get the most out of the Databricks platform: workspace architecture, Unity Catalog governance, Asset Bundles deployment standards, cost control — up to and including agentic AI use cases with your data science team.',
        deliverables: 'WORKSPACE DESIGN · DEPLOYMENT STANDARDS · COST REVIEW · AI USE CASES',
      },
      {
        title: 'Platform engineering & DevOps uplift',
        blurb:
          'Give your teams golden paths instead of tickets: standardized pipelines, reusable Terraform/Terragrunt modules, Kubernetes where it earns its keep, and DevOps ways of working that stick.',
        deliverables: 'GOLDEN PATHS · MODULE LIBRARY · RELEASE AUTOMATION · TEAM WORKFLOWS',
      },
      {
        title: 'Training & coaching',
        blurb:
          'Turn BI and data teams into engineering teams: dbt introduction and standards, Git, DataOps and cloud-engineering practices — taught hands-on, on your own platform, until the team runs without me.',
        deliverables: 'dbt-STANDARDS · GIT/DATAOPS COACHING · HANDS-ON WORKSHOPS',
      },
    ],
    ctaLabel: 'REQUEST A PROPOSAL',
    ctaSubject: 'Request for proposal',
    ctaNote: 'RESPONSE WITHIN TWO WORKING DAYS. NO OBLIGATION, NO BOILERPLATE.',
  },
  nl: {
    sheetNo: '02A',
    title: 'BESTEK — DIENSTEN',
    intro: 'VIER STANDAARD WERKPAKKETTEN. COMBINATIES EN MAATWERK IN OVERLEG.',
    items: [
      {
        title: 'Dataplatform bouwen & architectuur',
        blurb:
          'Ontwerp en bouw van je dataplatform van begin tot eind: data-mesh- of lakehouse-architectuur op Azure en Databricks, alle infrastructuur als code, inclusief governance en CI/CD — productieklaar, en eigendom van je eigen team als ik vertrek.',
        deliverables: 'DOELARCHITECTUUR · TERRAFORM/TERRAGRUNT-IAC · CI/CD · DOCUMENTATIE',
      },
      {
        title: 'Databricks-enablement',
        blurb:
          'Haal het maximale uit het Databricks-platform: workspace-architectuur, Unity Catalog-governance, deploystandaarden met Asset Bundles, kostenbeheersing — tot en met agentic-AI-toepassingen met je datascienceteam.',
        deliverables: 'WORKSPACE-ONTWERP · DEPLOYSTANDAARDEN · KOSTENREVIEW · AI-TOEPASSINGEN',
      },
      {
        title: 'Platform engineering & DevOps-versterking',
        blurb:
          'Geef je teams golden paths in plaats van tickets: gestandaardiseerde pijplijnen, herbruikbare Terraform/Terragrunt-modules, Kubernetes waar het zich terugverdient, en DevOps-werkwijzen die beklijven.',
        deliverables: 'GOLDEN PATHS · MODULEBIBLIOTHEEK · RELEASE-AUTOMATISERING · TEAMWORKFLOWS',
      },
      {
        title: 'Training & coaching',
        blurb:
          'Maak van BI- en datateams engineeringteams: dbt-introductie en -standaarden, Git, DataOps en cloud-engineering-praktijken — hands-on aangeleerd, op je eigen platform, tot het team zonder mij draait.',
        deliverables: 'dbt-STANDAARDEN · GIT/DATAOPS-COACHING · HANDS-ON WORKSHOPS',
      },
    ],
    ctaLabel: 'VRAAG EEN VOORSTEL AAN',
    ctaSubject: 'Aanvraag voorstel',
    ctaNote: 'REACTIE BINNEN TWEE WERKDAGEN. VRIJBLIJVEND, ZONDER STANDAARDWERK.',
  },
};

export function getServices(locale: Locale): ServicesContent {
  return data[locale];
}
