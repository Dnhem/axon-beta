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
  const options = {
    method: "GET",
    url: `http://localhost:5000/exercises/bodyPart/${bodyPart}`,
  };
  await axios
    .request(options)
    .then(function(exercises) {
      populateDropDown(exercises.data, dropDown);
    })
    .catch(function(error) {
      console.error(error);
    });
}

// Generate dropdown menu for each body part on page load
getExercises("lower%20legs", "lower-leg-select");
getExercises("upper%20legs", "upper-leg-select");
getExercises("back", "back-select");
getExercises("chest", "chest-select");
