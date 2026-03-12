from pyscript import document

def carica_competenze(event):
    competenze = ["HTML5", "CSS3", "Python", "C#", "SQL", "Git & GitHub", "Problem Solving"]
    
    container = document.querySelector("#skills-container")
    container.innerHTML = "" 
    
    for skill in competenze:
        tag = document.createElement("span")
        tag.className = "skill-tag"
        tag.innerText = skill
        container.appendChild(tag)
        
    document.querySelector("#btn-skills").style.display = "none"
