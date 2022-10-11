// Helper function to populate a dropdown item for each exercise
function populateDropDown(bodyPart, dropDown) {
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
  // TODO: Uncomment to make remote API call
  // try {
  //   const exercises = await axios({
  //     url: `http://localhost:5000/exercises/bodyPart/${bodyPart}`,
  //     method: "GET",
  //   });
  //   populateDropDown(exercises.data, dropDown);
  // } catch (err) {
  //   console.log(err);
  // }

  // Mock data, API monthly quota exceeded
  let results = {
    "lower legs": [ { name: "calf raises" }, { name: "peroneal stretch" } ],
    "upper legs": [ { name: "squats" }, { name: "lunge" } ],
    back: [ { name: "lat pull-down" }, { name: "dumbbell row" } ],
    chest: [ { name: "bench press" }, { name: "dumbbell flies" } ],
  };
  populateDropDown(results[bodyPart], dropDown);
}

// Generate dropdown menu for each body part on page load
getExercises("lower legs", "lower-leg-select");
getExercises("upper legs", "upper-leg-select");
getExercises("back", "back-select");
getExercises("chest", "chest-select");
