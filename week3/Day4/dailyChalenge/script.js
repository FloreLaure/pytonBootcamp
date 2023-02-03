// Todo list
let listTasks = [];
let formulaire,div,contenu,p,check,label;
let valeur;
submit = document.getElementById("add");
submit.addEventListener("click",function addTask(event){//l'évènement se déclenche lorque le formulaire est soumis
        valeur=document.getElementById("text").value;
        if(valeur==""){
        alert("Entrée vide");
        }else{
            listTasks=valeur;

            // utilisation de nextElementSibling
            formulaire=document.body.firstElementChild.nextElementSibling;
            div = document.getElementsByClassName("listTasks")[0];
            contenu= document.createTextNode(listTasks);
            p=document.createElement("p");

            // ajout de la croix
            var font=document.createElement("i");
            font.setAttribute("class","fa-solid fa-xmark");
            p.appendChild(font);

            //ckeckbox
            check=document.createElement("input");
            check.type='checkbox';
            check.id='choix';
            check.name='choix';
            label=document.createElement("label");
            label.htmlFor=contenu.textContent;
            p.appendChild(check);
            check.appendChild(label);
            p.appendChild(contenu);
            div.appendChild(p);
        }
        document.getElementById("text").value = "";
        event.preventDefault();//pour que les valeur ne se réinitialise pas 
    });
