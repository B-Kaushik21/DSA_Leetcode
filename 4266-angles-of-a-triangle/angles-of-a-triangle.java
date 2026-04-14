class Solution {
    public double[] internalAngles(int[] sides) {
        double a=sides[0];
        double b=sides[1];
        double c=sides[2];

        if (a+b<=c || b+c<=a || c+a<=b){
            return new double[0];
        }

        double A=Math.acos((b*b+c*c-a*a)/(2*b*c))*180.0/ Math.PI;
        double B=Math.acos((a*a+c*c-b*b)/(2*a*c))*180.0/ Math.PI;
        double C=Math.acos((b*b-c*c+a*a)/(2*a*b))*180.0/ Math.PI;

        double res []= new double[]{A,B,C};
        Arrays.sort(res);
        return res;
    }
}