let screenWidth = 1200;
let screenHeight = 600;
let waves = [];
let colors = [];
// let wave = [];
let time;
let maxN;
let slider;
const sliderMax = 50;

function setup() {
  createCanvas(screenWidth, screenHeight);
  
  circX = screenWidth / 4;
  circY = screenHeight / 2;
  circScale = 250;
  waveX = screenWidth * (2/4);
  // waveY = screenHeight / 2;
  time = 0.000;
  timeStep = 0.01;
  
  maxN = 11;
  
  for (i=0; i<=sliderMax; i++) {
    waves[i] = [];
    // colors[i] = color(random(255), random(255), random (255));
  }
  
  // Create a slider and place it at the top of the canvas.
  slider = createSlider(1, sliderMax);
  slider.position(10, height - 50);
  slider.size(300);
  slider.value(5);
  
}

function draw() {
  background(220);
  stroke(0,0,0,255);
  maxN = slider.value();
  
  time += timeStep;
  
  text("Time = " + time, 10, 30);
  text("maxN = " + maxN, 10, 50);
  // text("wave[] = " + wave, 10, 70);
  // text("wave.length = " + wave.length, 10, 90);
  
  // draw wave CS
  rad = circScale * (4 / (1 * PI));
  line(waveX, circY - rad, waveX, circY + rad);
  line(waveX - 50, circY, width, circY);
  
  // draw orbits
  x = circX;
  y = circY;
  for (let n = 1; n < maxN +1; n += 2) {
    prevX = x;
    prevY = y;
    rad = circScale * (4 / (n * PI));
    x += rad * cos(n*time)/2;
    y += -1 * rad * sin(n*time)/2;
    circle(prevX, prevY, rad);
    line(prevX, prevY, x, y);
    let w = (n+1) / 2;
    waves[w].splice(0,0,y);
    if ( waves[w].length > screenWidth) {
      waves[w].splice(waves[w].length - 1, 1);
    }
  }
  //circle(x, y, rad/PI);

  // check if waves.length is greater than slider value. If so, slider slid left and need to kill the extras?
  // TODO

  // Draw the waves
  for (u = 0; u < waves.length; u++) {
    // set alpha based on depth in array. Last entry is most visible
    alph = u / waves.length * 255 +1;
    stroke(0,0,0, alph);
    for (j = 0; j < waves[u].length; j++) {
      pX = waveX + j;
      pY = waves[u][j];
      circle(pX, pY, 1);
    }
  }
  
  
  
  // add y location of smallest circle to the wave
  // wave.splice(0, 0, y);
  // if (wave.length > 650) {
  //   let d = wave.length;
  //   wave.splice(d-1, 1);
  // }
  
//  for (let i = 0; i < wave.length; i++) {
//    pX = waveX + i;
//    pY = wave[i];
//    circle(pX, pY, 1);
//  }
  stroke(0,0,0,255);
  line(x, y, waveX, y);
  
 
  
}
