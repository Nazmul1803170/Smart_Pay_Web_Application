//getUserInfo(index) --> struct user
//getTripInfo(id) --> struct trip

// bus_id=<>&&id=<>&&status=<>&&lat=<>&&lon=<>
String postDataMakerStart(trip currentTrip, String id, String bus_id){
  String data;
  location currentLocation;// = getLocation();

  currentLocation.lat = 20.20;
  currentLocation.lon = 40.40;
  data = "bus_id="+bus_id+"&&id="+id+"&&status="+currentTrip.status+"&&lat="+(String)currentLocation.lat+"&&lon="+(String)currentLocation.lon;

  return data;
}

// bus_id=<>&&id=<>&&status=<>&&lat=<>&&lon=<>+&&distance=<>
String postDataMakerEnd(trip currentTrip, String id, String bus_id, location startLoc){
  String data;
  location currentLocation;// = getLocation();

  currentLocation.lat = 20.80;
  currentLocation.lon = 40.80;
  //float distance = getDistance(startLoc,currentLocation);
  int distance = 12;

  showText("Distance: "+ (String)distance + "km",2,5,5);

  data = "bus_id="+bus_id+"&&id="+id+"&&status="+currentTrip.status+"&&lat="+(String)currentLocation.lat+"&&lon="+(String)currentLocation.lon+"&&distance="+distance;

  return data;
}

void postLocation(String id, String bus_id){
  
  trip currentTrip = getTripInfo(id);
  if (currentTrip.status == "start"){
    showText("Start Trip",2,0,0);
    String payload = httpPost(tripping,postDataMakerStart(currentTrip,id,bus_id));
    Serial.println(payload);
  }
  else if(currentTrip.status == "end"){
    showText("End Trip",2,0,0);
    location startLoc;
    startLoc.lat = currentTrip.lat;
    startLoc.lon = currentTrip.lon;
    String payload = httpPost(tripping,postDataMakerEnd(currentTrip,id,bus_id,startLoc));
    Serial.println(payload);
  }
}

//contact=<>&&id=<>
void postCard(String contact, String id){
  String postdata = "contact="+contact+"&&id="+id;
  String payload = httpPost(addcard,postdata);
  Serial.println(payload);
}

void addUserCard(){
  user info = getUserInfo(2);
  postCard(info.contact, "1803133");
}