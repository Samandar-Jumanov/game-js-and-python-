console.log('Welcome to the game ')
console.log('Treasure Game , ')

let direction = prompt('You are in the middle of tha Island , Choose "left" or "right"')

let getFunc = ()=>{
    if (direction === "left"){
        let left = prompt('You are near the lake boat is coming , "wait" or "swim"')
        if (left === "wait"){
            let rooms = prompt('You are arrived finally , Choose room "yellow" "green" "red"')
            if(rooms === "yellow"){
                console.log('You are Winner , Tresure')
            }
            else if (rooms === "red"){
            console.log('You are butied Game over ')
            }
            else 
            {
                console.log('Game over , you choked on the green liquid')
            }
        }
        else {
            console.log('You are drawned')
        }
    }
    else {
        console.log('You are fallen to the hole !')
    }
}
getFunc()