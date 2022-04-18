from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 12

cities = [

    {

        "id": "1",
        "rank": "1",
        "city": "Cancun",
        "country": "Mexico",
        "image":"https://media.istockphoto.com/photos/cancun-beach-with-hotels-and-plam-tree-in-foreground-picture-id1165435852?k=20&m=1165435852&s=612x612&w=0&h=l8QeG-XeHOe18Ndqycp4nVutP_tXxsv-P2VNTtuTgIY=",
        "alt_image": "An image of a Cancun beach with views of the blue sea and jetskis on the water.",
        "map_link": "https://goo.gl/maps/Z88xizAZDj8yU49m8",
        "facts": "Cancún, a Mexican city on the Yucatán Peninsula bordering the Caribbean Sea, is known for its beaches, numerous resorts and nightlife. It's composed of 2 distinct areas: the more traditional downtown area, El Centro, and Zona Hotelera, a long, beachfront strip of high-rise hotels, nightclubs, shops and restaurants. Cancun is also a famed destination for students during universities' spring break period.",
        "things_to_do": ["Water Sports", "Isla Mujeres", "Dance at Coco Bongo Cancun",  "Chichén Itzá"],
        "hotels": ["The Ritz Carlton", "Le Blanc Spa Resort",  "Excellence Playa Mujeres"],
        "restaurants": ["Divina Carne", "Restaurante Careyes", "Umiami"],
        "temperature": "79",
        "currency": "Mexican Peso",
        "travel_requirements": ["Passport needed",  "Visa on arrival"],
        "destination_type": "Beach",
        "famous_for": ["Dancing", "Water Sports"],
        "more_like_this": ["Cabo San Lucas", "Playa Del Carmen"],
        "alt_facts": "What happens in Cancun, stays in Cancun."
    
    },

    {
        "id": "2",
        "rank": "2",
        "city": "Miami Beach",
        "country": "USA",
        "image":"https://www.worldatlas.com/upload/df/29/12/shutterstock-490898872.jpg",
        "alt_image": "A bird's eye view of Miami Beach city with its jet blue water.",
        "map_link": "https://goo.gl/maps/V2YsXVvgXQFefxc2A",
        "facts": "Miami Beach is a south Florida island city, connected by bridges to mainland Miami. Wide beaches stretch from North Shore Open Space Park, past palm-lined Lummus Park to South Pointe Park. The southern end, South Beach, is known for its international cachet with models and celebrities, and its early-20th-century architecture in the Art Deco Historic district with pastel-colored buildings, especially on Ocean Drive.",
        "things_to_do": ["South Beach", "Ocean Drive", "Haulover Park"],
        "hotels": ["Acqualina Resort & Residences on the Beach", "The Setai, Miami Beach", "Faena Hotel, Miami Beach"],
        "restaurants": ["Havana Vieja South Beach", "Pane & Vino", "Mama's Tacos"],
        "temperature": "65",
        "currency": "US Dollar",
        "travel_requirements": [],
        "destination_type": "Beach",
        "famous_for": ["Aesthetic Drives", "Parks"],
        "more_like_this": ["Panama City Beach", "Montego Bay"]
    },

    {
        "id": "3",
        "rank": "3",
        "city": "South Padre Island",
        "country": "USA",
        "image":"https://travel.home.sndimg.com/content/dam/images/travel/fullrights/2016/01/06/south-padre-island-the-pearl.jpg.rend.hgtvcom.1280.960.suffix/1491593016222.jpeg",
        "alt_image": "An image of South padre Island displaying its beautiful Palm trees.",
        "map_link": "https://goo.gl/maps/zu99DkuFTbXJ3hai8",
        "facts": "Every March, like clockwork, students cram into cars and head to South Padre Island for spring break fun in the sun and 24-hour beach bashes. While the island is still home to spring breakers for just over a month, the area has seen a rebirth of sorts as a popular family vacation destination. That's because South Padre, or SPI, delivers with wide sandy beaches, sparkling blue water and a mixture of fun activities for kids of all ages.",
        "things_to_do": ["Laguna Madre Nature Trail", "Sea Turtle, Inc.", "Isla Blanca Park"],
        "hotels": ["Hilton Garden Inn South Padre Island Beachfront", "Isla Grand Beach Resort", "Pearl South Padre"],
        "restaurants": ["Bar Louie", "Seviche Seviche"],
        "temperature": "65",
        "currency": "US Dollar",
        "travel_requirements": [],
        "destination_type": "Beach",
        "famous_for": ["Trails", "Parks"],
        "more_like_this": ["Miami Beach", "Punta Cana"]
    },

    {
        "id": "4",
        "rank": "4",
        "city": "Cabo San Lucas",
        "country": "Mexico",
        "image":"https://www.planetware.com/wpimages/2018/09/mexico-cabo-san-lucas-things-to-do-sunset-lands-end.jpg",
        "alt_image": "An image of Cabo's El Arco that displays the famous stone archways in the water.",
        "map_link": "https://goo.gl/maps/sY69PUBMosHGSRSk6",
        "facts": "Cabo San Lucas, a resort city on the southern tip of Mexico’s Baja California peninsula, is known for its beaches, water-based activities and nightlife. Playa El Médano is Cabo’s main beach, with outdoor restaurants and numerous bars. Past the marina is Land's End promontory, site of Playa del Amor (Lover's Beach) and El Arco, a natural archway in the seacliffs.",
        "things_to_do": ["Diving & Snorkeling", "Boat Tours"],
        "hotels": ["Montage Los Cabos", "Esperanza, Auberge Resorts Collection", "Las Ventanas al Paraiso, A Rosewood Resort"],
        "restaurants": ["Carbon Grill Restaurant", "La Casona", "Metate Cabo", "Mamazzita Cabo"],
        "temperature": "57",
        "currency": "Mexican Peso",
        "travel_requirements": ["Passport needed",  "Visa on arrival"],
        "destination_type": "Beach",
        "famous_for": ["Water Sports", "Boat Tours"],
        "more_like_this": ["Nassau", "Cancun"]
    },

    {
        "id": "5",
        "rank": "5",
        "city": "Montego Bay",
        "country": "Jamaica",
        "image":"https://cdn.travelpulse.com/images/b8aaedf4-a957-df11-b491-006073e71405/cf5cc01e-1d87-4148-81fa-ebfa8277626f/630x355.jpg",
        "alt_image": "An image of Montego's natural waterfalls.",
        "map_link": "https://goo.gl/maps/7TzrUcEuh1GSTyk69",
        "facts": "Montego Bay, the capital of Saint James Parish on Jamaica’s north coast, is a major cruise ship port with numerous beach resorts and golf courses outside its commercial core. Popular beaches include Doctor’s Cave Beach and Walter Fletcher Beach, home to an amusement park. There’s also snorkelling and diving at coral reefs in the protected waters of Montego Bay Marine Park.",
        "things_to_do": ["Dunn's River Falls and Park (Ocho Rios)", "Seven Mile Beach (Negril)"],
        "hotels": ["Round Hill Hotel and Villas", "Tensing Pen Resort"],
        "restaurants": ["Juici Patties"],
        "temperature": "70",
        "currency": "Jamaican Dollar",
        "travel_requirements": ["Passport needed", "Visa on arrival", "Sufficient funds certificate"],
        "destination_type": "Beach",
        "famous_for": ["Parks", "Aesthetic Drives"],
        "more_like_this": ["Miami Beach", "Panama City Beach"]

    },

    {
        "id": "6",
        "rank": "6",
        "city": "Nassau",
        "country": "Bahamas",
        "image":"https://e291f1206726d700191b-d0cedd1cc05016668dc83bc2742129e5.ssl.cf1.rackcdn.com/windsong/media/bmto-hero-img-5fda3f136b00c.jpg",
        "alt_image": "An image of the sparkling blue crystal waters of Nassau.",
        "map_link": "https://goo.gl/maps/FMxSQvyoYvQ4P5k8A",
        "facts": "Nassau is the capital of the Bahamas. It lies on the island of New Providence, with neighboring Paradise Island accessible via Nassau Harbor bridges. A popular cruise-ship stop, the city has a hilly landscape and is known for beaches as well as its offshore coral reefs, popular for diving and snorkeling. It retains many of its typical pastel-colored British colonial buildings, like the pink-hued Government House.",
        "things_to_do": ["Diving & Snorkeling", "Boat Tours"],
        "hotels": ["Kamalame Cay", "Rosewood Baha Mar", "Grand Hyatt Baha Mar"],
        "restaurants": ["La Caverna", "Louis & Steen's Market Orleans"],
        "temperature": "65",
        "currency": "Bahamian Dollar",
        "travel_requirements": ["Passport needed", "Valid return date"],
        "destination_type": "Beach",
        "famous_for": ["Casinos", "Water Sports", "Boat Tours"],
        "more_like_this": ["Daytona Beach", "Panama City Beach"],
        "alt_facts": "It is indeed better in the Bahamas."
    },

    {
        "id": "7",
        "rank": "7",
        "city": "Punta Cana",
        "country": "Dominican Republic",
        "image":"https://dynamic-media-cdn.tripadvisor.com/media/photo-o/12/f4/14/08/beach-overview.jpg?w=900&h=-1&s=1",
        "alt_image": "An image of Punta Cana with its crystal waters and larger than life coconut trees.",
        "map_link": "https://goo.gl/maps/dD8Au235R6SiCQSt7",
        "facts": "Punta Cana, the easternmost tip of the Dominican Republic, abuts the Caribbean Sea and the Atlantic Ocean. It's a region known for its 32km stretch of beaches and clear waters. The Bávaro area and Punta Cana combine to form what's known as La Costa del Coco, or the Coconut Coast, an area of lavish, all-inclusive resorts. It's popular for zip-lining, windsurfing, kayaking and sailing.",
        "things_to_do": ["Golf", "Altos de Chavón"],
        "hotels": ["Eden Roc at Cap Cana", "Tortuga Bay Hotel", "Casa de Campo Resort & Villas"],
        "restaurants": ["Montserrat Manor Restaurant", "Castaways Restaurant And Bar", "Chic Cabaret & Restaurant Punta Cana"],
        "temperature": "73",
        "currency": "Dominican Peso",
        "travel_requirements": ["Passport needed", "Visa required if stay exceeds 30 days"],
        "destination_type": "Beach",
        "famous_for": ["Architectural Sites"],
        "more_like_this": ["Montego Bay",  "South Padre Island"]
    },

    {
        "id": "8",
        "rank": "8",
        "city": "Playa del Carmen",
        "country": "Mexico",
        "image":"https://www.cataloniahotels.com/en/blog/wp-content/uploads/2019/07/cancun-luces.jpg",
        "alt_image": "An image showing Playa Del Carmen's glistening city surrounded by crystal blue water.",
        "map_link": "https://goo.gl/maps/S3zRDMw5RncsdEze6",
        "facts": "Playa del Carmen is a coastal resort town in Mexico, along the Yucatán Peninsula's Riviera Maya strip of Caribbean shoreline. In the state of Quintana Roo, it’s known for its palm-lined beaches and coral reefs. Its Quinta Avenida pedestrian thoroughfare runs parallel to the beach, with blocks of shops, restaurants and nightspots ranging from laid-back bars to dance clubs.",
        "things_to_do": ["La Quinta Avenida", "Snorkeling and Scuba Diving"],
        "hotels": ["Eden Roc at Cap Cana", "Tortuga Bay Hotel", "Casa de Campo Resort & Villas"],
        "restaurants": ["Montserrat Manor Restaurant", "Castaways Restaurant And Bar", "Chic Cabaret & Restaurant Punta Cana"],
        "temperature": "73",
        "currency": "Dominican Peso",
        "travel_requirements": ["Passport needed", "Visa required if stay exceeds 30 days"],
        "destination_type": "Beach",
        "famous_for": ["Water Sports", "Dancing"],
        "more_like_this": ["Cabo San Lucas", "Cancun"]
    },

    {
        "id": "9",
        "rank": "9",
        "city": "Daytona Beach",
        "country": "USA",
        "image":"https://assets.simpleviewinc.com/simpleview/image/upload/c_limit,h_1200,q_75,w_1200/v1/clients/daytonabeach/Beach_Aeriel_cx_af61e1fd-615c-4c57-8011-9689d196ae6b.jpg",
        "alt_image": "An image of Daytona's famous city on the coast of the Atlantc Ocean.",
        "map_link": "https://goo.gl/maps/c4LZUzhNFHYUWg9T6",
        "facts": "Daytona Beach is a city on Florida’s Atlantic coast. It’s known for Daytona International Speedway, which hosts February’s iconic Daytona 500 NASCAR race. The beach has hard-packed sand where driving is permitted in designated areas. Near the boardwalk’s rides and arcades, Daytona Beach Bandshell stages free summer concerts. Steps from the beach, Daytona Lagoon water park offers go-karts, laser tag and waterslides.",
        "things_to_do": ["Ponce de Leon Inlet Lighthouse & Museum", "Daytona International Speedway"],
        "hotels": ["The Shores Resort & Spa", "Delta Hotels by Marriott Daytona Beach", "Catalina Beach Club"],
        "restaurants": ["Daytona Brickyard"],
        "temperature": "56",
        "currency": "US Dollar",
        "travel_requirements": [],
        "destination_type": "Beach",
        "famous_for": ["Museums", "Aesthetic Drives", "Casinos"],
        "more_like_this": ["Panama City Beach", "Montego Bay"]
    },

    {
        "id": "10",
        "rank": "10",
        "city": "Park City",
        "country": "USA",
        "image":"https://i0.wp.com/popoversandpassports.com/wp-content/uploads/2021/03/img_6964.jpg?resize=1024%2C768&ssl=1",
        "alt_image": "An image of the famous park city ski slopes that attract tourists every year.",
        "map_link": "https://goo.gl/maps/4b9QJb64zk9Bqgub7",
        "facts": "Park City lies east of Salt Lake City in the western state of Utah. Framed by the craggy Wasatch Range, it’s bordered by the Deer Valley Resort and the huge Park City Mountain Resort, both known for their ski slopes. Utah Olympic Park, to the north, hosted the 2002 Winter Olympics and is now predominantly a training facility. In town, Main Street is lined with buildings built during a 19th-century silver mining boom.",
        "things_to_do": ["Skiing", "Snowboarding", "Hiking"],
        "hotels": ["Deer Valley Resort", "Park City Mountain Resort"],
        "restaurants": ["Butchers Chop House & Bar", "Firewood", "Grappa"],
        "temperature": "45",
        "currency": "US Dollar",
        "travel_requirements": [],
        "destination_type": "Mountain",
        "famous_for": ["Snow Sports", "Trails"],
        "more_like_this": ["Whistler"]
    },

    {
        "id": "11",
        "rank": "11",
        "city": "Panama City Beach",
        "country": "USA",
        "image":"https://digital.ihg.com/is/image/ihg/holiday-inn-resort-panama-city-beach-6482208681-4x3",
        "alt_image": "An image of Panama city's famous casinos with a view of their gliterring coastline.",
        "map_link": "https://goo.gl/maps/X4ciYu6Sz69kg7op8",
        "facts": "Panama City Beach is a waterfront town and vacation destination in northwest Florida. It's known for miles of white-sand beaches fronting the calm, clear waters of the Gulf of Mexico. St. Andrews State Park, one of 2 protected nature preserves nearby, is bordered by the Gulf and has hiking trails and fishing piers. Pier Park is the main shopping hub and a venue for major events.",
        "things_to_do": ["Dolphin Tours"],
        "hotels": ["The Pearl Hotel", "Holiday Inn Resort Panama City Beach", "Marriott's Legends Edge at Bay Point"],
        "restaurants": ["Paula Deen's Family Kitchen", "Gypsea Crepes"],
        "temperature": "56",
        "currency": "US Dollar",
        "travel_requirements": [],
        "destination_type": "Beach",
        "famous_for": ["Shopping", "Casinos"],
        "more_like_this": ["Miami Beach", "Daytona Beach"]
    },

    {
        "id": "12",
        "rank": "12",
        "city": "Whistler",
        "country": "Canada",
        "image":"https://content.r9cdn.net/rimg/dimg/50/83/9f442efc-city-40386-1629b6be43d.jpg?crop=true&width=1366&height=768&xhint=1688&yhint=1177",
        "alt_image": "An image of Whistler's beaming ski resorts that make it a perfect snowy spring getaway.",
        "map_link": "https://goo.gl/maps/2URGSReycJc23Gja6",
        "facts": "Whistler is a town north of Vancouver, British Columbia, that's home to Whistler Blackcomb, one of the largest ski resorts in North America. Besides skiing and snowboarding, the area offers snowshoeing, tobogganing and ski jumping at the Olympic Park, a venue for the 2010 Vancouver Winter Olympics. The hub of Whistler is a compact, chalet-style pedestrian village at the base of Whistler and Blackcomb mountains.",
        "things_to_do": ["Skiing", "Snowboarding", "Shopping"],
        "hotels": ["Four Seasons Resort", "Fairmont Chateau"],
        "restaurants": ["II Caminetto", "Araxi"],
        "temperature": "48",
        "currency": "Canadian Dollar",
        "travel_requirements": ["Passport needed"],
        "destination_type": "Mountain",
        "famous_for": ["Snow Sports", "Shopping"],
        "more_like_this": ["Park City"],
        "alt_facts": "Breathe the clean, fresh air and ski a little."
    }

]

# ROUTES

@app.route('/')
def home_page():
   return render_template('home_page.html', cities = cities)   


@app.route('/view/<id>')
def view( id = None ):

    global cities

    city = None

    for i in range(len(cities)):

        if cities[i]["id"] == id:

            city = cities[i]

    return render_template('view.html', id = id, city = city) 



@app.route('/search_results/<search_term>')
def search_results( search_term = None):

    global cities

    lower_search_term = search_term.lower()

    search_city_result = []
    search_country_result = []
    search_type_result = []

    search_city_result_number = 0
    search_country_result_number = 0
    search_type_result_number = 0

    for c in cities:

        if c["city"].lower().find(lower_search_term) != -1:
            
            search_city_result.append(c)
            search_city_result_number = search_city_result_number + 1

        if c["country"].lower().find(lower_search_term) != -1:
            
            search_country_result.append(c)
            search_country_result_number = search_country_result_number + 1

        if c["destination_type"].lower().find(lower_search_term) != -1:
            
            search_type_result.append(c)
            search_type_result_number = search_type_result_number + 1


    return render_template('search_display.html', search_term = search_term, search_city_result = search_city_result, search_city_result_number = search_city_result_number, search_country_result = search_country_result, search_country_result_number = search_country_result_number, search_type_result = search_type_result, search_type_result_number = search_type_result_number)


@app.route('/add')
def add_data():
    return render_template('add.html')


@app.route('/save_data', methods = ['POST', 'GET'])
def save_data():

    global cities
    global current_id

    json_data = request.get_json()

    current_id = current_id + 1
    new_city = { 
        "id": current_id,
        "rank": json_data['rank'],
        "city": json_data['city'],
        "country": json_data['country'],
        "image": json_data['image'],
        "map_link": json_data['map_link'],
        "facts": json_data['facts'],
        "things_to_do": json_data['things_to_do'],
        "hotels": json_data['hotels'],
        "restaurants": json_data['restaurants'],
        "temperature": json_data['temperature'],
        "currency": json_data['currency'],
        "travel_requirements": json_data['travel_requirements'],
        "destination_type": json_data["destination_type"],
        "famous_for": json_data["famous_for"],
        "more_like_this": json_data["more_like_this"]
    }

    print(new_city)

    cities.insert(len(cities), new_city)

    print(cities)

    return jsonify(current_id)

@app.route('/edit/<id>')
def edit( id = None ):

    global cities

    city = None

    for i in range(len(cities)):

        if cities[i]["id"] == id:

            city = cities[i]

    return render_template('edit.html', id = id, city = city) 


@app.route('/edit_data', methods = ['POST', 'GET'])
def edit_data():

    global cities

    json_data = request.get_json()

    edit_id = json_data["id"]
    edit_city = json_data["city"]
    edit_country = json_data["country"]
    edit_rank = json_data["rank"]
    edit_image = json_data["image"]
    edit_map = json_data["map_link"]
    edit_facts = json_data["facts"]
    edit_things= json_data["things_to_do"]
    edit_hotels = json_data["hotels"]
    edit_restaurants = json_data["restaurants"]
    edit_temperature = json_data["temperature"]
    edit_currency = json_data[ "currency"]
    edit_requirements = json_data["travel_requirements"]
    edit_type = json_data["destination_type"]
    edit_famous = json_data["famous_for"]
    edit_more = json_data["more_like_this"]

    for i in range(len(cities)):

        if cities[i]["id"] == edit_id:

            cities[i]["city"] = edit_city
            cities[i]["country"] = edit_country
            cities[i]["rank"] = edit_rank
            cities[i]["image"] = edit_image
            cities[i]["map_link"] = edit_map
            cities[i]["facts"] = edit_facts
            cities[i]["things_to_do"] = edit_things
            cities[i]["hotels"] = edit_hotels
            cities[i]["restaurants"] = edit_restaurants
            cities[i]["temperature"] = edit_temperature
            cities[i]["currency"] = edit_currency
            cities[i]["travel_requirements"] = edit_requirements
            cities[i]["destination_type"] = edit_type
            cities[i]["famous_for"] = edit_famous
            cities[i]["more_like_this"] = edit_more
            print(cities[11])

    edited_city = None


    return jsonify(edited_city)


if __name__ == '__main__':
   app.run(debug = True)




