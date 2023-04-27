/*
Insertion Sort

Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
*/

function insertionSort(data:Array<number>): Array<number>
{
    let step_index = 1;
    for(let i = 0; i < data.length; i++){
        // step_index 2
        for(let j = 0; j < step_index; j++){
            if(data[i] < data[j]){
                const temp = data[j];
                data[j] = data[i];
                data[i] = temp;
                step_index+=1;
            }
        }
    }
    return data
}


let data:Array<number> = [5, 2, 8, 9, 7, 4, 3, 6, 10, 1];
let result:Array<number> = insertionSort(data);

console.log(result); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]