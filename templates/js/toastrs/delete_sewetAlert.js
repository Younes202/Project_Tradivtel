<script>
function deleteItem(dataType, deleteUrl, itemId) {
  // Afficher une boîte de dialogue de confirmation à l'aide de SweetAlert
  Swal.fire({
    title: "Êtes-vous sûr(e) ?",
    text: "Vous ne pourrez pas revenir en arrière !",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Oui, supprimez-le !",
    cancelButtonText: "Non, annuler",
    reverseButtons: true,
  }).then((result) => {
    if (result.isConfirmed) {
      // L'utilisateur a cliqué sur le bouton "Oui, supprimez-le !"
      var csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
      fetch(deleteUrl, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
      })
        .then(response => {
          if (!response.ok) {
            throw new Error("La réponse réseau n'était pas correcte");
          }
          // Afficher un message de réussite
          Swal.fire({
            icon: "success",
            title: `${dataType} supprimé(e) avec succès`,
          }).then(() => {
            location.reload(); // Recharger la page pour mettre à jour la liste
          });
        })
        .catch(error => {
          console.error(`Une erreur s'est produite lors de la suppression de ${dataType} :`, error);
          // Afficher un message d'erreur
          Swal.fire({
            icon: "error",
            title: "Erreur",
            text: `Une erreur s'est produite lors de la suppression de ${dataType}.`,
          });
        });
    } else {
      // L'utilisateur a cliqué sur le bouton "Non, annuler" ou a fermé la boîte de dialogue
      return false;
    }
  });
}

// Sélectionner tous les boutons de suppression et attacher l'écouteur d'événement à chacun d'eux
var deleteButtons = document.querySelectorAll('.delete-item');
deleteButtons.forEach(function(deleteButton) {
  deleteButton.addEventListener('click', function() {
    var dataType = this.dataset.type;
    var deleteUrl = this.dataset.url;
    var itemId = this.dataset.id;
    deleteItem(dataType, deleteUrl, itemId);
  });
});
</script>
