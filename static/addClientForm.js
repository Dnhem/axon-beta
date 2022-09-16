// Button handlers for trainer page
const addClient = document.querySelector("#add-client-btn");
const modalForm = document.querySelector(".modal-form");
const btnCancel = document.querySelector(".btn-cancel");
const btnSave = document.querySelector(".btn-save");
const formInput = document.querySelector(".form-input");

addClient.addEventListener("click", () => {
  modalForm.classList.add("visible");
});

btnCancel.addEventListener("click", e => {
  e.preventDefault();
  formInput.reset();
  modalForm.classList.remove("visible");
});

btnSave.addEventListener("click", e => {
  modalForm.classList.add("visible");
});
