/*
Selection Sort
Selection sort is a simple sorting algorithm used to sort a list or array of elements. The algorithm works by finding the smallest element in the unsorted portion of the list and moving it to the beginning of the list, then repeating the process for the remaining unsorted elements until the entire list is sorted.


Time Complexity - Best, Worst, Average: O(n^2)
Space Complexity: O(1)
*/

function selectionSort(data:Array<number>) : Array<number>
{
    let smallest:number, temp:number;
    for(let step = 0; step < data.length; step++){
        smallest = data[step];
        temp = step;
        for(let i = step; i < data.length; i++){
            if(smallest > data[i]){
                temp = i;
                smallest = data[i];
            }             
        }
        data[temp] = data[step];
        data[step] = smallest;
    }

    return data
}


let data:Array<number> = [5, 2, 8, 9, 7, 4, 3, 6, 10, 1];
let result:Array<number> = selectionSort(data);

console.log(result); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]