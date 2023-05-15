<script>
$(document).ready(function() {
  $('#add-special-form, #add-technician-form, #edit-special-form, #edit-technician-form, #add-equipe-form').on('submit', function(e) {
    e.preventDefault();
    var form = $(this);
    var success_message = "Les informations ont été enregistrées avec succès !";
    var edit_message = "Les informations ont été modifiées avec succès ";
    var message;
    var formType = form.data('form-type');
    if (formType == "specialA" || formType == "technicianA" || formType == "equipeA") {
      message = success_message;
    }
    else if (formType == "specialE" ||  formType == "technicianE" ) {
      message = edit_message;
    }
    else{
    alert("There is some problem");
    }


    $.ajax({
      url: form.attr('action'),
      type: form.attr('method'),
      data: form.serialize(),
      success: function(response) {
        // Do nothing here
      },
      error: function(xhr, status, error) {
        Swal.fire({
          icon: 'error',
          title: 'Erreur!',
          text: 'La valeur est deja dans la base de données .',
          background: '#dc3545'
        });
      }
    }).then(function(response) {
      // Show the toastr notification
      toastr.success(message, 'Succès!', {
        closeButton: false,
        timeOut: 1000,
        extendedTimeOut: 0
      });

      // Hide all the modals after 1 second and reload the page
      setTimeout(function() {
        $('#add-special-modal, #add-technician-modal, #edit-special-modal, #edit-technician-modal').modal('hide');
        location.reload();
      }, 1000);
    });
  });
});

</script>
