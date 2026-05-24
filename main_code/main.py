<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ali Rosyid - Founding AI Architect</title>
    <style>
        :root {
            --primary: #c0392b; /* Warna aksen merah/oranye tajam khas database/Oracle */
            --secondary: #2c3e50;
            --accent: #ecf0f1;
            --text-main: #2d3436;
            --text-light: #636e72;
        }
        body {
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.4;
            color: var(--text-main);
            max-width: 850px;
            margin: 0 auto;
            padding: 0mm 15mm 5mm 15mm;
            background-color: #ffffff;
        }
        h1 {
            font-size: 30px;
            color: var(--secondary);
            margin-top: 0px !important; 
            margin-bottom: 2px;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 800;
        }
        h2 {
            font-size: 16px;
            color: var(--secondary);
            border-bottom: 2px solid var(--primary);
            padding-bottom: 2px;
            margin-top: 12px;
            margin-bottom: 8px;
            text-transform: uppercase;
            font-weight: 700;
        }
        .contact-info {
            font-size: 13px;
            color: var(--text-light);
            margin-bottom: 12px;
            display: flex;
            gap: 15px;
            font-weight: 500;
        }
        .contact-info a {
            color: var(--primary);
            text-decoration: none;
            font-weight: bold;
        }
        .summary {
            font-size: 13.5px;
            margin-bottom: 12px;
            text-align: justify;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            font-size: 13px;
        }
        .experience-item {
            margin-bottom: 12px;
        }
        .job-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 2px;
        }
        .job-title {
            font-weight: bold;
            font-size: 14px;
            color: var(--secondary);
        }
        .job-date {
            font-size: 13px;
            color: var(--text-light);
            font-weight: bold;
        }
        ul {
            margin-top: 2px;
            padding-left: 20px;
            font-size: 13px;
            margin-bottom: 0;
        }
        li {
            margin-bottom: 4px;
        }
        .highlight {
            font-weight: bold;
            color: var(--primary);
        }

        /* ATURAN MUTLAK UNTUK CETAK PDF 1 HALAMAN */
        @media print {
            @page {
                size: A4 portrait;
                margin: 0 !important;
            }
            body {
                padding: 5mm 15mm 5mm 15mm !important; 
            }
            h1 {
                margin-top: 0 !important;
                padding-top: 0 !important;
            }
        }
    </style>
</head>
<body>

    <h1>Ali Rosyid</h1>
    <div class="contact-info">
        <span>Software & AI Architect</span> |
        <span><a href="mailto:aliahamdarrosyid@gmail.com">aliahamdarrosyid@gmail.com</a></span> |
        <span><a href="https://www.linkedin.com/in/alirosyid-ai-automation" target="_blank">LinkedIn</a></span> |
        <span><a href="https://github.com/alirosyid/b2b-automation-architectures" target="_blank">GitHub</a></span>
    </div>

    <div class="summary">
        Software Architect specialized in wrapping probabilistic AI models (LLMs) within deterministic, verifiable enterprise systems. Expert in architecting stateful, multi-agent workflows using Python, robust API backend routing, and Model Context Protocol (MCP). Proven ability to enforce rigid systemic guardrails—utilizing typed contracts and structured outputs—to ensure non-deterministic components execute idempotently in production environments.
    </div>

    <h2>Core Architecture & Deterministic Logic</h2>
    <div class="skills-grid">
        <ul>
            <li><span class="highlight">Agent Orchestration:</span> Stateful workflow engines, directed graph logic, tool server integration, and replayable execution loops.</li>
            <li><span class="highlight">Verifiable AI Systems:</span> Model Context Protocol (MCP), Structured JSON validation, strict multi-component prompt engineering.</li>
        </ul>
        <ul>
            <li><span class="highlight">Backend Engineering:</span> Python, REST/GraphQL APIs, PostgreSQL, Webhook routing, durable background jobs.</li>
            <li><span class="highlight">Infrastructure & DevOps:</span> Docker containerization, Cloud deployments, CI/CD, system observability.</li>
        </ul>
    </div>

    <h2>Engineering Execution</h2>

    <div class="experience-item">
        <div class="job-header">
            <span class="job-title">Senior AI Automation Architect (Independent B2B Contract)</span>
            <span class="job-date">2023 - Present</span>
        </div>
        <div><em>Deterministic Workflows & Multi-Agent Infrastructure</em></div>
        <ul>
            <li>Architected and shipped end-to-end multi-agent systems, replacing raw probabilistic LLM outputs with deterministic pipelines by enforcing rigid JSON schemas and typed contracts for all API interactions.</li>
            <li>Engineered stateful validation loops within orchestration workflows (Python/n8n), ensuring failed API tool-calls trigger logic-based retries rather than hallucinatory cascading errors.</li>
            <li>Built custom Model Context Protocol (MCP) servers and RAG pipelines, connecting AI agents securely to PostgreSQL databases and external SaaS platforms with strict access constraints.</li>
            <li>Designed a proprietary 6-component systemic guardrail framework (Role, Task, Constraint mapping) that guarantees idempotent execution across high-volume operational tasks.</li>
        </ul>
    </div>

    <div class="experience-item">
        <div class="job-header">
            <span class="job-title">Backend Infrastructure & Process Integration Engineer</span>
            <span class="job-date">2022 - 2024</span>
        </div>
        <div><em>Data Engineering & System Reliability</em></div>
        <ul>
            <li>Developed and maintained secure Python backend services, focusing on data extraction, API normalization, and continuous integration.</li>
            <li>Monitored distributed architectures using Docker, ensuring low-latency data routing and SLA compliance across automated operational workflows.</li>
        </ul>
    </div>

    <h2>Technical Proof of Work</h2>
    <div class="experience-item">
        <div class="job-header">
            <span class="job-title"><a href="https://github.com/alirosyid/b2b-automation-architectures" target="_blank">b2b-automation-architectures (GitHub Repository)</a></span>
        </div>
        <ul>
            <li>My public repository showcasing production blueprints: how I wrap non-deterministic LLM tool-calling inside deterministic Python logic, enforce MCP, and design durable, replayable AI architectures.</li>
        </ul>
    </div>

</body>
</html>
