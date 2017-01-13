// Find delete button, add on click listener.

buttons = document.getElementsByClassName('delete_book');

for ( b = 0 ; b < buttons.length ; b++) {
  buttons[b].addEventListener('click', deleteBook);
}

function deleteBook() {

  console.log('delete book runs.... ')

  if (confirm('Delete book: are you sure?')) {

    var book_id = this.value

    //AJAX request
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 204) {
        // remove div with book in
        console.log('ajax callback SRTVSERTSVEBT')
        delete_div = document.getElementById(book_id);
        delete_div.parentNode.removeChild(delete_div);
      }
    }

    xhttp.open('DELETE', '/book/' + book_id, true);
    xhttp.send();

  }

}
