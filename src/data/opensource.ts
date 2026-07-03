import type { Locale } from '../i18n';

export interface OpenSourceProject {
  name: string;
  tagline: string;
  description: string;
  tech: string[];
  license: string;
  repo: string;
  install?: string;
}

const shared = {
  name: 'isolinear',
  tech: ['Python 3.11+', 'Textual', 'Databricks SDK', 'uv', 'ruff', 'pytest'],
  license: 'MIT',
  repo: 'https://github.com/misja-pronk/isolinear',
  install: 'pipx install isolinear',
};

const text: Record<Locale, { tagline: string; description: string }[]> = {
  en: [
    {
      tagline: 'A keyboard-driven terminal UI for managing Databricks secrets.',
      description:
        'Browse scopes, secrets and ACLs in a three-pane terminal interface — with a workspace picker for Databricks Asset Bundles, profiles and OAuth, lazy-loaded secret values, full CRUD, fuzzy filtering and a command palette. Built on a hexagonal architecture so the domain logic is fully testable without network access. Named after the chips, of course.',
    },
  ],
  nl: [
    {
      tagline: 'Een toetsenbordgedreven terminal-UI voor het beheren van Databricks-secrets.',
      description:
        'Blader door scopes, secrets en ACL’s in een terminalinterface met drie panelen — met een workspace-kiezer voor Databricks Asset Bundles, profielen en OAuth, lazy geladen secret-waarden, volledige CRUD, fuzzy filteren en een command palette. Gebouwd op een hexagonale architectuur zodat de domeinlogica volledig testbaar is zonder netwerktoegang. Vernoemd naar de chips, uiteraard.',
    },
  ],
};

export function getOpenSource(locale: Locale): OpenSourceProject[] {
  return text[locale].map((t, i) => ({ ...shared, ...t }));
}
