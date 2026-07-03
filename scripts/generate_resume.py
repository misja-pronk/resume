# /// script
# requires-python = ">=3.11"
# dependencies = ["reportlab>=4.0"]
# ///
"""Generate the resume PDFs (EN + NL) into public/docs/.

Run with:  uv run scripts/generate_resume.py
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
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

# ---------------------------------------------------------------- content

CONTENT = {
    "en": {
        "file": "mp_resume.pdf",
        "title": "Data & Platform Engineering Consultant",
        "subtitle": "Owner, ProRex Consultancy · Friesland, The Netherlands",
        "contact": "misja@prorexconsultancy.nl · linkedin.com/in/misja-pronk · github.com/misja-pronk · misja-pronk.github.io/resume",
        "profile_h": "Profile",
        "profile": (
            "Freelance Data & Platform Engineering consultant with 11+ years in IT, of which 8+ years designing and "
            "building data platforms. Deep, day-to-day Databricks expertise, metadata-driven architectures and the full "
            "platform-engineering stack — Terraform, Terragrunt, GitHub and CI/CD. Open-source-first, and as much a "
            "coach as an engineer: teams I leave behind own their platform. Motto: measure twice, build once."
        ),
        "expertise_h": "Core expertise",
        "expertise": [
            "<b>Databricks platform</b> — Spark, Delta Lake, Unity Catalog, Asset Bundles, workspace architecture, cost control, agentic AI",
            "<b>Platform engineering &amp; DevOps</b> — Terraform, Terragrunt, GitHub Actions, Azure DevOps, Kubernetes, CI/CD",
            "<b>Metadata-driven data platforms</b> — hundreds of sources integrated through configuration, not code duplication",
            "<b>Enablement</b> — training and coaching teams in dbt, Git, DataOps and cloud-engineering ways of working",
        ],
        "experience_h": "Experience",
        "jobs": [
            {
                "who": "ProRex Consultancy — Owner · Data & Platform Engineering Consultant",
                "when": "Mar 2022 – present",
                "bullets": [],
            },
            {
                "who": "Heijmans — Platform Engineer / Data Engineer (via ProRex)",
                "when": "Dec 2025 – present",
                "bullets": [
                    "Building the Heijmans data platform: data-mesh architecture on Azure and Databricks, all infrastructure as code in Terraform and Terragrunt.",
                    "Standardized CI/CD on Databricks Asset Bundles with reusable Python packages serving data engineering and data science.",
                    "Data pipelines integrating SAP, Autodesk and M-Files; agentic-AI use cases with a team of five data scientists.",
                    "Upskilling the cloud team from Bicep to Terragrunt; sparring partner for the solution architect.",
                ],
            },
            {
                "who": "TBI — Lead Data & Platform Engineer (via ProRex)",
                "when": "2022 – 2025",
                "bullets": [
                    "Led the build of TBI's data-mesh platform: Terraform and Terragrunt IaC, all standardized CI/CD pipelines in GitHub.",
                    "Coached the BI team (5–8 professionals) in dbt, TMDL, Power BI deployments from code, Git and DataOps — turning a classic BI team into an engineering-minded one.",
                    "Supported the integration team's modernization from Azure App Services to Kubernetes; designed extraction patterns for 4PS (construction ERP).",
                ],
            },
            {
                "who": "Vattenfall — Data Engineer / Solution Architect (via ProRex)",
                "when": "2022 · 6 months",
                "bullets": [
                    "Migrated a struggling Azure data warehouse to a Databricks + dbt lakehouse: architecture, technology stack, infrastructure, CI/CD and team training.",
                ],
            },
            {
                "who": "GoDataDriven — Data & Analytics Consultant",
                "when": "Sep 2020 – Feb 2022",
                "bullets": [
                    "Data solutions for Nationale-Nederlanden, Stedin, Witteveen+Bos, Intergamma and VeiligheidNL; built the infrastructure of a reusable data platform sold to customers.",
                ],
            },
            {
                "who": "Macaw — Data & Analytics Consultant",
                "when": "Sep 2019 – Aug 2020",
                "bullets": [
                    "Data solutions for SamenGezond (Menzis), Sustainovate and Henkel; technology-committee member: platform revision, best practices, mentoring juniors.",
                ],
            },
            {
                "who": "Motion10 — Data & Analytics Consultant",
                "when": "Jan 2018 – Aug 2019",
                "bullets": [
                    "Data solutions for eight clients, incl. Van Gogh Museum, ABN AMRO Pensioenfonds, TBI, Samskip and De Goudse; developed training materials and a reusable data platform.",
                ],
            },
            {
                "who": "Vixion — Full Stack Developer",
                "when": "2017",
                "bullets": ["SSO-as-a-Service product: API, database and application (C#, ASP.NET Core, IdentityServer)."],
            },
            {
                "who": "OGD — IT Support Specialist",
                "when": "2015 – 2016",
                "bullets": [],
            },
        ],
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
        ],
        "edu_h": "Education",
        "edu": [
            ("BSc Information Technology — The Hague University of Applied Sciences", "2012 – 2017"),
            ("MBO 4 Application Development — ROC ID College", "2010 – 2012"),
        ],
        "skills_h": "Skills",
        "skills": [
            ("Databricks & data", "Spark, Delta Lake, Unity Catalog, Asset Bundles, dbt, dlt, SQL Server, PostgreSQL, Neo4j, Great Expectations"),
            ("Platform & cloud", "Azure (25+ services in production), Terraform, Terragrunt, Kubernetes, Docker, GitHub Actions, Azure DevOps"),
            ("Programming", "Python, SQL, C#, PowerShell, Cypher"),
            ("Tooling", "uv, mise, ruff, pytest, Databricks CLI, kubectl, Git"),
            ("Methods", "Data mesh, DataOps, metadata-driven design, dimensional modeling, Scrum"),
            ("Languages", "Dutch (native), English (fluent), Spanish (conversational)"),
        ],
        "footer": "Full interactive portfolio: misja-pronk.github.io/resume (EN) · misja-pronk.github.io/resume/nl/ (NL)",
    },
    "nl": {
        "file": "mp_resume_nl.pdf",
        "title": "Data & Platform Engineering Consultant",
        "subtitle": "Eigenaar, ProRex Consultancy · Friesland, Nederland",
        "contact": "misja@prorexconsultancy.nl · linkedin.com/in/misja-pronk · github.com/misja-pronk · misja-pronk.github.io/resume/nl",
        "profile_h": "Profiel",
        "profile": (
            "Freelance Data & Platform Engineering consultant met 11+ jaar in de IT, waarvan 8+ jaar in het ontwerpen en "
            "bouwen van dataplatformen. Diepgaande, dagelijkse Databricks-expertise, metadata-gedreven architecturen en de "
            "volledige platform-engineering-stack — Terraform, Terragrunt, GitHub en CI/CD. Open source eerst, en evenzeer "
            "coach als engineer: teams die ik achterlaat, beheren hun eigen platform. Motto: meet twee keer, bouw één keer."
        ),
        "expertise_h": "Kernexpertise",
        "expertise": [
            "<b>Databricks-platform</b> — Spark, Delta Lake, Unity Catalog, Asset Bundles, workspace-architectuur, kostenbeheersing, agentic AI",
            "<b>Platform engineering &amp; DevOps</b> — Terraform, Terragrunt, GitHub Actions, Azure DevOps, Kubernetes, CI/CD",
            "<b>Metadata-gedreven dataplatformen</b> — honderden bronnen geïntegreerd via configuratie in plaats van codeduplicatie",
            "<b>Enablement</b> — teams trainen en coachen in dbt, Git, DataOps en cloud-engineering-werkwijzen",
        ],
        "experience_h": "Werkervaring",
        "jobs": [
            {
                "who": "ProRex Consultancy — Eigenaar · Data & Platform Engineering Consultant",
                "when": "mrt 2022 – heden",
                "bullets": [],
            },
            {
                "who": "Heijmans — Platform Engineer / Data Engineer (via ProRex)",
                "when": "dec 2025 – heden",
                "bullets": [
                    "Bouw van het Heijmans-dataplatform: data-mesh-architectuur op Azure en Databricks, alle infrastructuur als code in Terraform en Terragrunt.",
                    "Gestandaardiseerde CI/CD op Databricks Asset Bundles met herbruikbare Python-packages voor data engineering én data science.",
                    "Datapijplijnen voor SAP, Autodesk en M-Files; agentic-AI-toepassingen met een team van vijf data scientists.",
                    "Cloudteam bijgeschoold van Bicep naar Terragrunt; sparringpartner voor de solution architect.",
                ],
            },
            {
                "who": "TBI — Lead Data & Platform Engineer (via ProRex)",
                "when": "2022 – 2025",
                "bullets": [
                    "Leiding over de bouw van het data-mesh-platform van TBI: Terraform- en Terragrunt-IaC, alle gestandaardiseerde CI/CD-pijplijnen in GitHub.",
                    "BI-team (5–8 professionals) gecoacht in dbt, TMDL, Power BI-deployments vanuit code, Git en DataOps — van klassiek BI-team naar engineeringmentaliteit.",
                    "Integratieteam ondersteund bij modernisering van Azure App Services naar Kubernetes; extractiepatronen ontworpen voor 4PS (bouw-ERP).",
                ],
            },
            {
                "who": "Vattenfall — Data Engineer / Solution Architect (via ProRex)",
                "when": "2022 · 6 maanden",
                "bullets": [
                    "Een vastgelopen Azure-datawarehouse gemigreerd naar een Databricks + dbt-lakehouse: architectuur, technologiestack, infrastructuur, CI/CD en teamtraining.",
                ],
            },
            {
                "who": "GoDataDriven — Data & Analytics Consultant",
                "when": "sep 2020 – feb 2022",
                "bullets": [
                    "Dataoplossingen voor Nationale-Nederlanden, Stedin, Witteveen+Bos, Intergamma en VeiligheidNL; infrastructuur gebouwd van een herbruikbaar dataplatform dat aan klanten wordt verkocht.",
                ],
            },
            {
                "who": "Macaw — Data & Analytics Consultant",
                "when": "sep 2019 – aug 2020",
                "bullets": [
                    "Dataoplossingen voor SamenGezond (Menzis), Sustainovate en Henkel; lid technologiecommissie: platformherziening, best practices, begeleiding van juniors.",
                ],
            },
            {
                "who": "Motion10 — Data & Analytics Consultant",
                "when": "jan 2018 – aug 2019",
                "bullets": [
                    "Dataoplossingen voor acht klanten, o.a. Van Gogh Museum, ABN AMRO Pensioenfonds, TBI, Samskip en De Goudse; trainingsmateriaal en een herbruikbaar dataplatform ontwikkeld.",
                ],
            },
            {
                "who": "Vixion — Fullstack-developer",
                "when": "2017",
                "bullets": ["SSO-as-a-Service-product: API, database en applicatie (C#, ASP.NET Core, IdentityServer)."],
            },
            {
                "who": "OGD — IT-supportspecialist",
                "when": "2015 – 2016",
                "bullets": [],
            },
        ],
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
        ],
        "edu_h": "Opleiding",
        "edu": [
            ("BSc Informatica (HBO) — De Haagse Hogeschool", "2012 – 2017"),
            ("MBO 4 Applicatieontwikkelaar — ROC ID College", "2010 – 2012"),
        ],
        "skills_h": "Vaardigheden",
        "skills": [
            ("Databricks & data", "Spark, Delta Lake, Unity Catalog, Asset Bundles, dbt, dlt, SQL Server, PostgreSQL, Neo4j, Great Expectations"),
            ("Platform & cloud", "Azure (25+ services in productie), Terraform, Terragrunt, Kubernetes, Docker, GitHub Actions, Azure DevOps"),
            ("Programmeren", "Python, SQL, C#, PowerShell, Cypher"),
            ("Tooling", "uv, mise, ruff, pytest, Databricks CLI, kubectl, Git"),
            ("Methoden", "Data mesh, DataOps, metadata-gedreven ontwerp, dimensionaal modelleren, Scrum"),
            ("Talen", "Nederlands (moedertaal), Engels (vloeiend), Spaans (conversatie)"),
        ],
        "footer": "Volledig interactief portfolio: misja-pronk.github.io/resume/nl/ (NL) · misja-pronk.github.io/resume (EN)",
    },
}

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


def rule() -> HRFlowable:
    return HRFlowable(width="100%", thickness=0.7, color=LINE, spaceBefore=1, spaceAfter=5)


def heading(text: str) -> list:
    return [Paragraph(text.upper(), S["h"]), rule()]


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


def build(locale: str) -> None:
    c = CONTENT[locale]
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / c["file"]

    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=13 * mm,
        title=f"Misja Pronk — {c['title']}",
        author="Misja Pronk",
    )

    story = []

    # header
    header = Table(
        [[
            [Paragraph("MISJA PRONK", S["name"]), Spacer(1, 2), Paragraph(c["title"], S["title"])],
            [Paragraph(c["subtitle"], S["subtitle"]), Spacer(1, 3), Paragraph(c["contact"], S["contact"])],
        ]],
        colWidths=[95 * mm, 83 * mm],
    )
    header.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ])
    )
    story.append(header)
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.4, color=INK, spaceAfter=6))

    # profile
    story += heading(c["profile_h"])
    story.append(Paragraph(c["profile"], S["body"]))

    # expertise
    story += heading(c["expertise_h"])
    for item in c["expertise"]:
        story.append(Paragraph(item, S["bullet"], bulletText="—"))

    # experience
    story += heading(c["experience_h"])
    for job in c["jobs"]:
        entry = [job_row(job["who"], job["when"])]
        for b in job["bullets"]:
            entry.append(Paragraph(b, S["bullet"], bulletText="•"))
        story.append(KeepTogether(entry))

    # open source
    story += heading(c["oss_h"])
    story.append(Paragraph(c["oss"], S["body"]))

    # certifications
    story += heading(c["certs_h"])
    for cert in c["certs"]:
        story.append(Paragraph(cert, S["bullet"], bulletText="•"))

    # education
    story += heading(c["edu_h"])
    for degree, when in c["edu"]:
        story.append(job_row(degree, when))

    # skills
    story += heading(c["skills_h"])
    for label, value in c["skills"]:
        story.append(Paragraph(f"<b>{label}:</b> {value}", S["bullet"]))

    story.append(Paragraph(c["footer"], S["footer"]))

    doc.build(story)
    print(f"wrote {path}")


if __name__ == "__main__":
    for locale in ("en", "nl"):
        build(locale)
