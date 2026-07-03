export interface Specialism {
  name: string;
  blurb: string;
  tools: string[];
}

/** The load-bearing expertise — deep specialisms, shown above the general toolbox. */
export const specialisms: Specialism[] = [
  {
    name: 'Databricks Platform',
    blurb:
      'Extensive, day-to-day expertise across the Databricks platform: Spark and Delta Lake engineering, workspace architecture, governance, Asset Bundles and cost control — up to and including agentic AI use cases with data science teams.',
    tools: ['Spark', 'Delta Lake', 'Asset Bundles', 'Agentic AI', 'dbt', 'Python'],
  },
  {
    name: 'Platform Engineering & DevOps',
    blurb:
      'The full platform-engineering stack: infrastructure as code, automated testing, release pipelines and DevOps ways of working — so teams ship data products instead of fighting environments.',
    tools: ['Terraform', 'Terragrunt', 'GitHub Actions', 'Azure DevOps', 'CI/CD'],
  },
  {
    name: 'Metadata-Driven Data Platforms',
    blurb:
      'My signature approach: platforms that integrate hundreds of sources through configuration instead of code duplication — cheaper to extend, easier to maintain, faster to onboard.',
    tools: ['Data Factory', 'Databricks', 'Azure', 'SQL'],
  },
  {
    name: 'Open Source First',
    blurb:
      'A love for open source runs through everything I build: open formats, open tooling and open standards over vendor lock-in. I also ship my own — isolinear, an open-source terminal UI for managing Databricks secrets.',
    tools: ['isolinear', 'dbt', 'Spark', 'Delta Lake', 'Terraform'],
  },
];

export interface SkillGroup {
  grouping: string;
  icon: string; // inline SVG path (24x24 viewBox)
  skills: { name: string; link?: string }[];
}

export const skillGroups: SkillGroup[] = [
  {
    grouping: 'Azure',
    icon: 'M6.5 17.5 13 4l4 8-6 5.5h9L13 4M2 20h11l-4.5-9z',
    skills: [
      { name: 'Databricks', link: 'https://learn.microsoft.com/en-us/azure/databricks/scenarios/what-is-azure-databricks' },
      { name: 'Synapse', link: 'https://learn.microsoft.com/en-us/azure/synapse-analytics/overview-what-is' },
      { name: 'Data Factory', link: 'https://learn.microsoft.com/en-us/azure/data-factory/introduction' },
      { name: 'Data Lake Storage', link: 'https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction' },
      { name: 'Functions', link: 'https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview' },
      { name: 'App Service', link: 'https://learn.microsoft.com/en-us/azure/app-service/overview' },
      { name: 'Container Instances', link: 'https://learn.microsoft.com/en-us/azure/container-instances/container-instances-overview' },
      { name: 'Container Registry', link: 'https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro' },
      { name: 'SQL Database', link: 'https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview' },
      { name: 'PostgreSQL', link: 'https://learn.microsoft.com/en-us/azure/postgresql/overview' },
      { name: 'DevOps', link: 'https://azure.microsoft.com/en-us/services/devops/' },
      { name: 'Logic Apps', link: 'https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-overview' },
      { name: 'Key Vault', link: 'https://learn.microsoft.com/en-us/azure/key-vault/general/overview' },
      { name: 'Entra ID', link: 'https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis' },
      { name: 'Blob Storage', link: 'https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview' },
      { name: 'Virtual Network', link: 'https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview' },
      { name: 'Private Link', link: 'https://azure.microsoft.com/en-us/services/private-link/' },
      { name: 'Log Analytics', link: 'https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview' },
      { name: 'Azure Policy', link: 'https://learn.microsoft.com/en-us/azure/governance/policy/overview' },
      { name: 'Cost Management', link: 'https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview' },
      { name: 'Virtual Machines', link: 'https://learn.microsoft.com/en-us/azure/virtual-machines/windows/overview' },
    ],
  },
  {
    grouping: 'Data & Databases',
    icon: 'M12 3C7.58 3 4 4.79 4 7s3.58 4 8 4 8-1.79 8-4-3.58-4-8-4M4 9v3c0 2.21 3.58 4 8 4s8-1.79 8-4V9c0 2.21-3.58 4-8 4s-8-1.79-8-4m0 5v3c0 2.21 3.58 4 8 4s8-1.79 8-4v-3c0 2.21-3.58 4-8 4s-8-1.79-8-4Z',
    skills: [
      { name: 'SQL Server', link: 'https://www.microsoft.com/en-us/sql-server' },
      { name: 'PostgreSQL', link: 'https://www.postgresql.org' },
      { name: 'Delta Lake', link: 'https://docs.delta.io/latest/index.html' },
      { name: 'Databricks', link: 'https://databricks.com' },
      { name: 'Spark', link: 'https://spark.apache.org' },
      { name: 'dbt', link: 'https://www.getdbt.com' },
      { name: 'Fivetran', link: 'https://fivetran.com' },
      { name: 'Great Expectations', link: 'https://greatexpectations.io' },
      { name: 'Neo4j', link: 'https://neo4j.com' },
    ],
  },
  {
    grouping: 'Programming',
    icon: 'm8 6-6 6 6 6 1.4-1.4L4.8 12l4.6-4.6zm8 0-1.4 1.4 4.6 4.6-4.6 4.6L16 18l6-6z',
    skills: [
      { name: 'Python' },
      { name: 'SQL' },
      { name: 'C#' },
      { name: 'Java' },
      { name: 'PowerShell' },
      { name: 'Cypher' },
      { name: 'U-SQL' },
    ],
  },
  {
    grouping: 'Cloud & Infrastructure',
    icon: 'M19.35 10.04A7.49 7.49 0 0 0 12 4C9.11 4 6.6 5.64 5.35 8.04A5.994 5.994 0 0 0 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96Z',
    skills: [
      { name: 'Terraform', link: 'https://www.terraform.io' },
      { name: 'Terragrunt', link: 'https://terragrunt.gruntwork.io' },
      { name: 'GitHub Actions', link: 'https://github.com/features/actions' },
      { name: 'Bicep / ARM', link: 'https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview' },
      { name: 'Kubernetes', link: 'https://kubernetes.io' },
      { name: 'Docker', link: 'https://docker.com' },
      { name: 'Linux', link: 'https://www.linux.org' },
      { name: 'Cloud Custodian', link: 'https://cloudcustodian.io' },
      { name: 'Git', link: 'https://git-scm.com' },
      { name: 'Azure DevOps', link: 'https://azure.microsoft.com/en-us/services/devops/' },
      { name: 'GitLab', link: 'https://about.gitlab.com' },
      { name: 'GitHub', link: 'https://github.com' },
    ],
  },
  {
    grouping: 'Architecture & Methods',
    icon: 'M12 2 2 7l10 5 10-5-10-5M2 17l10 5 10-5M2 12l10 5 10-5',
    skills: [
      { name: 'Dimensional Modeling', link: 'https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/' },
      { name: 'Data Modeling' },
      { name: 'Graph Modeling' },
      { name: 'UML' },
      { name: 'Agile', link: 'https://agilemanifesto.org' },
      { name: 'Scrum', link: 'https://www.scrum.org' },
      { name: 'Waterfall' },
    ],
  },
  {
    grouping: 'Languages & Soft Skills',
    icon: 'M12 1a11 11 0 1 0 11 11A11 11 0 0 0 12 1m6.9 7h-3.2a15.6 15.6 0 0 0-1.5-4.1A9 9 0 0 1 18.9 8M12 3.2A13.8 13.8 0 0 1 13.8 8h-3.6A13.8 13.8 0 0 1 12 3.2M3.5 14a8.9 8.9 0 0 1 0-4h3.4a16.5 16.5 0 0 0 0 4m.6 2h3.2a15.6 15.6 0 0 0 1.5 4.1A9 9 0 0 1 5.1 16m3.2-8H5.1a9 9 0 0 1 4.7-4.1A15.6 15.6 0 0 0 8.3 8M12 20.8a13.8 13.8 0 0 1-1.8-4.8h3.6a13.8 13.8 0 0 1-1.8 4.8m2.3-6.8H9.7a14.6 14.6 0 0 1 0-4h4.6a14.6 14.6 0 0 1 0 4m.5 6.1a15.6 15.6 0 0 0 1.5-4.1h3.2a9 9 0 0 1-4.7 4.1m2.3-6.1a16.5 16.5 0 0 0 0-4h3.4a8.9 8.9 0 0 1 0 4Z',
    skills: [
      { name: 'Dutch (native)' },
      { name: 'English (fluent)' },
      { name: 'Spanish (conversational)' },
      { name: 'Presenting' },
      { name: 'Training & coaching' },
    ],
  },
];
