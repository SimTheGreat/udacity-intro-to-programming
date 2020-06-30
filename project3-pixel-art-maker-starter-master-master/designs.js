//all the variable definitions
const color = document.getElementById("colorPicker");
const gridSize = document.getElementById("sizePicker");
const gridHeight = document.getElementById("inputHeight");
const gridWidth = document.getElementById("inputWidth");
const designCanvas = document.getElementById("pixelCanvas");
//creates a grid after the users spessifications
document.addEventListener('submit', (event) => {
    event.preventDefault();
    height = (inputHeight.value);
    width = (inputWidth.value);
    designCanvas.innerHTML = "";
    makeGrid(height, width);
})


function makeGrid(height, width) {
    for(let h = 0; h < height; h++) {
        let row = designCanvas.insertRow(h);//creates a row until the for loop is true
        for(let w = 0; w < width; w++) {
            let cell = row.insertCell(w);//creates a col until the for loop is true
            cell.addEventListener('click', (event) => {
                event.target.style.backgroundColor = color.value;
                designCanvas.addEventListener('dblclick', (event) => { //doubleclick sets the cell color back to white
                    event.target.style.backgroundColor = ''
                });
            })
        }
    }
}
