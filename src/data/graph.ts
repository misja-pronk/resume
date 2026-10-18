// The as-built graph: nodes are [id, label, group, radius]; the component lays them out.
export type Group = 'person' | 'family' | 'work' | 'oss' | 'hobby';

export interface GEdge {
  source: string;
  target: string;
  rel: string;
}

export const defs: [string, string, Group, number][] = [
  ['misja', 'MISJA', 'person', 30],
  // family
  ['wife', 'WIFE', 'family', 15],
  ['junior', 'JUNIOR v1.0', 'family', 13],
  ['rex', 'REX 🐾', 'family', 13],
  // work
  ['prorex', 'PROREX', 'work', 16],
  ['heijmans', 'HEIJMANS', 'work', 14],
  ['tbi', 'TBI', 'work', 14],
  ['vattenfall', 'VATTENFALL', 'work', 12],
  ['databricks', 'DATABRICKS', 'work', 16],
  ['terraform', 'TERRAFORM', 'work', 13],
  ['terragrunt', 'TERRAGRUNT', 'work', 12],
  ['dbt', 'DBT', 'work', 12],
  ['github', 'GITHUB', 'work', 12],
  ['neo4j', 'NEO4J', 'work', 13],
  ['cypher', 'CYPHER', 'work', 11],
  // oss
  ['isolinear', 'ISOLINEAR', 'oss', 14],
  ['dbt4ps', 'DBT-4PS-STAGING', 'oss', 12],
  // hobbies
  ['wood', 'WOODWORKING', 'hobby', 12],
  ['tiny', 'TINY HOUSES', 'hobby', 12],
  ['house', 'OWN HOUSE', 'hobby', 11],
  ['bbq', 'BBQ', 'hobby', 11],
  ['dining', 'FINE DINING', 'hobby', 11],
  ['homeauto', 'HOME AUTOMATION', 'hobby', 12],
  ['desk', 'DESK SETUP', 'hobby', 10],
  ['pcs', 'CUSTOM PCs', 'hobby', 10],
  ['keebs', 'MECH KEYBOARDS', 'hobby', 10],
  ['ktm', 'KTM 1190', 'hobby', 10],
  ['guitars', 'GUITARS', 'hobby', 10],
];

export const edges: GEdge[] = [
  { source: 'misja', target: 'wife', rel: 'MARRIED_TO' },
  { source: 'misja', target: 'junior', rel: 'EXPECTING' },
  { source: 'wife', target: 'junior', rel: 'EXPECTING' },
  { source: 'misja', target: 'rex', rel: 'WALKS' },
  { source: 'misja', target: 'prorex', rel: 'OWNS' },
  { source: 'prorex', target: 'heijmans', rel: 'WORKS_FOR' },
  { source: 'prorex', target: 'tbi', rel: 'WORKED_FOR' },
  { source: 'prorex', target: 'vattenfall', rel: 'WORKED_FOR' },
  { source: 'misja', target: 'databricks', rel: 'EXPERT_IN' },
  { source: 'misja', target: 'terraform', rel: 'AUTOMATES_WITH' },
  { source: 'terraform', target: 'terragrunt', rel: 'WRAPPED_BY' },
  { source: 'misja', target: 'dbt', rel: 'TRANSFORMS_WITH' },
  { source: 'misja', target: 'github', rel: 'SHIPS_VIA' },
  { source: 'misja', target: 'neo4j', rel: 'LOVES' },
  { source: 'neo4j', target: 'cypher', rel: 'SPEAKS' },
  { source: 'misja', target: 'isolinear', rel: 'AUTHORED' },
  { source: 'isolinear', target: 'databricks', rel: 'MANAGES_SECRETS_OF' },
  { source: 'misja', target: 'dbt4ps', rel: 'AUTHORED' },
  { source: 'dbt4ps', target: 'dbt', rel: 'GENERATES_MODELS_FOR' },
  { source: 'dbt4ps', target: 'tbi', rel: 'BORN_AT' },
  { source: 'heijmans', target: 'databricks', rel: 'RUNS_ON' },
  { source: 'tbi', target: 'terragrunt', rel: 'BUILT_WITH' },
  { source: 'misja', target: 'wood', rel: 'CRAFTS' },
  { source: 'wood', target: 'tiny', rel: 'SCALES_TO' },
  { source: 'tiny', target: 'house', rel: 'DREAMS_OF' },
  { source: 'misja', target: 'bbq', rel: 'SMOKES' },
  { source: 'bbq', target: 'dining', rel: 'PAIRS_WITH' },
  { source: 'misja', target: 'homeauto', rel: 'AUTOMATES' },
  { source: 'homeauto', target: 'desk', rel: 'POWERS' },
  { source: 'misja', target: 'pcs', rel: 'BUILDS' },
  { source: 'misja', target: 'keebs', rel: 'SOLDERS' },
  { source: 'pcs', target: 'desk', rel: 'DRIVES' },
  { source: 'keebs', target: 'desk', rel: 'CLACKS_ON' },
  { source: 'misja', target: 'ktm', rel: 'RIDES' },
  { source: 'misja', target: 'guitars', rel: 'PLAYS' },
];
