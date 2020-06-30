var colorPicker = document.getElementById("colorPicker").value;
var sizePicker = document.getElementById("sizePicker");
var canvas = document.getElementById("pixelCanvas");
var height = document.getElementById('inputHeight').value;
var width = document.getElementById('inputWidth').value;

makeGrid(height, width);
sizePicker.addEventListener('click', function(event) {
  event.preventDefault();
  var height = document.getElementById('inputHeight').value;
  var width = document.getElementById('inputWidth').value;


  makeGrid(height, width);
})
function makeGrid(height, width) {
  var height = document.getElementById('inputHeight').value;
  var width = document.getElementById('inputWidth').value;
  let rows = document.createElement("tr");
  let cells = document.createElement("td");

//  document.createElement('table');
  for (var x = 1; x < height; x++) {
    //document.table.appendChild('tr');
    canvas.appendChild(cells);
  for (var y = 1; y < width; y++) {
    //document.table.appendChild('td');
    canvas.appendChild(rows);
  cell.addEventListener('mousedown', function(event) {
      var color = colorPicker.value;
      color = event.target.style.backgroundColor;
      });
    }
  }
}
