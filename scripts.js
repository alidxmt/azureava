// Function to create SVG and append it to the main div
function createSVG() {
const mainDiv = document.getElementById('main-div');

// Create SVG element
const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
svg.setAttribute('id', 'main-svg');
svg.setAttribute('width', '100%');
svg.setAttribute('height', '100%');

// Create a line element inside the SVG
const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
line.setAttribute('id', 'line');
line.setAttribute('x1', '10%');
line.setAttribute('y1', '10%');
line.setAttribute('x2', '90%');
line.setAttribute('y2', '90%');
line.setAttribute('stroke', 'black');
line.setAttribute('stroke-width', '2');

// Append the line to the SVG
svg.appendChild(line);

// Append the SVG to the main div
mainDiv.appendChild(svg);
}

// Call the function to create SVG
createSVG();
