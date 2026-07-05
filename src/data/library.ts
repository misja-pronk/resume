import type { Locale } from '../i18n';

export type BookStatus = 'read' | 'reading' | 'wishlist';

export interface Book {
  title: string;
  author: string;
  discipline: string;
  status: BookStatus;
  cover?: string; // path under public/, e.g. img/books/lotr.jpg
  note?: string;
}

type BookDef = Omit<Book, 'discipline'> & { discipline: Record<Locale, string> };

const d = {
  dataEng: { en: 'Data Engineering', nl: 'Data engineering' },
  dataModeling: { en: 'Data Modeling', nl: 'Datamodelleren' },
  dataArch: { en: 'Data Architecture', nl: 'Data-architectuur' },
  dataSystems: { en: 'Data Systems', nl: 'Datasystemen' },
  dataScience: { en: 'Data Science', nl: 'Data science' },
  dataViz: { en: 'Data Visualization', nl: 'Datavisualisatie' },
  dataEthics: { en: 'Data Ethics', nl: 'Data-ethiek' },
  ml: { en: 'Machine Learning', nl: 'Machine learning' },
  bi: { en: 'Business Intelligence', nl: 'Business intelligence' },
  sql: { en: 'SQL', nl: 'SQL' },
  python: { en: 'Python', nl: 'Python' },
  go: { en: 'Go', nl: 'Go' },
  programming: { en: 'Programming', nl: 'Programmeren' },
  craft: { en: 'Software Craftsmanship', nl: 'Softwarevakmanschap' },
  design: { en: 'Software Design', nl: 'Softwareontwerp' },
  iac: { en: 'Infrastructure as Code', nl: 'Infrastructure as code' },
  containers: { en: 'Containers', nl: 'Containers' },
  kubernetes: { en: 'Kubernetes', nl: 'Kubernetes' },
  web: { en: 'Web Development', nl: 'Webontwikkeling' },
  git: { en: 'Version Control', nl: 'Versiebeheer' },
  cloud: { en: 'Cloud Architecture', nl: 'Cloudarchitectuur' },
  automation: { en: 'Automation', nl: 'Automatisering' },
  security: { en: 'Software Security', nl: 'Softwarebeveiliging' },
  fiction: { en: 'Fiction', nl: 'Fictie' },
  style: { en: 'Style', nl: 'Stijl' },
};

/**
 * The library — books read, in hand, or on order.
 * status: 'read' · 'reading' · 'wishlist'
 */
const books: BookDef[] = [
  // --- data
  { title: 'Designing Data-Intensive Applications', author: 'Martin Kleppmann', discipline: d.dataSystems, status: 'read', cover: 'img/books/ddia.jpg' },
  { title: 'The Data Warehouse Toolkit', author: 'Ralph Kimball & Margy Ross', discipline: d.dataModeling, status: 'read', cover: 'img/books/dw-toolkit.jpg' },
  { title: 'Data Management at Scale', author: 'Piethein Strengholt', discipline: d.dataArch, status: 'read', cover: 'img/books/data-mgmt-scale.jpg' },
  { title: 'Data Pipelines with Apache Airflow', author: 'Bas Harenslak & Julian de Ruiter', discipline: d.dataEng, status: 'read', cover: 'img/books/airflow.jpg' },
  { title: 'Spark: The Definitive Guide', author: 'Bill Chambers & Matei Zaharia', discipline: d.dataEng, status: 'read', cover: 'img/books/spark-definitive.jpg' },
  { title: 'The Definitive Guide to DAX', author: 'Marco Russo & Alberto Ferrari', discipline: d.bi, status: 'read', cover: 'img/books/bi-excel-ssas.jpg' },
  { title: 'Data Science for Business', author: 'Foster Provost & Tom Fawcett', discipline: d.dataScience, status: 'read', cover: 'img/books/ds-for-business.jpg' },
  { title: 'Machine Learning with Python Cookbook', author: 'Chris Albon', discipline: d.ml, status: 'read', cover: 'img/books/ml-python-cookbook.jpg' },
  { title: 'Ethics of Data and Analytics', author: 'Kirsten Martin', discipline: d.dataEthics, status: 'read', cover: 'img/books/ethics-of-data.jpg' },
  { title: 'The Wall Street Journal Guide to Information Graphics', author: 'Dona M. Wong', discipline: d.dataViz, status: 'read', cover: 'img/books/info-graphics.jpg' },
  // --- sql
  { title: 'The Art of SQL', author: 'Stéphane Faroult', discipline: d.sql, status: 'read', cover: 'img/books/art-of-sql.jpg' },
  { title: 'SQL Cookbook', author: 'Anthony Molinaro', discipline: d.sql, status: 'read', cover: 'img/books/sql-cookbook.jpg' },
  // --- python
  { title: 'Fluent Python', author: 'Luciano Ramalho', discipline: d.python, status: 'read', cover: 'img/books/fluent-python.jpg' },
  { title: 'Effective Python', author: 'Brett Slatkin', discipline: d.python, status: 'read', cover: 'img/books/effective-python.jpg' },
  { title: 'Python Cookbook', author: 'David Beazley & Brian K. Jones', discipline: d.python, status: 'read', cover: 'img/books/python-cookbook.jpg' },
  { title: 'Introduction to Computing Using Python', author: 'Ljubomir Perkovic', discipline: d.python, status: 'read', cover: 'img/books/intro-computing-python.jpg' },
  // --- other languages
  { title: 'C# in Depth', author: 'Jon Skeet', discipline: d.programming, status: 'read', cover: 'img/books/csharp-in-depth.jpg' },
  { title: 'Go in Action', author: 'William Kennedy', discipline: d.go, status: 'read', cover: 'img/books/go-in-action.jpg' },
  { title: 'Introducing Go', author: 'Caleb Doxsey', discipline: d.go, status: 'read', cover: 'img/books/introducing-go.jpg' },
  // --- web & tooling
  { title: 'Eloquent JavaScript', author: 'Marijn Haverbeke', discipline: d.web, status: 'read', cover: 'img/books/eloquent-js.jpg' },
  { title: 'Learning React', author: 'Alex Banks & Eve Porcello', discipline: d.web, status: 'read', cover: 'img/books/learning-react.jpg' },
  { title: 'Learning Git', author: 'Anna Skoulikari', discipline: d.git, status: 'read', cover: 'img/books/learning-git.jpg' },
  // --- craft & design
  { title: 'Clean Code', author: 'Robert C. Martin', discipline: d.craft, status: 'read', cover: 'img/books/clean-code.jpg' },
  { title: 'Refactoring', author: 'Martin Fowler', discipline: d.craft, status: 'read', cover: 'img/books/refactoring.jpg' },
  { title: 'Design Patterns Explained', author: 'Alan Shalloway & James Trott', discipline: d.design, status: 'read', cover: 'img/books/design-patterns-explained.jpg' },
  { title: 'UML 2 and the Unified Process', author: 'Jim Arlow & Ila Neustadt', discipline: d.design, status: 'read', cover: 'img/books/uml2.jpg' },
  // --- infra & cloud
  { title: 'Terraform in Action', author: 'Scott Winkler', discipline: d.iac, status: 'read', cover: 'img/books/terraform-in-action.jpg' },
  { title: 'HashiCorp Infrastructure Automation Certification Guide', author: 'Ravi Mishra', discipline: d.iac, status: 'read', cover: 'img/books/hashicorp-cert.jpg' },
  { title: 'Docker: Up & Running', author: 'Sean Kane & Karl Matthias', discipline: d.containers, status: 'read', cover: 'img/books/docker-up-running.jpg' },
  { title: 'Kubernetes: Up and Running', author: 'Kelsey Hightower, Brendan Burns & Joe Beda', discipline: d.kubernetes, status: 'read', cover: 'img/books/k8s-up-running.jpg' },
  { title: 'The Kubernetes Book', author: 'Nigel Poulton', discipline: d.kubernetes, status: 'read', cover: 'img/books/kubernetes-book.jpg' },
  { title: 'Implementing Azure Cloud Design Patterns', author: 'Oliver Michalski & Stefano Demiliani', discipline: d.cloud, status: 'read', cover: 'img/books/azure-patterns.jpg' },
  { title: 'Windows PowerShell in Action', author: 'Bruce Payette', discipline: d.automation, status: 'read', cover: 'img/books/powershell-in-action.jpg' },
  // --- off duty
  { title: 'Innocent Code', author: 'Sverre H. Huseby', discipline: d.security, status: 'read', cover: 'img/books/innocent-code.jpg' },
  { title: 'The Lord of the Rings', author: 'J.R.R. Tolkien', discipline: d.fiction, status: 'read', cover: 'img/books/lotr.jpg' },
  { title: 'The Alchemist', author: 'Paulo Coelho', discipline: d.fiction, status: 'read', cover: 'img/books/alchemist.jpg' },
  { title: 'Dressing the Man', author: 'Alan Flusser', discipline: d.style, status: 'read', cover: 'img/books/dressing-the-man.jpg' },
];

export function getLibrary(locale: Locale): Book[] {
  return books.map((b) => ({ ...b, discipline: b.discipline[locale] }));
}
