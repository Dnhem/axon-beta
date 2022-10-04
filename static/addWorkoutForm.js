const btnAddWorkout = document.querySelector("#add-workout-btn");
const btnCloseForm = document.querySelector(".btn-close-workout-form");
const workoutForm = document.querySelector(".workout-form");

btnAddWorkout.addEventListener("click", () => {
  workoutForm.classList.add("show-form");
});

btnCloseForm.addEventListener("click", () => {
  workoutForm.classList.remove("show-form");
});
