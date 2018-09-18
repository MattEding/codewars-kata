const COMPASS = {NORTH: "SOUTH", SOUTH: "NORTH", EAST: "WEST", WEST: "EAST"}

function dirReduc(arr){
  for (let [i, dir] of arr.entries()) {
    let opp = COMPASS[dir];
    let next = arr[i + 1];
    if (next == opp) {
      arr.splice(i, 2);
      dirReduc(arr);
    }
  }
  return arr;
}
