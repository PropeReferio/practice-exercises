function longestConsec(strarr, k) {
    let n = strarr.length;
    // Step 1: return empty string if impossible
    if (k<=0 || n == 0 || k > n){
      return '';
    }
    // Step 2: store all possible concatenations in an array
    let possibles = [];
    for (let i=0; i<=n-k; i++){
      let start=strarr[i];
      for (let j=1; j<k; j++){
        start += strarr[i+j];
      }
      possibles.push(start); //adds each concatenation to an array called possibles
    }
    // Step 2.9: Save standalone copy of the array for later
    let original = []
    for (let i=0; i<possibles.length; i++){
      original.push(possibles[i]);
    }
    // Step 3: Sort array by length in descending order
    possibles.sort(function(a, b){
    return b.length - a.length;
    });
    // Step 4: Get length of 1st element in possibles
    let longlength = possibles[0].length;
    // Step 5: Return 1st element that has a length "longlength" in original
    for (let i=0; i<original.length; i++){
      if (original[i].length == longlength){
        return original[i];
      }
    }
}