import type { Locale } from '../i18n';

export interface Specialism {
  name: string;
  blurb: string;
  tools: string[];
}

const specialismsData: Record<Locale, Specialism[]> = {
  en: [
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
  ],
  nl: [
    {
      name: 'Databricks-platform',
      blurb:
        'Uitgebreide, dagelijkse expertise over het hele Databricks-platform: Spark- en Delta Lake-engineering, workspace-architectuur, governance, Asset Bundles en kostenbeheersing — tot en met agentic-AI-toepassingen met datascienceteams.',
      tools: ['Spark', 'Delta Lake', 'Asset Bundles', 'Agentic AI', 'dbt', 'Python'],
    },
    {
      name: 'Platform engineering & DevOps',
      blurb:
        'De volledige platform-engineering-stack: infrastructure as code, geautomatiseerd testen, releasepijplijnen en DevOps-werkwijzen — zodat teams dataproducten opleveren in plaats van vechten met omgevingen.',
      tools: ['Terraform', 'Terragrunt', 'GitHub Actions', 'Azure DevOps', 'CI/CD'],
    },
    {
      name: 'Metadata-gedreven dataplatformen',
      blurb:
        'Mijn handtekening: platformen die honderden bronnen integreren via configuratie in plaats van codeduplicatie — goedkoper uit te breiden, makkelijker te onderhouden en sneller in gebruik te nemen.',
      tools: ['Data Factory', 'Databricks', 'Azure', 'SQL'],
    },
    {
      name: 'Open source eerst',
      blurb:
        'Liefde voor open source loopt door alles wat ik bouw: open formaten, open tooling en open standaarden boven vendor lock-in. Ik lever ook zelf — isolinear, een open-source terminal-UI voor het beheren van Databricks-secrets.',
      tools: ['isolinear', 'dbt', 'Spark', 'Delta Lake', 'Terraform'],
    },
  ],
};

export function getSpecialisms(locale: Locale): Specialism[] {
  return specialismsData[locale];
}

export interface SkillGroup {
  grouping: string;
  skills: { name: string; link?: string }[];
}

const azure = [
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
];

const databricks = [
  { name: 'Databricks', link: 'https://databricks.com' },
  { name: 'Spark', link: 'https://spark.apache.org' },
  { name: 'Delta Lake', link: 'https://docs.delta.io/latest/index.html' },
  { name: 'Unity Catalog', link: 'https://www.databricks.com/product/unity-catalog' },
  { name: 'Asset Bundles', link: 'https://docs.databricks.com/en/dev-tools/bundles/index.html' },
  { name: 'Workflows', link: 'https://www.databricks.com/product/workflows' },
  { name: 'Databricks SQL', link: 'https://www.databricks.com/product/databricks-sql' },
  { name: 'Databricks CLI', link: 'https://docs.databricks.com/en/dev-tools/cli/index.html' },
  { name: 'Agentic AI / Mosaic AI', link: 'https://www.databricks.com/product/artificial-intelligence' },
];

const dataDb = [
  { name: 'dbt', link: 'https://www.getdbt.com' },
  { name: 'dlt (dlthub)', link: 'https://dlthub.com' },
  { name: 'SQL Server', link: 'https://www.microsoft.com/en-us/sql-server' },
  { name: 'PostgreSQL', link: 'https://www.postgresql.org' },
  { name: 'Fivetran', link: 'https://fivetran.com' },
  { name: 'Great Expectations', link: 'https://greatexpectations.io' },
  { name: 'Neo4j', link: 'https://neo4j.com' },
];

const programming = [
  { name: 'Python' },
  { name: 'SQL' },
  { name: 'C#' },
  { name: 'Java' },
  { name: 'PowerShell' },
  { name: 'Cypher' },
  { name: 'U-SQL' },
];

const cloud = [
  { name: 'Terraform', link: 'https://www.terraform.io' },
  { name: 'Terragrunt', link: 'https://terragrunt.gruntwork.io' },
  { name: 'GitHub Actions', link: 'https://github.com/features/actions' },
  { name: 'Bicep / ARM', link: 'https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview' },
  { name: 'Kubernetes', link: 'https://kubernetes.io' },
  { name: 'Docker', link: 'https://docker.com' },
  { name: 'Linux', link: 'https://www.linux.org' },
  { name: 'Cloud Custodian', link: 'https://cloudcustodian.io' },
  { name: 'Azure DevOps', link: 'https://azure.microsoft.com/en-us/services/devops/' },
  { name: 'GitLab', link: 'https://about.gitlab.com' },
  { name: 'GitHub', link: 'https://github.com' },
];

const devTools = [
  { name: 'uv', link: 'https://docs.astral.sh/uv/' },
  { name: 'mise', link: 'https://mise.jdx.dev' },
  { name: 'ruff', link: 'https://docs.astral.sh/ruff/' },
  { name: 'pytest', link: 'https://pytest.org' },
  { name: 'Databricks CLI', link: 'https://docs.databricks.com/en/dev-tools/cli/index.html' },
  { name: 'kubectl', link: 'https://kubernetes.io/docs/reference/kubectl/' },
  { name: 'Git', link: 'https://git-scm.com' },
];

const methodsEn = [
  { name: 'Data Mesh' },
  { name: 'DataOps' },
  { name: 'Dimensional Modeling', link: 'https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/' },
  { name: 'Data Modeling' },
  { name: 'Graph Modeling' },
  { name: 'UML' },
  { name: 'Agile', link: 'https://agilemanifesto.org' },
  { name: 'Scrum', link: 'https://www.scrum.org' },
  { name: 'Waterfall' },
];

const methodsNl = [
  { name: 'Data mesh' },
  { name: 'DataOps' },
  { name: 'Dimensionaal modelleren', link: 'https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/' },
  { name: 'Datamodelleren' },
  { name: 'Grafmodelleren' },
  { name: 'UML' },
  { name: 'Agile', link: 'https://agilemanifesto.org' },
  { name: 'Scrum', link: 'https://www.scrum.org' },
  { name: 'Waterval' },
];

const softEn = [
  { name: 'Dutch (native)' },
  { name: 'English (fluent)' },
  { name: 'Spanish (conversational)' },
  { name: 'Presenting' },
  { name: 'Training & coaching' },
];

const softNl = [
  { name: 'Nederlands (moedertaal)' },
  { name: 'Engels (vloeiend)' },
  { name: 'Spaans (conversatie)' },
  { name: 'Presenteren' },
  { name: 'Training & coaching' },
];

const groupsData: Record<Locale, SkillGroup[]> = {
  en: [
    { grouping: 'Azure', skills: azure },
    { grouping: 'Databricks', skills: databricks },
    { grouping: 'Data & Databases', skills: dataDb },
    { grouping: 'Programming', skills: programming },
    { grouping: 'Cloud & Infrastructure', skills: cloud },
    { grouping: 'Developer Tooling & CLIs', skills: devTools },
    { grouping: 'Architecture & Methods', skills: methodsEn },
    { grouping: 'Languages & Soft Skills', skills: softEn },
  ],
  nl: [
    { grouping: 'Azure', skills: azure },
    { grouping: 'Databricks', skills: databricks },
    { grouping: 'Data & databases', skills: dataDb },
    { grouping: 'Programmeertalen', skills: programming },
    { grouping: 'Cloud & infrastructuur', skills: cloud },
    { grouping: "Developer tooling & CLI's", skills: devTools },
    { grouping: 'Architectuur & methoden', skills: methodsNl },
    { grouping: 'Talen & soft skills', skills: softNl },
  ],
};

export function getSkillGroups(locale: Locale): SkillGroup[] {
  return groupsData[locale];
}
