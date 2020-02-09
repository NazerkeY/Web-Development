var close = document.getElementsByClassName("todo-trash");

function del(){
for (let i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var prev = this.parentElement;
  //  prev.style.display = "none";
  prev.remove();
  }
}
}
del();

let list = document.querySelector('ul');
list.addEventListener('click', function(item) {
  if (item.target.tagName === 'LI') {
    item.target.classList.toggle('checked');
  }
}, false);

function newElement() {
  let li = document.createElement("li");
  let inputValue = document.getElementById("myInput").value;
  let t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("my-list").appendChild(li);
  }
  document.getElementById("myInput").value = "";

  let span = document.createElement("SPAN");
  let txt = document.createTextNode("X");
  span.className = "todo-trash";
  span.appendChild(txt);
  li.appendChild(span);
  del();
  console.log(document.getElementById("my-list"));
}