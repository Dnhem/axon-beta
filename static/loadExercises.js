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
    "upper legs": [
      { name: "barbell squat" },
      { name: "lunge" },
      { name: "rear elevated foot squat" },
      { name: "walking lunges" },
      { name: "reverse lunge" },
      { name: "barbell hip thruster" },
      { name: "glute bridge" },
      { name: "leg extension" },
      { name: "step up" },
      { name: "plyo squat" },
      { name: "box jump" },
    ],
    back: [
      { name: "lat pull-down" },
      { name: "dumbbell row" },
      { name: "seated cable row" },
      { name: "barbell row" },
      { name: "landmine row" },
      { name: "inverted row" },
      { name: "pull-up" },
      { name: "deadlift" },
      { name: "rack pull" },
      { name: "kettle bell row" },
    ],
    chest: [
      { name: "dumbbell bench press" },
      { name: "dumbbell flies" },
      { name: "dumbell incline bench press" },
      { name: "cable fly" },
      { name: "push up" },
      { name: "incline push up" },
      { name: "close grip bench press" },
      { name: "neutral grip dumbbell press" },
      { name: "incline barbell bench press" },
      { name: "decline push up" },
    ],
  };
  populateDropDown(results[bodyPart], dropDown);
}

// Generate dropdown menu for each body part on page load
getExercises("lower legs", "lower-leg-select");
getExercises("upper legs", "upper-leg-select");
getExercises("back", "back-select");
getExercises("chest", "chest-select");
