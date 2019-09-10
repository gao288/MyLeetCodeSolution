import java.io.*;
import java.util.*;

public class median_of_two_sorted_array_4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int index1 = 0;
        int index2 = 0;
        int m = nums1.length - 1;
        int n = nums2.length - 1;
        int[] ary = new int[m+n+2];
        int count = 0;
        while (index1 <= m && index2 <= n) {

            if (nums1[m] < nums2[n]){
                ary[count]= nums1[m];
                m++;
            }else{
                ary[count]= nums2[n];
                n++;
            }
            count++;
        }
        if ((m + n + 2) % 2 == 0){
            return (double) (ary[(m + n + 2) / 2] + ary[(m + n + 2) / 2 - 1]) / 2;
        }
        else {
            return (double) ary[(m + n + 2) / 2];
        }

    }
}
