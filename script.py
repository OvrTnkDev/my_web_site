from pyscript import document

def carica_competenze(event):
    # Competenze estratte dal tuo background
    competenze = [
        "C# / .NET", 
        "Python (Pandas, Scikit-learn)", 
        "SQL (DB2, Ottimizzazione)", 
        "Ingegneria ETL",
        "Machine Learning", 
        "ASP.NET Core", 
        "Git & GitHub", 
        "Problem Solving"
    ]
    
    container = document.querySelector("#skills-container")
    container.innerHTML = "" 
    
    for skill in competenze:
        tag = document.createElement("span")
        tag.className = "skill-tag"
        tag.innerText = skill
        container.appendChild(tag)
        
    document.querySelector("#btn-skills").style.display = "none"
