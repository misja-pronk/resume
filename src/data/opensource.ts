import type { Locale } from '../i18n';

export interface OpenSourceProject {
  name: string;
  tagline: string;
  description: string;
  tech: string[];
  license: string;
  repo: string;
  install: string;
  run: string;
}

const shared = [
  {
    name: 'isolinear',
    tech: ['Python 3.11+', 'Textual', 'Databricks SDK', 'uv', 'ruff', 'pytest'],
    license: 'MIT',
    repo: 'https://github.com/misja-pronk/isolinear',
    install: 'pipx install isolinear',
    run: 'iso',
  },
  {
    name: 'dbt-4ps-staging',
    tech: ['Python 3.11+', 'dbt', 'Databricks', 'CDM / bc2adls', 'uv', 'ruff'],
    license: 'MIT',
    repo: 'https://github.com/misja-pronk/dbt-4ps-staging',
    install: 'uv tool install dbt-4ps-generator',
    run: 'dbt-4ps-generator generate',
  },
];

const text: Record<Locale, { tagline: string; description: string }[]> = {
  en: [
    {
      tagline: 'A keyboard-driven terminal UI for managing Databricks secrets.',
      description:
        'Browse scopes, secrets and ACLs in a three-pane terminal interface — with a workspace picker for Databricks Asset Bundles, profiles and OAuth, lazy-loaded secret values, full CRUD, fuzzy filtering and a command palette. Built on a hexagonal architecture so the domain logic is fully testable without network access. Named after the chips, of course.',
    },
    {
      tagline: 'A generator that turns 4PS Construct (Business Central) exports into a Databricks dbt staging layer.',
      description:
        'bc2adls exports Business Central tables as CSV deltas plus CDM metadata; this CLI turns that metadata into dbt staging models — one streaming table per source table, with typed columns, snake_case names, column documentation and primary-key tests — so nobody hand-writes staging models again. Born from the 4PS extraction patterns at construction clients, published so the next data team does not start from zero.',
    },
  ],
  nl: [
    {
      tagline: 'Een toetsenbordgedreven terminal-UI voor het beheren van Databricks-secrets.',
      description:
        'Blader door scopes, secrets en ACL’s in een terminalinterface met drie panelen — met een workspace-kiezer voor Databricks Asset Bundles, profielen en OAuth, lazy geladen secret-waarden, volledige CRUD, fuzzy filteren en een command palette. Gebouwd op een hexagonale architectuur zodat de domeinlogica volledig testbaar is zonder netwerktoegang. Vernoemd naar de chips, uiteraard.',
    },
    {
      tagline: 'Een generator die 4PS Construct-exports (Business Central) omzet in een Databricks dbt-staginglaag.',
      description:
        'bc2adls exporteert Business Central-tabellen als CSV-delta’s plus CDM-metadata; deze CLI zet die metadata om in dbt-stagingmodellen — één streaming table per brontabel, met getypeerde kolommen, snake_case-namen, kolomdocumentatie en primary-key-tests — zodat niemand stagingmodellen meer met de hand schrijft. Ontstaan uit de 4PS-extractiepatronen bij bouwopdrachtgevers, gepubliceerd zodat het volgende datateam niet bij nul begint.',
    },
  ],
};

export function getOpenSource(locale: Locale): OpenSourceProject[] {
  return text[locale].map((t, i) => ({ ...shared[i], ...t }));
}
