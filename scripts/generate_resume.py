# /// script
# requires-python = ">=3.11"
# dependencies = ["reportlab>=4.0"]
# ///
"""Generate the resume PDFs into public/docs/.

Produces a general resume plus three role-targeted variants (architect,
data engineer, platform engineer), each in English and Dutch:

    uv run scripts/generate_resume.py

Same facts, different lens: each variant reorders and reframes the
experience bullets for the target role.
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

INK = colors.HexColor("#16324f")
DIM = colors.HexColor("#47617c")
ACCENT = colors.HexColor("#0d6fb8")
LINE = colors.HexColor("#c4cfda")

OUT = Path(__file__).resolve().parent.parent / "public" / "docs"

# ---------------------------------------------------------------- shared base

BASE = {
    "en": {
        "subtitle": "Owner, ProRex Consultancy · Friesland, The Netherlands",
        "contact": (
            '<a href="mailto:misja@prorexconsultancy.nl" color="#0d6fb8">misja@prorexconsultancy.nl</a> · '
            '<a href="https://www.linkedin.com/in/misja-pronk" color="#0d6fb8">linkedin.com/in/misja-pronk</a><br/>'
            '<a href="https://github.com/misja-pronk" color="#0d6fb8">github.com/misja-pronk</a> · '
            '<a href="https://prorexconsultancy.nl/" color="#0d6fb8">prorexconsultancy.nl</a>'
        ),
        "stats": [
            ("11+", "YEARS IN IT"),
            ("8+", "YEARS DATA & PLATFORMS"),
            ("21", "PROJECTS DELIVERED"),
            ("5", "CERTIFICATIONS"),
        ],
        "clients_label": "SELECTED CLIENTS",
        "clients": "Heijmans · TBI · Vattenfall · Nationale-Nederlanden · ABN AMRO · Stedin · Van Gogh Museum · Menzis",
        "footer_left": "MISJA PRONK",
        "footer_right": "MEASURE TWICE · BUILD ONCE — SHEET {page} OF {total}",
        "profile_h": "Profile",
        "expertise_h": "Core expertise",
        "experience_h": "Experience",
        "oss_h": "Open source",
        "oss": (
            "<b>isolinear</b> — keyboard-driven terminal UI for managing Databricks secrets "
            "(Python, Textual, MIT) · github.com/misja-pronk/isolinear"
        ),
        "certs_h": "Certifications",
        "certs": [
            "MCSA: Data Engineering with Azure — Microsoft",
            "MCSE: Data Management and Analytics — Microsoft",
            "dbt Fundamentals — dbt Labs",
            "Databricks Lakehouse Fundamentals — Databricks",
            "dlt Fundamentals — dltHub",
        ],
        "edu_h": "Education",
        "edu": [
            ("BSc Information Technology — The Hague University of Applied Sciences", "2012 – 2017"),
            ("MBO 4 Application Development — ROC ID College", "2010 – 2012"),
        ],
        "skills_h": "Skills",
        "footer": "Full interactive portfolio: prorexconsultancy.nl (EN) · prorexconsultancy.nl/nl (NL)",
        "job_meta": {
            "prorex": ("ProRex Consultancy — Owner · Data & Platform Engineering Consultant", "Mar 2022 – present"),
            "heijmans": ("Heijmans — Platform Engineer / Data Engineer (via ProRex)", "Dec 2025 – present"),
            "tbi": ("TBI — Lead Data & Platform Engineer (via ProRex)", "2022 – 2025"),
            "vattenfall": ("Vattenfall — Data Engineer / Solution Architect (via ProRex)", "2022 · 6 months"),
            "gdd": ("GoDataDriven — Data & Analytics Consultant", "Sep 2020 – Feb 2022"),
            "macaw": ("Macaw — Data & Analytics Consultant", "Sep 2019 – Aug 2020"),
            "motion10": ("Motion10 — Data & Analytics Consultant", "Jan 2018 – Aug 2019"),
            "vixion": ("Vixion — Full Stack Developer", "2017"),
            "ogd": ("OGD — IT Support Specialist", "2015 – 2016"),
        },
        "vixion_bullet": "SSO-as-a-Service product: API, database and application (C#, ASP.NET Core, IdentityServer).",
    },
    "nl": {
        "subtitle": "Eigenaar, ProRex Consultancy · Friesland, Nederland",
        "contact": (
            '<a href="mailto:misja@prorexconsultancy.nl" color="#0d6fb8">misja@prorexconsultancy.nl</a> · '
            '<a href="https://www.linkedin.com/in/misja-pronk" color="#0d6fb8">linkedin.com/in/misja-pronk</a><br/>'
            '<a href="https://github.com/misja-pronk" color="#0d6fb8">github.com/misja-pronk</a> · '
            '<a href="https://prorexconsultancy.nl/nl/" color="#0d6fb8">prorexconsultancy.nl/nl</a>'
        ),
        "stats": [
            ("11+", "JAAR IN IT"),
            ("8+", "JAAR DATA & PLATFORMS"),
            ("21", "PROJECTEN OPGELEVERD"),
            ("5", "CERTIFICERINGEN"),
        ],
        "clients_label": "SELECTIE VAN KLANTEN",
        "clients": "Heijmans · TBI · Vattenfall · Nationale-Nederlanden · ABN AMRO · Stedin · Van Gogh Museum · Menzis",
        "footer_left": "MISJA PRONK",
        "footer_right": "MEET TWEE KEER · BOUW ÉÉN KEER — BLAD {page} VAN {total}",
        "profile_h": "Profiel",
        "expertise_h": "Kernexpertise",
        "experience_h": "Werkervaring",
        "oss_h": "Open source",
        "oss": (
            "<b>isolinear</b> — toetsenbordgedreven terminal-UI voor het beheren van Databricks-secrets "
            "(Python, Textual, MIT) · github.com/misja-pronk/isolinear"
        ),
        "certs_h": "Certificeringen",
        "certs": [
            "MCSA: Data Engineering with Azure — Microsoft",
            "MCSE: Data Management and Analytics — Microsoft",
            "dbt Fundamentals — dbt Labs",
            "Databricks Lakehouse Fundamentals — Databricks",
            "dlt Fundamentals — dltHub",
        ],
        "edu_h": "Opleiding",
        "edu": [
            ("BSc Informatica (HBO) — De Haagse Hogeschool", "2012 – 2017"),
            ("MBO 4 Applicatieontwikkelaar — ROC ID College", "2010 – 2012"),
        ],
        "skills_h": "Vaardigheden",
        "footer": "Volledig interactief portfolio: prorexconsultancy.nl/nl (NL) · prorexconsultancy.nl (EN)",
        "job_meta": {
            "prorex": ("ProRex Consultancy — Eigenaar · Data & Platform Engineering Consultant", "mrt 2022 – heden"),
            "heijmans": ("Heijmans — Platform Engineer / Data Engineer (via ProRex)", "dec 2025 – heden"),
            "tbi": ("TBI — Lead Data & Platform Engineer (via ProRex)", "2022 – 2025"),
            "vattenfall": ("Vattenfall — Data Engineer / Solution Architect (via ProRex)", "2022 · 6 maanden"),
            "gdd": ("GoDataDriven — Data & Analytics Consultant", "sep 2020 – feb 2022"),
            "macaw": ("Macaw — Data & Analytics Consultant", "sep 2019 – aug 2020"),
            "motion10": ("Motion10 — Data & Analytics Consultant", "jan 2018 – aug 2019"),
            "vixion": ("Vixion — Fullstack-developer", "2017"),
            "ogd": ("OGD — IT-supportspecialist", "2015 – 2016"),
        },
        "vixion_bullet": "SSO-as-a-Service-product: API, database en applicatie (C#, ASP.NET Core, IdentityServer).",
    },
}

SKILLS = {
    "en": {
        "databricks": ("Databricks & data", "Spark, Delta Lake, Unity Catalog, Asset Bundles, dbt, dlt, SQL Server, PostgreSQL, Neo4j, Great Expectations"),
        "platform": ("Platform & cloud", "Azure (25+ services in production), Terraform, Terragrunt, Kubernetes, Docker, GitHub Actions, Azure DevOps"),
        "programming": ("Programming", "Python, SQL, C#, PowerShell, Cypher"),
        "tooling": ("Tooling", "uv, mise, ruff, pytest, Databricks CLI, kubectl, Git"),
        "methods": ("Methods", "Data mesh, DataOps, metadata-driven design, dimensional modeling, Scrum"),
        "languages": ("Languages", "Dutch (native), English (fluent), Spanish (conversational)"),
    },
    "nl": {
        "databricks": ("Databricks & data", "Spark, Delta Lake, Unity Catalog, Asset Bundles, dbt, dlt, SQL Server, PostgreSQL, Neo4j, Great Expectations"),
        "platform": ("Platform & cloud", "Azure (25+ services in productie), Terraform, Terragrunt, Kubernetes, Docker, GitHub Actions, Azure DevOps"),
        "programming": ("Programmeren", "Python, SQL, C#, PowerShell, Cypher"),
        "tooling": ("Tooling", "uv, mise, ruff, pytest, Databricks CLI, kubectl, Git"),
        "methods": ("Methoden", "Data mesh, DataOps, metadata-gedreven ontwerp, dimensionaal modelleren, Scrum"),
        "languages": ("Talen", "Nederlands (moedertaal), Engels (vloeiend), Spaans (conversatie)"),
    },
}

SKILL_ORDER_DEFAULT = ["databricks", "platform", "programming", "tooling", "methods", "languages"]

# ---------------------------------------------------------------- variants
# Each variant: file (EN name; NL gets _nl suffix), title, profile,
# expertise, per-job bullets, skill order.

VARIANTS = {
    "general": {
        "file": "mp_resume",
        "no": "CV-001",
        "skill_order": SKILL_ORDER_DEFAULT,
        "en": {
            "title": "Data & Platform Engineering Consultant",
            "profile": (
                "Freelance Data & Platform Engineering consultant with 11+ years in IT, of which 8+ years designing and "
                "building data platforms. Deep, day-to-day Databricks expertise, metadata-driven architectures and the full "
                "platform-engineering stack — Terraform, Terragrunt, GitHub and CI/CD. Open-source-first, and as much a "
                "coach as an engineer: teams I leave behind own their platform. Motto: measure twice, build once."
            ),
            "expertise": [
                "<b>Databricks platform</b> — Spark, Delta Lake, Unity Catalog, Asset Bundles, workspace architecture, cost control, agentic AI",
                "<b>Platform engineering &amp; DevOps</b> — Terraform, Terragrunt, GitHub Actions, Azure DevOps, Kubernetes, CI/CD",
                "<b>Metadata-driven data platforms</b> — hundreds of sources integrated through configuration, not code duplication",
                "<b>Enablement</b> — training and coaching teams in dbt, Git, DataOps and cloud-engineering ways of working",
            ],
            "bullets": {
                "heijmans": [
                    "Building the Heijmans data platform: data-mesh architecture on Azure and Databricks, all infrastructure as code in Terraform and Terragrunt.",
                    "Standardized CI/CD on Databricks Asset Bundles with reusable Python packages serving data engineering and data science.",
                    "Data pipelines integrating SAP, Autodesk and M-Files; agentic-AI use cases with a team of five data scientists.",
                    "Upskilling the cloud team from Bicep to Terragrunt; sparring partner for the solution architect.",
                ],
                "tbi": [
                    "Led the build of TBI's data-mesh platform: Terraform and Terragrunt IaC, all standardized CI/CD pipelines in GitHub.",
                    "Coached the BI team (5–8 professionals) in dbt, TMDL, Power BI deployments from code, Git and DataOps — turning a classic BI team into an engineering-minded one.",
                    "Supported the integration team's modernization from Azure App Services to Kubernetes; designed extraction patterns for 4PS (construction ERP).",
                ],
                "vattenfall": [
                    "Migrated a struggling Azure data warehouse to a Databricks + dbt lakehouse: architecture, technology stack, infrastructure, CI/CD and team training.",
                ],
                "gdd": [
                    "Data solutions for Nationale-Nederlanden, Stedin, Witteveen+Bos, Intergamma and VeiligheidNL; built the infrastructure of a reusable data platform sold to customers.",
                ],
                "macaw": [
                    "Data solutions for SamenGezond (Menzis), Sustainovate and Henkel; technology-committee member: platform revision, best practices, mentoring juniors.",
                ],
                "motion10": [
                    "Data solutions for eight clients, incl. Van Gogh Museum, ABN AMRO Pensioenfonds, TBI, Samskip and De Goudse; developed training materials and a reusable data platform.",
                ],
            },
        },
        "nl": {
            "title": "Data & Platform Engineering Consultant",
            "profile": (
                "Freelance Data & Platform Engineering consultant met 11+ jaar in de IT, waarvan 8+ jaar in het ontwerpen en "
                "bouwen van dataplatformen. Diepgaande, dagelijkse Databricks-expertise, metadata-gedreven architecturen en de "
                "volledige platform-engineering-stack — Terraform, Terragrunt, GitHub en CI/CD. Open source eerst, en evenzeer "
                "coach als engineer: teams die ik achterlaat, beheren hun eigen platform. Motto: meet twee keer, bouw één keer."
            ),
            "expertise": [
                "<b>Databricks-platform</b> — Spark, Delta Lake, Unity Catalog, Asset Bundles, workspace-architectuur, kostenbeheersing, agentic AI",
                "<b>Platform engineering &amp; DevOps</b> — Terraform, Terragrunt, GitHub Actions, Azure DevOps, Kubernetes, CI/CD",
                "<b>Metadata-gedreven dataplatformen</b> — honderden bronnen geïntegreerd via configuratie in plaats van codeduplicatie",
                "<b>Enablement</b> — teams trainen en coachen in dbt, Git, DataOps en cloud-engineering-werkwijzen",
            ],
            "bullets": {
                "heijmans": [
                    "Bouw van het Heijmans-dataplatform: data-mesh-architectuur op Azure en Databricks, alle infrastructuur als code in Terraform en Terragrunt.",
                    "Gestandaardiseerde CI/CD op Databricks Asset Bundles met herbruikbare Python-packages voor data engineering én data science.",
                    "Datapijplijnen voor SAP, Autodesk en M-Files; agentic-AI-toepassingen met een team van vijf data scientists.",
                    "Cloudteam bijgeschoold van Bicep naar Terragrunt; sparringpartner voor de solution architect.",
                ],
                "tbi": [
                    "Leiding over de bouw van het data-mesh-platform van TBI: Terraform- en Terragrunt-IaC, alle gestandaardiseerde CI/CD-pijplijnen in GitHub.",
                    "BI-team (5–8 professionals) gecoacht in dbt, TMDL, Power BI-deployments vanuit code, Git en DataOps — van klassiek BI-team naar engineeringmentaliteit.",
                    "Integratieteam ondersteund bij modernisering van Azure App Services naar Kubernetes; extractiepatronen ontworpen voor 4PS (bouw-ERP).",
                ],
                "vattenfall": [
                    "Een vastgelopen Azure-datawarehouse gemigreerd naar een Databricks + dbt-lakehouse: architectuur, technologiestack, infrastructuur, CI/CD en teamtraining.",
                ],
                "gdd": [
                    "Dataoplossingen voor Nationale-Nederlanden, Stedin, Witteveen+Bos, Intergamma en VeiligheidNL; infrastructuur gebouwd van een herbruikbaar dataplatform dat aan klanten wordt verkocht.",
                ],
                "macaw": [
                    "Dataoplossingen voor SamenGezond (Menzis), Sustainovate en Henkel; lid technologiecommissie: platformherziening, best practices, begeleiding van juniors.",
                ],
                "motion10": [
                    "Dataoplossingen voor acht klanten, o.a. Van Gogh Museum, ABN AMRO Pensioenfonds, TBI, Samskip en De Goudse; trainingsmateriaal en een herbruikbaar dataplatform ontwikkeld.",
                ],
            },
        },
    },
    "architect": {
        "file": "mp_resume_architect",
        "no": "CV-002",
        "skill_order": ["methods", "databricks", "platform", "programming", "tooling", "languages"],
        "en": {
            "title": "Data & Solution Architect",
            "profile": (
                "Data & solution architect with 11+ years in IT and 8+ years designing data platforms — data mesh, lakehouse "
                "and metadata-driven architectures on Azure and Databricks. I design target architectures that survive contact "
                "with reality, because I also build and run them: infrastructure as code, CI/CD and governance included. "
                "Comfortable from whiteboard to production, and a sparring partner for enterprise architects and teams alike."
            ),
            "expertise": [
                "<b>Architecture</b> — data mesh, lakehouse, metadata-driven platforms, target architectures and roadmaps",
                "<b>Databricks platform</b> — workspace architecture, Unity Catalog governance, Asset Bundles, cost control",
                "<b>Cloud foundations</b> — Azure, Terraform/Terragrunt structures, CI/CD, Kubernetes",
                "<b>Advisory &amp; enablement</b> — assessments, cloud roadmaps, coaching architects and engineering teams",
            ],
            "bullets": {
                "heijmans": [
                    "Co-designing the Heijmans data platform: data-mesh target architecture on Azure and Databricks; sparring partner for the solution architect.",
                    "Architecture made executable: all infrastructure as code (Terraform/Terragrunt) and standardized CI/CD on Databricks Asset Bundles.",
                    "Integration architecture for SAP, Autodesk and M-Files; agentic-AI use cases with the data science team.",
                ],
                "tbi": [
                    "Designed and led the build of TBI's data-mesh platform architecture, serving 17 companies and hundreds of sources (Terraform/Terragrunt, GitHub CI/CD).",
                    "Designed the extraction patterns for 4PS (construction ERP); guided the App Services → Kubernetes modernization.",
                    "Set the standards and coached the BI team into engineering and DataOps ways of working.",
                ],
                "vattenfall": [
                    "Designed the target lakehouse architecture (Databricks + dbt) replacing a struggling Azure data warehouse: stack selection, infrastructure, CI/CD and team training.",
                ],
                "gdd": [
                    "Platform assessment for Stedin; cloud roadmap for Intergamma (AWS/Azure/GCP scenarios); platform rebuild for Nationale-Nederlanden; architecture for a reusable, commercially sold data platform.",
                ],
                "macaw": [
                    "Solution architecture for Sustainovate's privacy-compliant data marketplace; data platforms for SamenGezond (Menzis) and Henkel; technology-committee member.",
                ],
                "motion10": [
                    "Solution architect for ABN AMRO Pensioenfonds (urgent Brexit cloud migration), De Goudse (integrated target architecture), Croonwolter&amp;dros (modern DWH design) and Van Gogh Museum; hands-on delivery for Samskip, Het Nieuwe Instituut, TBI and Marlink.",
                ],
            },
        },
        "nl": {
            "title": "Data & Solution Architect",
            "profile": (
                "Data & solution architect met 11+ jaar in de IT en 8+ jaar in het ontwerpen van dataplatformen — data-mesh-, "
                "lakehouse- en metadata-gedreven architecturen op Azure en Databricks. Ik ontwerp doelarchitecturen die het "
                "contact met de werkelijkheid overleven, omdat ik ze ook zelf bouw en beheer: inclusief infrastructure as code, "
                "CI/CD en governance. Thuis van whiteboard tot productie, en sparringpartner voor enterprise-architecten en teams."
            ),
            "expertise": [
                "<b>Architectuur</b> — data mesh, lakehouse, metadata-gedreven platformen, doelarchitecturen en roadmaps",
                "<b>Databricks-platform</b> — workspace-architectuur, Unity Catalog-governance, Asset Bundles, kostenbeheersing",
                "<b>Cloudfundament</b> — Azure, Terraform/Terragrunt-structuren, CI/CD, Kubernetes",
                "<b>Advies &amp; enablement</b> — assessments, cloudroadmaps, coaching van architecten en engineeringteams",
            ],
            "bullets": {
                "heijmans": [
                    "Mede-ontwerper van het Heijmans-dataplatform: data-mesh-doelarchitectuur op Azure en Databricks; sparringpartner voor de solution architect.",
                    "Architectuur die uitvoerbaar is: alle infrastructuur als code (Terraform/Terragrunt) en gestandaardiseerde CI/CD op Databricks Asset Bundles.",
                    "Integratiearchitectuur voor SAP, Autodesk en M-Files; agentic-AI-toepassingen met het datascienceteam.",
                ],
                "tbi": [
                    "Architectuur ontworpen en bouw geleid van het data-mesh-platform van TBI, voor 17 bedrijven en honderden bronnen (Terraform/Terragrunt, GitHub-CI/CD).",
                    "Extractiepatronen ontworpen voor 4PS (bouw-ERP); modernisering van App Services naar Kubernetes begeleid.",
                    "Standaarden neergezet en het BI-team gecoacht naar engineering- en DataOps-werkwijzen.",
                ],
                "vattenfall": [
                    "Doelarchitectuur ontworpen voor het lakehouse (Databricks + dbt) ter vervanging van een vastgelopen Azure-datawarehouse: stackkeuze, infrastructuur, CI/CD en teamtraining.",
                ],
                "gdd": [
                    "Platformassessment voor Stedin; cloudroadmap voor Intergamma (AWS/Azure/GCP-scenario's); platformherbouw voor Nationale-Nederlanden; architectuur van een herbruikbaar, commercieel verkocht dataplatform.",
                ],
                "macaw": [
                    "Solution-architectuur voor de privacyconforme datamarktplaats van Sustainovate; dataplatformen voor SamenGezond (Menzis) en Henkel; lid technologiecommissie.",
                ],
                "motion10": [
                    "Solution architect voor ABN AMRO Pensioenfonds (urgente brexit-cloudmigratie), De Goudse (geïntegreerde doelarchitectuur), Croonwolter&amp;dros (modern DWH-ontwerp) en het Van Gogh Museum; hands-on delivery voor Samskip, Het Nieuwe Instituut, TBI en Marlink.",
                ],
            },
        },
    },
    "data_engineer": {
        "file": "mp_resume_data_engineer",
        "no": "CV-003",
        "skill_order": SKILL_ORDER_DEFAULT,
        "en": {
            "title": "Senior Data Engineer",
            "profile": (
                "Senior data engineer with 8+ years building data platforms and pipelines — Databricks-deep (Spark, Delta Lake, "
                "Unity Catalog, Asset Bundles), dbt-fluent and metadata-driven by conviction. I integrate the hard sources — "
                "ERPs, legacy systems, APIs — and leave behind tested, automated pipelines and teams that can run them."
            ),
            "expertise": [
                "<b>Databricks engineering</b> — Spark, Delta Lake, Unity Catalog, Workflows, Asset Bundles, agentic AI",
                "<b>Pipelines &amp; modeling</b> — dbt, dlt, metadata-driven ETL, dimensional modeling, Great Expectations",
                "<b>Source integration</b> — SAP, 4PS, Autodesk, M-Files, AS400/DB2, REST APIs",
                "<b>CI/CD for data</b> — GitHub Actions, Azure DevOps, Databricks Asset Bundles, tested deployments",
            ],
            "bullets": {
                "heijmans": [
                    "Data pipelines integrating SAP, Autodesk and M-Files into a Databricks data mesh on Azure.",
                    "Standardized CI/CD on Databricks Asset Bundles with reusable Python packages for data engineering and data science.",
                    "Agentic-AI use cases with a team of five data scientists — upskilling the team and delivering to production.",
                ],
                "tbi": [
                    "Built the pipelines of TBI's data-mesh platform; designed the extraction patterns for 4PS (construction ERP).",
                    "Introduced dbt to the BI team (5–8 professionals): standards, practices, TMDL and Power BI deployments from code.",
                    "All CI/CD standardized in GitHub; Git and DataOps ways of working established.",
                ],
                "vattenfall": [
                    "Migrated a struggling Azure data warehouse to a Databricks + dbt lakehouse: source extraction in PySpark, dbt models, CI/CD and team training.",
                ],
                "gdd": [
                    "Rebuilt Nationale-Nederlanden's platform ETL with automated data quality (Great Expectations); GDPR-compliant ML API for VeiligheidNL; Databricks performance rework for Clay.",
                ],
                "macaw": [
                    "Real-time integration platform for SamenGezond (Dacadoo, Mailchimp, Typeform APIs); marketing-API platform for Henkel, leading a team of 7 developers.",
                ],
                "motion10": [
                    "ETL from AS400/DB2, AFAS and Exact to Azure data marts for Samskip, Het Nieuwe Instituut and Van Gogh Museum; metadata-driven platform for TBI integrating hundreds of sources.",
                ],
            },
        },
        "nl": {
            "title": "Senior Data Engineer",
            "profile": (
                "Senior data engineer met 8+ jaar ervaring in het bouwen van dataplatformen en -pijplijnen — Databricks-diep "
                "(Spark, Delta Lake, Unity Catalog, Asset Bundles), vloeiend in dbt en metadata-gedreven uit overtuiging. Ik "
                "integreer de lastige bronnen — ERP's, legacysystemen, API's — en laat geteste, geautomatiseerde pijplijnen "
                "achter, plus teams die ze zelf kunnen beheren."
            ),
            "expertise": [
                "<b>Databricks-engineering</b> — Spark, Delta Lake, Unity Catalog, Workflows, Asset Bundles, agentic AI",
                "<b>Pijplijnen &amp; modellering</b> — dbt, dlt, metadata-gedreven ETL, dimensionaal modelleren, Great Expectations",
                "<b>Bronintegratie</b> — SAP, 4PS, Autodesk, M-Files, AS400/DB2, REST-API's",
                "<b>CI/CD voor data</b> — GitHub Actions, Azure DevOps, Databricks Asset Bundles, geteste deployments",
            ],
            "bullets": {
                "heijmans": [
                    "Datapijplijnen die SAP, Autodesk en M-Files integreren in een Databricks-data-mesh op Azure.",
                    "Gestandaardiseerde CI/CD op Databricks Asset Bundles met herbruikbare Python-packages voor data engineering én data science.",
                    "Agentic-AI-toepassingen met een team van vijf data scientists — team bijgeschoold en use cases naar productie gebracht.",
                ],
                "tbi": [
                    "Pijplijnen gebouwd van het data-mesh-platform van TBI; extractiepatronen ontworpen voor 4PS (bouw-ERP).",
                    "dbt geïntroduceerd bij het BI-team (5–8 professionals): standaarden, werkwijzen, TMDL en Power BI-deployments vanuit code.",
                    "Alle CI/CD gestandaardiseerd in GitHub; Git- en DataOps-werkwijzen neergezet.",
                ],
                "vattenfall": [
                    "Een vastgelopen Azure-datawarehouse gemigreerd naar een Databricks + dbt-lakehouse: bronextractie in PySpark, dbt-modellen, CI/CD en teamtraining.",
                ],
                "gdd": [
                    "ETL van het Nationale-Nederlanden-platform herbouwd met geautomatiseerde datakwaliteit (Great Expectations); AVG-conforme ML-API voor VeiligheidNL; Databricks-performanceherbouw voor Clay.",
                ],
                "macaw": [
                    "Realtime-integratieplatform voor SamenGezond (Dacadoo-, Mailchimp-, Typeform-API's); marketing-API-platform voor Henkel, met aansturing van 7 ontwikkelaars.",
                ],
                "motion10": [
                    "ETL van AS400/DB2, AFAS en Exact naar Azure-datamarts voor Samskip, Het Nieuwe Instituut en het Van Gogh Museum; metadata-gedreven platform voor TBI met honderden bronnen.",
                ],
            },
        },
    },
    "platform_engineer": {
        "file": "mp_resume_platform_engineer",
        "no": "CV-004",
        "skill_order": ["platform", "tooling", "databricks", "programming", "methods", "languages"],
        "en": {
            "title": "Platform / Cloud Engineer",
            "profile": (
                "Platform engineer with 11+ years in IT, specialized in making data teams fast: infrastructure as code "
                "(Terraform, Terragrunt), GitHub CI/CD, Kubernetes and DevOps ways of working on Azure. I build golden paths — "
                "standardized pipelines, reusable modules, self-service platforms — and coach teams until they own them."
            ),
            "expertise": [
                "<b>Infrastructure as code</b> — Terraform, Terragrunt, Bicep/ARM, reusable module design",
                "<b>CI/CD &amp; DevOps</b> — GitHub Actions, Azure DevOps, Databricks Asset Bundles, release standardization",
                "<b>Containers &amp; runtime</b> — Kubernetes, Docker, Azure (25+ services), networking &amp; Private Link",
                "<b>Enablement</b> — team migrations (Bicep → Terragrunt), Git/DataOps coaching, developer tooling (uv, mise)",
            ],
            "bullets": {
                "heijmans": [
                    "Building the Heijmans platform infrastructure: Terraform/Terragrunt IaC for Azure and Databricks (data-mesh architecture).",
                    "Standardized CI/CD: Databricks Asset Bundles plus reusable Python packages as the golden path for data engineering and data science.",
                    "Migrating the cloud team from Bicep to Terragrunt — standards, module design and coaching.",
                ],
                "tbi": [
                    "Lead platform engineer: Terraform/Terragrunt IaC and all standardized GitHub CI/CD for TBI's data-mesh platform (17 companies).",
                    "Supported the integration team's modernization from Azure App Services to Kubernetes.",
                    "Established Git and DataOps ways of working across BI and engineering teams.",
                ],
                "vattenfall": [
                    "Set up the infrastructure and CI/CD (Bicep/ARM, Azure DevOps) for a Databricks + dbt lakehouse migration.",
                ],
                "gdd": [
                    "Rebuilt Nationale-Nederlanden's platform infrastructure in Terraform with automated infrastructure testing (container instances, networking, Key Vault, Purview); infra of a reusable data platform sold to customers.",
                ],
                "macaw": [
                    "Azure platform design and delivery for SamenGezond (Menzis) and Henkel; technology-committee member: platform revision and best practices.",
                ],
                "motion10": [
                    "Provisioned and automated Azure environments and CI/CD across eight clients; built a reusable, metadata-driven platform and trained client teams.",
                ],
            },
        },
        "nl": {
            "title": "Platform / Cloud Engineer",
            "profile": (
                "Platform engineer met 11+ jaar in de IT, gespecialiseerd in datateams snel maken: infrastructure as code "
                "(Terraform, Terragrunt), GitHub-CI/CD, Kubernetes en DevOps-werkwijzen op Azure. Ik bouw golden paths — "
                "gestandaardiseerde pijplijnen, herbruikbare modules, selfserviceplatformen — en coach teams tot ze die zelf beheren."
            ),
            "expertise": [
                "<b>Infrastructure as code</b> — Terraform, Terragrunt, Bicep/ARM, herbruikbaar moduleontwerp",
                "<b>CI/CD &amp; DevOps</b> — GitHub Actions, Azure DevOps, Databricks Asset Bundles, releasestandaardisatie",
                "<b>Containers &amp; runtime</b> — Kubernetes, Docker, Azure (25+ services), networking &amp; Private Link",
                "<b>Enablement</b> — teammigraties (Bicep → Terragrunt), Git/DataOps-coaching, developer tooling (uv, mise)",
            ],
            "bullets": {
                "heijmans": [
                    "Bouw van de Heijmans-platforminfrastructuur: Terraform/Terragrunt-IaC voor Azure en Databricks (data-mesh-architectuur).",
                    "Gestandaardiseerde CI/CD: Databricks Asset Bundles plus herbruikbare Python-packages als golden path voor data engineering en data science.",
                    "Cloudteam migreren van Bicep naar Terragrunt — standaarden, moduleontwerp en coaching.",
                ],
                "tbi": [
                    "Lead platform engineer: Terraform/Terragrunt-IaC en alle gestandaardiseerde GitHub-CI/CD voor het data-mesh-platform van TBI (17 bedrijven).",
                    "Integratieteam ondersteund bij de modernisering van Azure App Services naar Kubernetes.",
                    "Git- en DataOps-werkwijzen neergezet bij BI- en engineeringteams.",
                ],
                "vattenfall": [
                    "Infrastructuur en CI/CD opgezet (Bicep/ARM, Azure DevOps) voor een Databricks + dbt-lakehouse-migratie.",
                ],
                "gdd": [
                    "Platforminfrastructuur van Nationale-Nederlanden herbouwd in Terraform met geautomatiseerd infrastructuurtesten (container instances, networking, Key Vault, Purview); infrastructuur van een herbruikbaar dataplatform dat aan klanten wordt verkocht.",
                ],
                "macaw": [
                    "Azure-platformontwerp en -oplevering voor SamenGezond (Menzis) en Henkel; lid technologiecommissie: platformherziening en best practices.",
                ],
                "motion10": [
                    "Azure-omgevingen en CI/CD ingericht en geautomatiseerd bij acht klanten; herbruikbaar, metadata-gedreven platform gebouwd en klantteams getraind.",
                ],
            },
        },
    },
}

JOB_ORDER = ["prorex", "heijmans", "tbi", "vattenfall", "gdd", "macaw", "motion10", "vixion", "ogd"]

# ---------------------------------------------------------------- styles

S = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, leading=25, textColor=INK),
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=10.5, leading=14, textColor=ACCENT),
    "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=9, leading=12, textColor=DIM),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8.2, leading=11, textColor=DIM),
    "h": ParagraphStyle(
        "h", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=ACCENT,
        spaceBefore=10, spaceAfter=3,
    ),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.2, leading=13, textColor=INK),
    "bullet": ParagraphStyle(
        "bullet", fontName="Helvetica", fontSize=9, leading=12.4, textColor=INK,
        leftIndent=9, bulletIndent=0, spaceAfter=1.5,
    ),
    "job": ParagraphStyle("job", fontName="Helvetica-Bold", fontSize=9.4, leading=12.5, textColor=INK),
    "when": ParagraphStyle("when", fontName="Helvetica", fontSize=8.4, leading=12.5, textColor=DIM, alignment=TA_RIGHT),
    "footer": ParagraphStyle(
        "footer", fontName="Helvetica-Oblique", fontSize=8, leading=11, textColor=DIM, spaceBefore=12,
    ),
}


S["stat_val"] = ParagraphStyle(
    "stat_val", fontName="Helvetica-Bold", fontSize=13, leading=15, textColor=ACCENT, alignment=TA_CENTER,
)
S["stat_label"] = ParagraphStyle(
    "stat_label", fontName="Helvetica", fontSize=5.6, leading=7.5, textColor=DIM, alignment=TA_CENTER,
)
S["clients"] = ParagraphStyle(
    "clients", fontName="Helvetica-Bold", fontSize=7.6, leading=11, textColor=DIM, spaceBefore=5,
)
S["docno"] = ParagraphStyle(
    "docno", fontName="Courier-Bold", fontSize=7.2, leading=10, textColor=DIM, alignment=TA_RIGHT,
)


def rule() -> HRFlowable:
    return HRFlowable(width="100%", thickness=0.7, color=LINE, spaceBefore=1, spaceAfter=5)


def heading(number: int, text: str) -> list:
    return [
        Paragraph(f'<font color="#d43d3d">{number:02d}</font> — {text.upper()}', S["h"]),
        rule(),
    ]


def stats_strip(stats: list[tuple[str, str]]) -> Table:
    cells = [
        [Paragraph(value, S["stat_val"]), Paragraph(label, S["stat_label"])]
        for value, label in stats
    ]
    t = Table([cells], colWidths=[44.5 * mm] * len(cells))
    t.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.7, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ])
    )
    return t


class SheetCanvas(pdfcanvas.Canvas):
    """Two-pass canvas that draws a title-block footer with SHEET X OF Y."""

    footer_left = ""
    footer_right = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_states = []

    def showPage(self):
        self._saved_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved_states)
        for i, state in enumerate(self._saved_states, start=1):
            self.__dict__.update(state)
            self._draw_footer(i, total)
            super().showPage()
        super().save()

    def _draw_footer(self, page: int, total: int):
        self.saveState()
        self.setStrokeColor(LINE)
        self.setLineWidth(0.7)
        self.line(16 * mm, 9.5 * mm, A4[0] - 16 * mm, 9.5 * mm)
        self.setFont("Courier", 6.6)
        self.setFillColor(DIM)
        self.drawString(16 * mm, 6 * mm, self.footer_left)
        self.drawRightString(
            A4[0] - 16 * mm, 6 * mm, self.footer_right.format(page=page, total=total)
        )
        self.restoreState()


def job_row(who: str, when: str) -> Table:
    t = Table(
        [[Paragraph(who, S["job"]), Paragraph(when, S["when"])]],
        colWidths=[132 * mm, 46 * mm],
    )
    t.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ])
    )
    return t


def build(variant_key: str, locale: str) -> None:
    base = BASE[locale]
    variant = VARIANTS[variant_key]
    v = variant[locale]

    suffix = "" if locale == "en" else "_nl"
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{variant['file']}{suffix}.pdf"

    docno = f"MP-{variant['no']}"
    keywords = [v["title"], "Databricks", "Terraform", "Terragrunt", "dbt", "Azure", "Data Mesh", "CI/CD", "Kubernetes"]

    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=15 * mm,
        title=f"Misja Pronk — {v['title']}",
        author="Misja Pronk",
        subject=v["title"],
        keywords=", ".join(keywords),
    )

    story = []

    header = Table(
        [[
            [Paragraph("MISJA PRONK", S["name"]), Spacer(1, 2), Paragraph(v["title"], S["title"])],
            [
                Paragraph(f"DOC NO. {docno} · REV 2026", S["docno"]),
                Spacer(1, 3),
                Paragraph(base["subtitle"], S["subtitle"]),
                Spacer(1, 3),
                Paragraph(base["contact"], S["contact"]),
            ],
        ]],
        colWidths=[88 * mm, 90 * mm],
    )
    header.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ])
    )
    story.append(header)
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.4, color=INK, spaceAfter=7))

    story.append(stats_strip(base["stats"]))
    story.append(Spacer(1, 2))

    n = iter(range(1, 10))
    story += heading(next(n), base["profile_h"])
    story.append(Paragraph(v["profile"], S["body"]))
    story.append(Paragraph(f'<font color="#7a8ea3">{base["clients_label"]}:</font> {base["clients"]}', S["clients"]))

    story += heading(next(n), base["expertise_h"])
    for item in v["expertise"]:
        story.append(Paragraph(item, S["bullet"], bulletText="—"))

    story += heading(next(n), base["experience_h"])
    for key in JOB_ORDER:
        who, when = base["job_meta"][key]
        if key == "vixion":
            bullets = [base["vixion_bullet"]]
        else:
            bullets = v["bullets"].get(key, [])
        entry = [job_row(who, when)]
        for b in bullets:
            entry.append(Paragraph(b, S["bullet"], bulletText="•"))
        story.append(KeepTogether(entry))

    story += heading(next(n), base["oss_h"])
    story.append(Paragraph(base["oss"], S["body"]))

    story += heading(next(n), base["certs_h"])
    for cert in base["certs"]:
        story.append(Paragraph(cert, S["bullet"], bulletText="•"))

    story += heading(next(n), base["edu_h"])
    for degree, when in base["edu"]:
        story.append(job_row(degree, when))

    story += heading(next(n), base["skills_h"])
    for skill_key in variant["skill_order"]:
        label, value = SKILLS[locale][skill_key]
        story.append(Paragraph(f"<b>{label}:</b> {value}", S["bullet"]))

    story.append(Paragraph(base["footer"], S["footer"]))

    canvas_cls = type(
        "FooterCanvas",
        (SheetCanvas,),
        {"footer_left": f"{base['footer_left']} — {v['title'].upper()}", "footer_right": base["footer_right"]},
    )
    doc.build(story, canvasmaker=canvas_cls)
    print(f"wrote {path}")


if __name__ == "__main__":
    for variant_key in VARIANTS:
        for locale in ("en", "nl"):
            build(variant_key, locale)
