/**
 * Deletes a note with the specified noteId.
 * @param {number} noteId - The ID of the note to be deleted.
 */
function deleteNote(noteId) {
  // Send a POST request to the "/delete-note" endpoint
  fetch("/delete-note", {
    method: "POST", // Use the POST method
    body: JSON.stringify({ noteId: noteId }), // Convert the noteId to JSON format and send it in the request body
  }).then((_res) => { // When the request is completed
    // Redirect the user to the home page
    window.location.href = "/";
  });
}
