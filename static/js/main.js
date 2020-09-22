function next_random_quiz(){
    $.get("/bopomofo/", function(result){
    console.log(result);
    });
}

$(function(){
    next_random_quiz();
});    