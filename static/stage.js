// El personaje entra caminando, lanza el hechizo y queda con el orbe activo.
// Clic, Enter o espacio sobre él: vuelve a lanzarlo. Diálogo: clic para avanzar.
(function () {
  var hero = document.querySelector(".hero");
  var stage = document.querySelector(".stage");
  if (!hero || !stage) return;
  var still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var mp = stage.querySelector(".hp");
  var timer = null;

  function frameW() { return hero.clientWidth; }
  function show(i) { hero.style.backgroundPosition = (-i * frameW()) + "px 0"; }
  function target() { return stage.clientWidth < 600 ? 12 : stage.clientWidth * 0.5 - frameW() * 1.55; }
  function setX(x) { hero.style.setProperty("--x", x + "px"); }

  function cast() {
    clearInterval(timer);
    hero.classList.add("casting");
    var i = 0, loop = 0;
    if (mp) mp.style.setProperty("--mp", "35%");
    timer = setInterval(function () {
      show(i);
      if (i < 7) { i++; return; }
      if (mp) mp.style.setProperty("--mp", "100%");
      i = 5 + (loop++ % 3);   // el orbe sigue latiendo con los tres últimos fotogramas
    }, 120);
  }

  function walk() {
    var x0 = -frameW(), x = x0, end = target(), f = 0, last = 0, t0 = null;
    hero.classList.remove("casting");
    function step(t) {
      if (t0 === null) t0 = t;
      if (t - last > 95) { show(f = (f + 1) % 8); last = t; }
      x = x0 + (t - t0) * 0.16; setX(Math.min(x, end));   // velocidad fija en px/ms
      if (x < end) requestAnimationFrame(step); else cast();
    }
    requestAnimationFrame(step);
  }

  hero.addEventListener("click", cast);
  addEventListener("resize", function () { setX(target()); show(7); });
  if (still) { hero.classList.add("casting"); setX(target()); show(7); }
  else walk();

  var box = document.querySelector(".dialog");
  if (!box) return;
  var lines = box.querySelectorAll("p");
  var n = 0;
  for (var k = 1; k < lines.length; k++) lines[k].hidden = true;
  function next() {
    lines[n].hidden = true;
    n = (n + 1) % lines.length;
    lines[n].hidden = false;
  }
  box.tabIndex = 0;
  box.addEventListener("click", next);
  box.addEventListener("keydown", function (ev) {
    if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); next(); }
  });
})();
