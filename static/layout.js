
function display_search(search_result){

	console.log("Got search value in function")
	console.log(search_result)

	window.location.href = '/search_results/'+  search_result;    


}


function redirect_to_add_page(){


	window.location.href = '/add'


}



$(document).ready(function(){

	$("#search_button").click(function(){

		search_val = ($("#search_bar").val())


		if (search_val.trim().length == 0){

			$("#search_bar").val('')
			$("#search_bar").focus('')
		}


		else{

			console.log(search_val)
			display_search(search_val)
		}


	})


	$("#search_bar").keyup(function(){
		if (event.which === 13) {
            $("#search_button").click()
    	}
	})


	$("#add_data_button").click(function(){

		redirect_to_add_page()
	})


})


