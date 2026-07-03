export interface OpenSourceProject {
  name: string;
  tagline: string;
  description: string;
  tech: string[];
  license: string;
  repo: string;
  install?: string;
}

export const openSource: OpenSourceProject[] = [
  {
    name: 'isolinear',
    tagline: 'A keyboard-driven terminal UI for managing Databricks secrets.',
    description:
      'Browse scopes, secrets and ACLs in a three-pane terminal interface — with a workspace picker for Databricks Asset Bundles, profiles and OAuth, lazy-loaded secret values, full CRUD, fuzzy filtering and a command palette. Built on a hexagonal architecture so the domain logic is fully testable without network access. Named after the chips, of course.',
    tech: ['Python 3.11+', 'Textual', 'Databricks SDK', 'uv', 'ruff', 'pytest'],
    license: 'MIT',
    repo: 'https://github.com/misja-pronk/isolinear',
    install: 'pipx install isolinear',
  },
];
