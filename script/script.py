from pyscript import document

def carica_competenze(event):
    competenze = [
        "C# / .NET", 
        "Python (Numpy, Pandas, Scikit-learn)", 
        "SQL (DB2, MySQL, Ottimizzazione)", 
        "Ingegneria ETL",
        "Machine Learning", 
        "Git & GitHub", 
        "Problem Solving"
    ]
    
    container = document.querySelector("#skills-container")
    container.innerHTML = " " 
    
    # Renderizziamo gli elementi aggiungendo un delay matematico
    for indice, skill in enumerate(competenze):
        tag = document.createElement("span")
        tag.className = "skill-tag"
        tag.innerText = skill
        
        # Aggiungiamo 0.1s di ritardo in più per ogni competenza
        ritardo = indice * 0.1
        tag.style.animationDelay = f"{ritardo}s"
        
        container.appendChild(tag)
        
    # Facciamo sparire il bottone con una transizione pulita
    bottone = document.querySelector("#btn-skills")
    bottone.style.transition = "opacity 0.4s ease, height 0.4s ease"
    bottone.style.opacity = "0"
    bottone.style.pointerEvents = "none"