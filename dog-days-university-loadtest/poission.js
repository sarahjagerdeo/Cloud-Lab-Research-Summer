// Rate is the RPS you want to use

function randomExponential(rate, randomUniform) {

    rate = rate || 1;
  
    // Allow to pass a random uniform value or function
    // Default to Math.random()
    var U = randomUniform;
    if (typeof randomUniform === 'function') U = randomUniform();
    if (!U) U = Math.random();
  
    return -Math.log(U)/rate;
  }

  randomExponential();
  for (let i = 0; i <= 1000; i++){
    console.log(randomExponential(2));

   }


//Code: nicolashery/poisson.js