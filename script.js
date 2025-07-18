let pyodide;

async function startPyodide() {
    pyodide = await loadPyodide();
    console.log("✅ Pyodide is ready!");
}

async function runPythonFile(filename) {
    const response = await fetch(filename);
    const code = await response.text();
    await pyodide.runPythonAsync(code);
}

async function runMyPythonCode() {
    const result = await pyodide.runPythonAsync(`
def square(x):
    return x * x

square(7)
`);
    console.log("Python result:", result);
}

document.addEventListener("DOMContentLoaded", async () => {
    const root = document.documentElement;
    const btn = document.getElementById("colorToggle");

    if (btn) {
        btn.addEventListener("click", () => {
            const currentBg = getComputedStyle(root).getPropertyValue("--background").trim();

            if (currentBg === "rgba(189, 233, 250, 1)") {
                root.style.setProperty("--background", "rgba(12, 29, 63, 1)");
                root.style.setProperty("--foreground", "rgba(189, 233, 250, 1)");
                btn.textContent = "Light Theme";
            } else {
                root.style.setProperty("--background", "rgba(189, 233, 250, 1)");
                root.style.setProperty("--foreground", "rgba(12, 29, 63, 1)");
                btn.textContent = "Dark Theme";
            }
        });
    }

    function typeWriterEffect(element, text, speed = 100, callback = null) {
        let index = 0;
        element.textContent = "";

        function type() {
            if (index < text.length) {
                element.textContent += text.charAt(index);
                index++;
                setTimeout(type, speed);
            } else if (callback) {
                callback();
            }
        }
        type();
    }

    const h1 = document.querySelector(".typewriter");
    const h3 = document.querySelector(".typewriter-secondary");

    if (h1 && h3) {
        const h1Text = h1.getAttribute("data-text");
        const h3Text = h3.getAttribute("data-text");

        typeWriterEffect(h1, h1Text, 150, () => {
            typeWriterEffect(h3, h3Text, 50);
        });
    }

    setTimeout(() => {
        document.querySelectorAll(".blink-cursor").forEach(el => {
            el.classList.remove("blink-cursor");
        });
    }, 2000);

    fetch('https://api.chess.com/pub/player/chessking43409/stats')
        .then(response => response.json())
        .then(data => {
            const rapidRating = data.chess_rapid?.last?.rating;
            document.getElementById('liveRating').textContent =
                rapidRating ? `Current Rapid Rating: ${rapidRating}` : 'Could not load rating.';
        })
        .catch(() => {
            document.getElementById('liveRating').textContent = 'Could not load rating.';
        });

  await startPyodide();

  try {
    //await runPythonFile("program.py");     // Now run main code that imports it
    const response = await fetch("program.py");
    const pythonCode = await response.text();
    await pyodide.runPythonAsync(pythonCode);
  } catch (err) {
    console.error("🐍 Error running Python:", err);
  }


    const pyBtn = document.getElementById("madeFrompython");
    if (pyBtn) {
        pyBtn.addEventListener("click", () => {
            runMyPythonCode();
        });
    }
});

let typed = "";
document.addEventListener("keydown", (e) => {
    if (document.activeElement.tagName === "INPUT" || document.activeElement.tagName === "TEXTAREA") return;

    typed += e.key.toLowerCase();
    if (typed.length > 7) typed = typed.slice(-7);

    if (typed === "awesome") {
        document.body.classList.toggle("reverse-gradient");
        typed = "";
    }
});

const animateConicGradient = () => {
    const elements = document.querySelectorAll('fieldset, details');
    let angle = 0;

    const update = () => {
        angle = (angle + 1) % 360;
        elements.forEach(el => {
            el.style.setProperty('--angle', `${angle}deg`);
        });
        requestAnimationFrame(update);
    };

    update();
};

animateConicGradient();
