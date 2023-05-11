<script>$(document).ready(function() {
  $('#add-special-form, #add-technician-form, #edit-special-form, #edit-technician-form').on('submit', function(e) {
    e.preventDefault();
    var form = $(this);
    var message;
    var formType = form.data('form-type');
    if (formType == "specialA") {
      message = $('#messageAS').val();
    } else if (formType == "technicianA") {
      message = $('#messageAT').val();
    }
    else if (formType == "specialE") {
      message = $('#messageES').val();
    } else if (formType == "technicianE") {
      message = $('#messageET').val();
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
          text: 'Une erreur est survenue lors de l\'enregistrement de la spécialité.',
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
