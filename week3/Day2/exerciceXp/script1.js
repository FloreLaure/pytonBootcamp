    function getBold_items(){
        let boldItems = document.getElementsByTagName('strong')
        console.log(boldItems)
        return boldItems;

    }

    function highlight(){
        let blue = getBold_items();
        for (let i = 0; i <blue.length; i++){
            blue[i].style.color = 'blue';
        }
    }
    highlight()

    function return_normal(){
        let returnBlack = getBold_items();
        for (let i = 0; i < returnBlack.length; i++){
            returnBlack[i].style.color = 'black';
        }
    }

    document.addEventListener("mouseover", highlight);
    document.addEventListener("mouseout", return_normal);



</script>   