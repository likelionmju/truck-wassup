let typing = document.getElementById('typing');

let typewriter = new Typewriter(typing, {
  loop: true
});

typewriter.typeString('Truck Wassup!')
  .pauseFor(2500)
  .deleteAll()
  .typeString('당신을 위한 푸드트럭')
  .pauseFor(2500)
  .deleteAll()
  .start();
