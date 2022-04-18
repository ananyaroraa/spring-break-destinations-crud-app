function error_detection(){

	flag = 0

	$("#city_warning").empty()
	$("#country_warning").empty()
	$("#rank_warning").empty()
	$("#image_warning").empty()
	$("#maps_warning").empty()
	$("#facts_warning").empty()
	$("#things_warning").empty()
	$("#hotels_warning").empty()
	$("#restaurants_warning").empty()
	$("#temperature_warning").empty()
	$("#currency_warning").empty()
	$("#requirement_warning").empty()
	$("#type_warning").empty()
	$("#famous_warning").empty()
	$("#more_warning").empty()

	if ($("#city_input").val().trim() == ''){

		$("#city_warning").text("Error! Please enter value!")
		$("#city_input").val('')
		$("#city_input").focus()
		flag = flag + 1
	}

	if ($("#country_input").val().trim() == ''){

		$("#country_warning").text("Error! Please enter value!")
		$("#country_input").val('')
		$("#country_input").focus()
		flag = flag + 1
	}

	if ($("#rank_input").val().trim() == ''){

		$("#rank_warning").text("Error! Please enter value!")
		$("#rank_input").val('')
		$("#rank_input").focus()
		flag = flag + 1
	}

	if ($("#image_input").val().trim() == ''){

		$("#image_warning").text("Error! Please enter value!")
		$("#image_input").val('')
		$("#image_input").focus()
		flag = flag + 1
	}

	if ($("#maps_input").val().trim() == ''){

		$("#maps_warning").text("Error! Please enter value!")
		$("#maps_input").val('')
		$("#maps_input").focus()
		flag = flag + 1
	}

	if ($("#facts_input").val().trim() == ''){

		$("#facts_warning").text("Error! Please enter value!")
		$("#facts_input").val('')
		$("#facts_input").focus()
		flag = flag + 1
	}

	if ($("#things_input").val().trim() == ''){

		$("#things_warning").text("Error! Please enter value!")
		$("#things_input").val('')
		$("#things_input").focus()
		flag = flag + 1
	}

	if ($("#hotels_input").val().trim() == ''){

		$("#hotels_warning").text("Error! Please enter value!")
		$("#hotels_input").val('')
		$("#hotels_input").focus()
		flag = flag + 1
	}

	if ($("#restaurants_input").val().trim() == ''){

		$("#restaurants_warning").text("Error! Please enter value!")
		$("#restaurants_input").val('')
		$("#restaurants_input").focus()
		flag = flag + 1
	}

	if ($("#temperature_input").val().trim() == ''){

		$("#temperature_warning").text("Error! Please enter value!")
		$("#temperature_input").val('')
		$("#temperature_input").focus()
		flag = flag + 1
	}

	if ($("#currency_input").val().trim() == ''){

		$("#currency_warning").text("Error! Please enter value!")
		$("#currency_input").val('')
		$("#currency_input").focus()
		flag = flag + 1
	}

	if ($("#requirement_input").val().trim() == ''){

		$("#requirement_warning").text("Error! Please enter value!")
		$("#requirement_input").val('')
		$("#requirement_input").focus()
		flag = flag + 1
	}

	if ($("#type_input").val().trim() == ''){

		$("#type_warning").text("Error! Please enter value!")
		$("#type_input").val('')
		$("#type_input").focus()
		flag = flag + 1
	}

	if ($("#famous_input").val().trim() == ''){

		$("#famous_warning").text("Error! Please enter value!")
		$("#famous_input").val('')
		$("#famous_input").focus()
		flag = flag + 1
	}

	if ($("#more_input").val().trim() == ''){

		$("#more_warning").text("Error! Please enter value!")
		$("#more_input").val('')
		$("#more_input").focus()
		flag = flag + 1
	}


	return flag
}





function add_data(){

	city = ($("#city_input")).val()
	country = ($("#country_input")).val()
	rank = ($("#rank_input")).val()
	image = ($("#image_input")).val()
	map_link = ($("#maps_input")).val()
	facts = ($("#facts_input")).val()
	things_to_do = ($("#things_input")).val()
	hotels = ($("#hotels_input")).val()
	restaurants = ($("#restaurants_input")).val()
	temperature = ($("#temperature_input")).val()
	currency = ($("#currency_input")).val()
	travel_requirements = ($("#requirement_input")).val()
	destination_type = ($("#type_input")).val()
	famous_for = ($("#famous_input")).val()
	more_like_this = ($("#more_input")).val()

	things_to_do = clean(things_to_do)
	hotels = clean(hotels)
	restaurants = clean(restaurants)
	travel_requirements = clean(travel_requirements)
	famous_for = clean(famous_for)
	more_like_this = clean(more_like_this)

	data = {
		"rank": rank,
		"city": city,
		"country": country,
		"image": image,
		"map_link": map_link,
		"facts": facts,
		"things_to_do": things_to_do,
		"hotels": hotels,
		"restaurants": restaurants,
		"temperature": temperature,
		"currency": currency,
		"travel_requirements": travel_requirements,
		"destination_type": destination_type,
		"famous_for": famous_for,
		"more_like_this": more_like_this
	}

	send_data(data)

}

function clean(text_data){

	clean_text = text_data.split(',')
	// console.log(clean_text)

	return clean_text
}


function view_new(new_id){

	$("<h5 id = 'sub_feedback'> Successfully Added Data!</h5>").appendTo("#feedback")
	$("<h5><a href = '/view/" + new_id + "'> Click here to view your new entry</a> or continue adding!</h5>").appendTo("#sub_feedback")
	empty_everything()

}

function empty_everything(){

	$("#city_input").val('')
	$("#country_input").val('')
	$("#rank_input").val('')
	$("#image_input").val('')
	$("#maps_input").val('')
	$("#facts_input").val('')
	$("#things_input").val('')
	$("#hotels_input").val('')
	$("#restaurants_input").val('')
	$("#temperature_input").val('')
	$("#currency_input").val('')
	$("#requirement_input").val('')
	$("#type_input").val('')
	$("#famous_input").val('')
	$("#more_input").val('')
	$("#city_input").focus()

}

function send_data(data){

	$.ajax({

		type: "POST",
		url: "save_data",
		contentType: "application/json; charset=utf-8",
		data: JSON.stringify(data),
		success: function(result){

			new_id = result

			console.log(new_id)

			view_new(new_id)

		}


	})
}



$(document).ready(function(){

	$("#submit_button").click(function(){

		flag = error_detection()

		console.log(flag)

		if (flag == 0){

			add_data()
		}



	})
})


