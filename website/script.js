// const API_BASE_URL = "https://ai-project-atlas-api.onrender.com";
const API_BASE_URL = "";


function getProjectIcon(project) {
    const searchableText = [
        ...(project.topics || []),
        ...(project.tags || []),
        project.project_type || "",
        project.title || "",
    ]
        .join(" ")
        .toLowerCase();

    // Check specific topics before broader categories.
    if (
        searchableText.includes("vector") ||
        searchableText.includes("linear algebra")
    ) {
        return "\u{1F9ED}"; // Compass
    }

    if (
        searchableText.includes("lstm") ||
        searchableText.includes("neural network") ||
        searchableText.includes("deep learning")
    ) {
        return "\u{1F9E0}"; // Brain
    }
        
    if (
        searchableText.includes("nlp") ||
        searchableText.includes("natural language processing") ||
        searchableText.includes("natural language") ||
        searchableText.includes("text classification") ||
        searchableText.includes("text preprocessing") ||
        searchableText.includes("emotion classification")
    ) {
        return "\u{1F4AC}"; // Speech bubble
    }


    if (
        searchableText.includes("llm") ||
        searchableText.includes("language model") ||
        searchableText.includes("generative ai")
    ) {
        return "\u2728"; // Sparkles
    }

    if (
        searchableText.includes("regression") ||
        searchableText.includes("classification") ||
        searchableText.includes("machine learning")
    ) {
        return "\u{1F4C8}"; // Chart
    }

    return "\u{1F916}"; // Robot fallback
}


async function loadProjects() {
    const projectList = document.getElementById("project-list");

    try {
        const response = await fetch(
            `${API_BASE_URL}/api/projects`
        );

        if (!response.ok) {
            throw new Error("Could not load projects.");
        }

        const projects = await response.json();

        projectList.innerHTML = "";

        const domainSections = new Map();

        for (const project of projects) {
            if (!domainSections.has(project.domain)) {
                const domainSection = document.createElement("section");
                domainSection.className = "catalogue-domain";

                domainSection.innerHTML = `
                    <h3>${project.domain}</h3>
                    <div class="catalogue-domain-projects"></div>
                `;

                projectList.appendChild(domainSection);

                domainSections.set(
                    project.domain,
                    domainSection.querySelector(".catalogue-domain-projects")
                );
            }

            const projectCard = document.createElement("article");
            const projectIcon = getProjectIcon(project);

            projectCard.innerHTML = `
                <h3 class="project-heading">
                    <span class="project-icon" aria-hidden="true">
                        ${projectIcon}
                    </span>
                    <span class="project-reference">
                        ${project.id.toUpperCase()}
                    </span>
                    <span class="project-title">
                        — ${project.title}
                    </span>
                </h3>

                <p>
                    <strong>Difficulty:</strong>
                    ${project.difficulty}
                </p>

                <p>
                    <strong>Project Type:</strong>
                    ${project.project_type}
                </p>

                <button data-project-id="${project.id}">
                    View Project
                </button>
            `;

            const viewButton = projectCard.querySelector("button");

            viewButton.addEventListener("click", () => {
                showProjectDetails(project.id);
            });

            domainSections
                .get(project.domain)
                .appendChild(projectCard);
        }

    } catch (error) {
        projectList.innerHTML = `
            <p>Unable to load projects.</p>
        `;

        console.error(error);
    }
}


async function showProjectDetails(projectId) {
    const catalogueView = document.getElementById("catalogue-view");
    const detailView = document.getElementById("project-detail-view");
    const projectDetail = document.getElementById("project-detail");

    catalogueView.hidden = true;
    detailView.hidden = false;

    projectDetail.innerHTML = "Loading project...";

    try {
        const response = await fetch(
            `${API_BASE_URL}/api/projects/${projectId}`
        );

        if (!response.ok) {
            throw new Error("Could not load project.");
        }

        const project = await response.json();

        projectDetail.innerHTML = `
            <h1>
                ${project.id.toUpperCase()} — ${project.title}
            </h1>

            <p>
                <strong>Domain:</strong>
                ${project.domain}
            </p>

            <p>
                <strong>Difficulty:</strong>
                ${project.difficulty}
            </p>

            <p>
                <strong>Status:</strong>
                ${project.status}
            </p>

            <h2>Topics</h2>

            <ul>
                ${project.topics
                    .map(topic => `<li>${topic}</li>`)
                    .join("")}
            </ul>

            <h2>Technologies</h2>

            <ul>
                ${project.technologies
                    .map(technology => `<li>${technology}</li>`)
                    .join("")}
            </ul>

            <h2>Capabilities</h2>

            <ul>
                ${project.capabilities
                    .map(capability => `<li>${capability}</li>`)
                    .join("")}
            </ul>

            <h2>Learning Outcomes</h2>

            <ul>
                ${project.learning_outcomes
                    .map(outcome => `<li>${outcome}</li>`)
                    .join("")}
            </ul>

            ${project.artifacts && project.artifacts.github
                ? `
                    <h2>Project Resources</h2>

                    <p>
                        <a
                            href="${project.artifacts.github}"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            💻 View Code on GitHub
                        </a>
                    </p>
                `
                : ""
            }

            ${project.experiences && project.experiences.length > 0
                ? `
                    <h2>Interactive Experience</h2>

                    <p>
                        ${project.experiences[0].description}
                    </p>

                    <button id="run-project">
                        Run Project
                    </button>
                `
                : ""
            }
        `;

        const runButton = document.getElementById("run-project");

        if (runButton) {
            const execution =
                project.experiences &&
                project.experiences[0] &&
                project.experiences[0].execution;

            const executionUrl = execution && execution.url;

            if (execution && execution.requested && executionUrl) {
                runButton.addEventListener("click", () => {
                    window.open(executionUrl, "_blank");
                });
            } else {
                runButton.disabled = true;
                runButton.textContent = "Demo Unavailable";
            }
        }
    } catch (error) {
        projectDetail.innerHTML = `
            <p>Unable to load project.</p>
        `;

        console.error(error);
    }
}


function showCatalogue() {
    const catalogueView = document.getElementById("catalogue-view");
    const detailView = document.getElementById("project-detail-view");

    detailView.hidden = true;
    catalogueView.hidden = false;
}


document
    .getElementById("back-to-projects")
    .addEventListener("click", showCatalogue);


loadProjects();