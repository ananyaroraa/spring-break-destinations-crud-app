function prepopulate(){

	$("#city_input").val(city_name)
	$("#country_input").val(country)
	$("#rank_input").val(rank)
	$("#image_input").val(image)
	$("#maps_input").val(map_link)
	$("#facts_input").val(facts)
	$("#things_input").val(city.things_to_do)
	$("#hotels_input").val(city.hotels)
	$("#restaurants_input").val(city.restaurants)
	$("#temperature_input").val(temperature)
	$("#currency_input").val(currency)
	$("#requirement_input").val(city.travel_requirements)
	$("#type_input").val(destination_type)
	$("#famous_input").val(city.famous_for)
	$("#more_input").val(city.more_like_this)
}

function send_new_data(data){

	$.ajax({

		type: "POST",
		url: "http://127.0.0.1:5000/edit_data",
		contentType: "application/json; charset=utf-8",
		data: JSON.stringify(data),
		success: function(result){

			window.location.href = '/view/'+  id 

		}


		})

}


$(document).ready(function(){


	prepopulate()
	console.log(restaurants)

	$("#submit_button").click(function(){

		new_city_val = $("#city_input").val()
		new_country_val = $("#country_input").val()
		new_rank_val = $("#rank_input").val()
		new_image_val = $("#image_input").val()
		new_map_val = $("#maps_input").val()
		new_facts_val = $("#facts_input").val()
		new_things_val = $("#things_input").val()
		new_hotels_val = $("#hotels_input").val()
		new_restaurants_val = $("#restaurants_input").val()
		new_temperature_val = $("#temperature_input").val()
		new_currency_val = $("#currency_input").val()
		new_requirement_val = $("#requirement_input").val()
		new_type_val = $("#type_input").val()
		new_famous_val = $("#famous_input").val()
		new_more_val = $("#more_input").val()


		data = {

			"id": id,
			"city": new_city_val,
			"country": new_country_val,
			"rank": new_rank_val,
			"image": new_image_val,
			"map_link": new_map_val,
			"facts": new_facts_val,
			"things_to_do": new_things_val,
			"hotels": new_hotels_val,
			"restaurants": new_restaurants_val,
			"temperature": new_temperature_val,
			"currency": new_currency_val,
			"travel_requirements": new_requirement_val,
			"destination_type": new_type_val,
			"famous_for": new_famous_val,
			"more_like_this": new_more_val
		}

		send_new_data(data)


	})

	$("#dialog").dialog({
            modal: true,
            autoOpen: false,
            title: "Discard Changes",
            width: 300,
            height: 150
        })


	$("#discard_button").click(function(){

		$('#dialog').dialog('open')

	})

	$("#yes_discard").click(function(){

		window.location.href = '/view/'+  id 

	})

	$("#no_discard").click(function(){

		$('#dialog').dialog( "close" )

	})


})


