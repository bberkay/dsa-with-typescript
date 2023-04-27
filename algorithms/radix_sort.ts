function radixSort(data: Array<number>): Array<number>
{
    for(let i = 0; i<data.length;i++){
        while(data[i] > 0){
            let current_digit = data[i] % 10;
            data[i] /= 10;
        }
    }
    return data;
}

let data:Array<number> = [5, 2, 8, 9, 7, 4, 3, 6, 10, 1];
let result:Array<number> = radixSort(data);

console.log(result); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]