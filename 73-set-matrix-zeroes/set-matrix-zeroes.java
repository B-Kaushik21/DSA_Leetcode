class Solution {
    public void setZeroes(int[][] matrix) {
        int rows=matrix.length;
        int cols=matrix[0].length;

        boolean firstRowHasZero=false;
        boolean firstColHasZero=false;

        //check first row contains zero
        for (int c=0; c<cols;c++){
            if (matrix[0][c]==0){
                firstRowHasZero=true;
                break;            }
        }
        //check first col contains zero
        for (int r=0;r<rows;r++){
            if(matrix[r][0]==0){
                firstColHasZero=true;
                break;
            }
        }
        //using first row&col as markers
        for (int r=1;r<rows;r++){
            for(int c=1;c<cols;c++){
                if (matrix[r][c]==0){
                    matrix[r][0]=0;
                    matrix[0][c]=0;
                }
            }
        }

        //set the marked rows to zero
        for (int r=1;r<rows;r++){
            if (matrix[r][0]==0){
                for(int c=1;c<cols;c++){
                    matrix[r][c]=0;
                }
            }
        }

        //set the marked cols to zero
        for (int c=1;c<cols;c++){
            if (matrix[0][c]==0){
                for(int r=1;r<rows;r++){
                    matrix[r][c]=0;
                }
            }
        }

        //set the first row to zero if needed
        if(firstRowHasZero){
            for(int c=0;c<cols;c++){
                matrix[0][c]=0;
            }
        }

        //set the first col to zero if needed
        if(firstColHasZero){
            for(int r=0;r<rows;r++){
                matrix[r][0]=0;
            }
        }
    }
}