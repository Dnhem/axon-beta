// Helper function to populate a dropdown item for each exercise
function populateDropDown(bodyPart, dropDown) {
  console.log(bodyPart);
  let dropDownList = document.querySelector(`#${dropDown}`);
  let defaultOption = document.createElement("option");
  defaultOption.text = "Select Exercise";
  dropDownList.add(defaultOption);
  dropDownList.selectedIndex = 0;
  let option;
  for (let i = 0; i < bodyPart.length; i++) {
    option = document.createElement("option");
    option.text = bodyPart[i].name;
    option.value = bodyPart[i].name;
    dropDownList.add(option);
  }
}

// Two Part Function:
// 1) API Call to retrieve all exercises for each individual body part
// 2) calls populateDropDown function
async function getExercises(bodyPart, dropDown) {
  const options = {
    method: "GET",
    url: `http://localhost:5000/exercises/bodyPart/${bodyPart}`,
  };
  await axios
    .request(options)
    .then(function(exercises) {
      // Mock data, API monthly quota exceeded
      let results = {
        "lower legs": [ { name: "calf raises" }, { name: "peroneal stretch" } ],
        "upper legs": [ { name: "squats" }, { name: "lunge" } ],
        back: [ { name: "lat pull-down" }, { name: "dumbbell row" } ],
        chest: [ { name: "bench press" }, { name: "dumbbell flies" } ],
      };
      console.log(results);
      console.log(bodyPart);
      // TODO: Uncomment line 39 and comment line 40 to make remote api call
      // populateDropDown(exercises.data, dropDown);
      populateDropDown(results[bodyPart], dropDown);
    })
    .catch(function(error) {
      console.error(error);
    });
}

// Generate dropdown menu for each body part on page load
getExercises("lower legs", "lower-leg-select");
getExercises("upper legs", "upper-leg-select");
getExercises("back", "back-select");
getExercises("chest", "chest-select");
