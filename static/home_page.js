function display(cities){

	most_popular_cities = []
	most_popular_cities.push(cities[5])
	most_popular_cities.push(cities[11])
	most_popular_cities.push(cities[0])

	$("#display_names").empty()

	for (let i = 0; i < most_popular_cities.length; i++){


			row_id = "#sub_display_names" + i
			col_id = "#col" + i

			$("<div class = 'col-md-4' id = 'col" + i + "'>").appendTo("#display_names")
			$("<div class = 'row' id = 'sub_display_names" + i + "'>").appendTo(col_id)
			$("<div class = 'col-md-12 home_title'><h5><a href = '/view/" + most_popular_cities[i]["id"] + "'><span class = home_city>" + most_popular_cities[i]["city"] + "</span>, " + most_popular_cities[i]["country"] + "</a></h5></div>").appendTo(row_id)
			$("<div class = 'col-md-12'><a href = '/view/" + most_popular_cities[i]["id"] + "'><img src = " + most_popular_cities[i]["image"] + "></a></div>").appendTo(row_id)
			$("<div class = 'col-md-12 one_liner'>" + most_popular_cities[i]["alt_facts"] + "</div>").appendTo(row_id)
	}

}


$(document).ready(function(){

	console.log(cities[5])


	display(cities)



})