class Solution {
    public int reverse(int x) {
        boolean neg = x<0;
        String start = Math.abs(x) + "";
        String end ="";
        for (char c: start.toCharArray()) 
            {
            end = c+end;
            }
        end = neg?"-"+end:end;
        try {return Integer.parseInt(end);}
catch (Exception e) {return 0;}
    }
}
