var post = {
    heart : function(id, element) {
        fetch("/api/like?id=" + id)
            .then(response => response.json())
            .then(res => {
                    console.log(element.childNodes)
            
            if (res.voted == true){
                element.childNodes[1].innerHtml = "<p>Upvoted</p>"
            }else{
                element.childNodes[1].innerHtml = "<p>Downvoted</p>"
            }}});
    }
}