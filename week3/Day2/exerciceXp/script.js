       // 1
        let paragraph = document.getElementsByTagName('p');
        for( let i =0; i <paragraph.length; i++){
            paragraph[i].classList.add('para_article')
        }

        let lastPara = document.body.firstElementChild.lastElementChild
        lastPara.remove()


        let headerTwo = document.querySelector('h2')
        headerTwo.addEventListener('click',removeHeader)

        function removeHeader(event){
            event.target.remove()
        }


        // let headerOne = document.body.firstElementChild.textContent
        // function headerOne (){
        //     for (i=0; i<=100; i++)
        // }
        // headerOne[i].style.fontSize = "x-large"

        //
        let firstPara = document.body.firstElementChild.children[2];// access first paragraph

        firstPara.addEventListener('click', hide)
        function hide(){
            firstPara.style.display='none'
        }

        let table = document.createElement('table')
        let tableRow1 = document.createElement('tr')
        let tableRow2 = document.createElement('tr')
        table.style.border='2px solid black'
        document.body.appendChild(table)

        let form = document.forms[0]
        let idea = form[1]
        let name = form [0]
        idea.addEventListener('change', addIdea)

        function addIdea(){
            tableRow2.innerHTML=idea.value
        }

        name.addEventListener('change', addName)
        function addName(){
            tableRow1.innerHTML=name.value
        }

        table.appendChild(tableRow1)
        table.appendChild(tableRow2)
