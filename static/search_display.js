function display(cities, city_result_num, countries, country_result_num, types, type_result_num){

	

	$("#display_names_city").empty()
	$("#display_names_country").empty()
	$("#display_names_type").empty()

	if (cities.length != 0){

		$("<div class = 'col-md-12 search_result_title'><br><br><h5> Results Filtered by City </h5></div>").appendTo("#display_names_city")
		$("<div class = 'col-md-12 search_result_number'><h5>" + city_result_num + " results found </h5></div>").appendTo("#display_names_city")

		for (let i = 0; i < cities.length; i++){


				row_id = "#sub_display_names_city" + i
				img_row_id = "#sub_display_img_city" + i
				col_id = "#col_city" + i

				$("<div class = 'col-md-3 search_polaroid' id = 'col_city" + i + "'>").appendTo("#display_names_city")
				$("<div class = 'row ' id = 'sub_display_names_city" + i + "'>").appendTo(col_id)
				$("<div class = 'col-md-12'><h5><a href = '/view/" + cities[i]["id"] + "'>" + cities[i]["city"] + ", " + cities[i]["country"] + "</a></h5></div>").appendTo(row_id)
				$("<div class = 'row' id = 'sub_display_img_city" + i + "'>").appendTo(col_id)
				$("<div class = 'col-md-12'><a href = '/view/" + cities[i]["id"]+ "'><img src = '" + cities[i]["image"] + "'class = 'search_img'></img></a></div>").appendTo(img_row_id)

		}

		
		let custfilter = new RegExp(search_term, "ig")
		let repstr = "<span class='highlight'>" + search_term + "</span>"


			for (let i = 0; i < cities.length; i++){

					row_id = "#sub_display_names_city" + i

					$(row_id).each(function() {
			            
			            $(this).children().children().children().children().prevObject[0].innerHTML = $(this).children().children().children().children().prevObject[0].innerHTML.replace(custfilter, '<mark class="highlight">$&</mark>')
			            
			        })

				}

	}


	if (countries.length != 0){

		$("<div class = 'col-md-12 search_result_title'><br><br><h5> Results Filtered by Country </h5></div>").appendTo("#display_names_country")
		$("<div class = 'col-md-12 search_result_number'><h5>" + country_result_num + " results found </h5></div>").appendTo("#display_names_country")

		for (let i = 0; i < countries.length; i++){


				row_id = "#sub_display_names_country" + i
				col_id = "#col_country" + i
				img_row_id = "#sub_display_country_img_city" + i

				$("<div class = 'col-md-3 search_polaroid' id = 'col_country" + i + "'>").appendTo("#display_names_country")
				$("<div class = 'row ' id = 'sub_display_names_country" + i + "'>").appendTo(col_id)
				$("<div class = 'col-md-12'><h5><a href = '/view/" + countries[i]["id"] + "'>" + countries[i]["city"] + ", " + countries[i]["country"] + "</a></h5></div>").appendTo(row_id)
				$("<div class = 'row' id = 'sub_display_country_img_city" + i + "'>").appendTo(col_id)
				$("<div class = 'col-md-12'><a href = '/view/" + countries[i]["id"]+ "'><img src = '" + countries[i]["image"] + "'class = 'search_img'></img></a></div>").appendTo(img_row_id)

		}

		
		let custfilter = new RegExp(search_term, "ig")
		let repstr = "<span class='highlight'>" + search_term + "</span>"


			for (let i = 0; i < countries.length; i++){

					row_id = "#sub_display_names_country" + i

					$(row_id).each(function() {
			            
			            $(this).children().children().children().children().prevObject[0].innerHTML = $(this).children().children().children().children().prevObject[0].innerHTML.replace(custfilter, '<mark class="highlight">$&</mark>')
			            
			        })

				}

	}


	if (types.length != 0){

		$("<div class = 'col-md-12 search_result_title'><br><br><h5> Results Filtered by Destination Type </h5></div>").appendTo("#display_names_type")
		$("<div class = 'col-md-12 search_result_number'><h5>" + type_result_num + " results found </h5></div>").appendTo("#display_names_type")

		for (let i = 0; i < types.length; i++){


				row_id = "#sub_display_names_type" + i
				col_id = "#col_type" + i
				img_row_id = "#sub_display_type_img_city" + i

				$("<div class = 'col-md-3 search_polaroid' id = 'col_type" + i + "'>").appendTo("#display_names_type")
				$("<div class = 'row' id = 'sub_display_names_type" + i + "'>").appendTo(col_id)
				$("<div class = 'col-md-12'><h5><a href = '/view/" + types[i]["id"] + "'>" + types[i]["city"] + ", " + types[i]["country"] + " (" + types[i]["destination_type"] + ")</a></h5></div>").appendTo(row_id)
				$("<div class = 'row' id = 'sub_display_type_img_city" + i + "'>").appendTo(col_id)
				$("<div class = 'col-md-12'><a href = '/view/" + types[i]["id"]+ "'><img src = '" + types[i]["image"] + "'class = 'search_img'></img></a></div>").appendTo(img_row_id)

		}

		
		let custfilter = new RegExp(search_term, "ig")
		let repstr = "<span class='highlight'>" + search_term + "</span>"


			for (let i = 0; i < types.length; i++){

					row_id = "#sub_display_names_type" + i

					$(row_id).each(function() {
			            
			            $(this).children().children().children().children().prevObject[0].innerHTML = $(this).children().children().children().children().prevObject[0].innerHTML.replace(custfilter, '<mark class="highlight">$&</mark>')
			            
			        })

				}

	}

	if (types.length == 0 && countries.length == 0 && cities.length == 0){


		$("<div class = 'col-md-12' id = col>").appendTo("#display_names_city")
		$("<div class = 'row' id = 'row'>").appendTo("#col")
		$("<div class = 'col-md-12'><h5> No Results Found </h5></div>").appendTo("#row")


	}

}


$(document).ready(function(){


	display(search_city_result, search_city_result_number, search_country_result, search_country_result_number, search_type_result, search_type_result_number)


})