document.addEventListener("DOMContentLoaded", function() {
    console.log("Document is ready");
  });

  function showModal(button) {
    console.log("showModal called");
    const buttonContent = button.textContent; // Usa textContent per ottenere il contenuto del bottone
    console.log("Button content:", buttonContent); // Log del contenuto del bottone
    document.getElementById('button-content').textContent = buttonContent; // Imposta il contenuto nel modal
    document.getElementById('my_modal').showModal(); // Mostra il modal
  }

  function closeModal() {
    console.log("closeModal called");
    document.getElementById('my_modal').close(); // Chiudi il modal
  }