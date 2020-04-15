var bugs = JSON.parse(bugs)
var fish = JSON.parse(fish)
var d = new Date();

console.log(getAvailable())

function getAvailable(){  
  var month = d.getMonth() + 1
  month = month + ""; 
  var hour = d.getHours() + ""

  var availCritters = {
    fish:[],
    bugs:[]
  };

  for (i = 0; i < bugs.length; i++) {
    if(bugs[i]["time"][hour] == 1 && bugs[i]["months"][month] == 1){
      availCritters["bugs"].push(bugs[i])
    }
  }

  for (i = 0; i < fish.length; i++) {
    if(fish[i]["time"][hour] == 1 && fish[i]["months"][month] == 1){
      availCritters["fish"].push(fish[i])
    }
  }
  return availCritters
}