const API_BASE_URL = "https://ai-project-atlas-api.onrender.com";


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

        for (const project of projects) {
            const projectCard = document.createElement("article");

            projectCard.innerHTML = `
                <h3>${project.id.toUpperCase()} — ${project.title}</h3>

                <p>
                    <strong>Domain:</strong>
                    ${project.domain}
                </p>

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

            projectList.appendChild(projectCard);
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
                            💻 View Source Code
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
            runButton.addEventListener("click", () => {
                window.open(
                    "http://localhost:8501",
                    "_blank"
                );
            });
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