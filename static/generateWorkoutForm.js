const exercisesList = document.querySelector(".exercises-list");
const errorMsg = document.querySelector(".error-message");

// Lower leg input section
const btnLowerLegExercise = document.querySelector("#lower-leg-exercise");
const lowerLegExercise = document.querySelector("#lower-leg-select");
const lowerLegSets = document.querySelector("#lower-leg-sets");
const lowerLegReps = document.querySelector("#lower-leg-reps");
const lowerLegWeight = document.querySelector("#lower-leg-weight");
const lowerLegRest = document.querySelector("#lower-leg-rest");
const lowerLegDuration = document.querySelector("#lower-leg-duration");

// Upper leg input section
const btnUpperLegExercise = document.querySelector("#upper-leg-exercise");
const upperLegExercise = document.querySelector("#upper-leg-select");
const upperLegSets = document.querySelector("#upper-leg-sets");
const upperLegReps = document.querySelector("#upper-leg-reps");
const upperLegWeight = document.querySelector("#upper-leg-weight");
const upperLegRest = document.querySelector("#upper-leg-rest");
const upperLegDuration = document.querySelector("#upper-leg-duration");

// Back input section
const btnBackExercise = document.querySelector("#back-exercise");
const backExercise = document.querySelector("#back-select");
const backSets = document.querySelector("#back-sets");
const backReps = document.querySelector("#back-reps");
const backWeight = document.querySelector("#back-weight");
const backRest = document.querySelector("#back-rest");
const backDuration = document.querySelector("#back-duration");

// Chest input section
const btnChestExercise = document.querySelector("#chest-exercise");
const chestExercise = document.querySelector("#chest-select");
const chestSets = document.querySelector("#chest-sets");
const chestReps = document.querySelector("#chest-reps");
const chestWeight = document.querySelector("#chest-weight");
const chestRest = document.querySelector("#chest-rest");
const chestDuration = document.querySelector("#chest-duration");

// Custom exercise input section
const btnCustomExercise = document.querySelector("#custom-exercise");
const customExercise = document.querySelector("#custom-exercise");
const customExerciseSets = document.querySelector("#custom-exercise-sets");
const customExerciseReps = document.querySelector("#custom-exercise-reps");
const customExerciseWeight = document.querySelector("#custom-exercise-weight");
const customExerciseRest = document.querySelector("#custom-exercise-rest");
const customExerciseDuration = document.querySelector(
  "#custom-exercise-duration"
);

//  Dynamically generate delete button to remove each row
const generateDeleteBtn = () => {
  const deleteBtn = document.createElement("button");
  deleteBtn.innerText = "X";
  deleteBtn.classList.add("remove-exercise");
  deleteBtn.addEventListener("click", e => {
    e.preventDefault();
    while (e.target.parentNode.firstChild) {
      e.target.parentNode.firstChild.remove();
    }
  });
  return deleteBtn;
};

// Label input name attributes uniformly
let rowCounter = 0;
const labelInputs = inputs => {
  for (let i = 0; i < inputs.length; i++) {
    inputs[0].setAttribute("name", "name-" + rowCounter);
    inputs[1].setAttribute("name", "sets-" + rowCounter);
    inputs[2].setAttribute("name", "reps-" + rowCounter);
    inputs[3].setAttribute("name", "weight-" + rowCounter);
    inputs[4].setAttribute("name", "rest-" + rowCounter);
    inputs[5].setAttribute("name", "duration-" + rowCounter);
  }
  // add common class name for second to last inputs for design
  for (let i = 1; i < inputs.length; i++) {
    inputs[i].classList.add("acute-variables");
  }
};

// Create a table row element
// attach table cell elements to that row
// Append table row to page
const createTableRow = (
  cellOne,
  cellTwo,
  cellThree,
  cellFour,
  cellFive,
  cellSix
) => {
  const newRow = document.createElement("tr");
  newRow.classList.add("new-row");
  let cells = [ cellOne, cellTwo, cellThree, cellFour, cellFive, cellSix ];
  let inputElements = [];
  for (let i = 0; i < cells.length; i++) {
    let cell = document.createElement("td");
    let inputData = document.createElement("input");
    inputData.innerText = cells[i].value;
    inputData.value = cells[i].value;
    inputElements.push(inputData);
    cell.append(inputData);
    newRow.append(cell);
  }
  labelInputs(inputElements);
  newRow.append(generateDeleteBtn());
  exercisesList.append(newRow);
  rowCounter++;
};

// Validate form inputs
// call helper function createTableRow to insert exercise,sets,reps to into table
const addExerciseToTable = (exercise, sets, reps, weight, rest, duration) => {
  if (exercise.value === "Select Exercise" || exercise.value === "") {
    errorMsg.innerText = "Please SELECT an exercise";
    errorMsg.classList.add("error-msg");
    return;
  }
  createTableRow(exercise, sets, reps, weight, rest, duration);
  errorMsg.innerText = "";
};

// Click event for lower leg exercises
btnLowerLegExercise.addEventListener("click", e => {
  e.preventDefault();
  addExerciseToTable(
    lowerLegExercise,
    lowerLegSets,
    lowerLegReps,
    lowerLegWeight,
    lowerLegRest,
    lowerLegDuration
  );
});

// Click event for upper leg exercises
btnUpperLegExercise.addEventListener("click", e => {
  e.preventDefault();
  addExerciseToTable(
    upperLegExercise,
    upperLegSets,
    upperLegReps,
    upperLegWeight,
    upperLegRest,
    upperLegDuration
  );
});

// Click event for back exercises
btnBackExercise.addEventListener("click", e => {
  e.preventDefault();
  addExerciseToTable(
    backExercise,
    backSets,
    backReps,
    backWeight,
    backRest,
    backDuration
  );
});

// Click event for chest exercises
btnChestExercise.addEventListener("click", e => {
  e.preventDefault();
  addExerciseToTable(
    chestExercise,
    chestSets,
    chestReps,
    chestWeight,
    chestRest,
    chestDuration
  );
  // reset input fields
  chestSets.value = "";
  chestReps.value = "";
  chestWeight.value = "";
  chestRest.value = "";
  chestDuration.value = "";
});

// Click event for custom exercises
btnCustomExercise.addEventListener("click", e => {
  e.preventDefault();
  addExerciseToTable(
    customExercise,
    customExerciseSets,
    customExerciseReps,
    customExerciseWeight,
    customExerciseRest,
    customExerciseDuration
  );
  // reset input fields
  customExercise.value = "";
  customExerciseSets.value = "";
  customExerciseReps.value = "";
  customExerciseWeight.value = "";
  customExerciseRest.value = "";
  customExerciseDuration.value = "";
});
