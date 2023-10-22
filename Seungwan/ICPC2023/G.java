package Seungwan.ICPC2023;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class G {
  List<BunSu> listArr = new ArrayList();
  public int[] solution(int n,int k) {
    if(k==1) {
      return new int[]{0,1};
    }
    
    for(int i=1;i<=n;i++) {
      for(int j=0;j<i;j++) {
        if (gcd(j, i) == 1) {
          listArr.add(new BunSu(i, j));
        }
        else if(j==1) listArr.add(new BunSu(i,1));
      }
    }
    if(k == listArr.size()+2) {
      int[] returnArr = new int[2];
      returnArr[0] = 1;
      returnArr[1] = 1;
      return returnArr;
    }
    listArr.sort(new Comparator<BunSu>() {
      @Override
      public int compare(BunSu o1, BunSu o2) {
        return o1.answer() - o2.answer()> 0 ? 1 : -1;
      }
      
    });
    BunSu answer = listArr.get(k-1);
    // for(int i=0;i<listArr.size();i++) {
    //   System.out.println(listArr.get(i).son + " "+ listArr.get(i).parent);
    // }
    int[] ans = new int[2];
    ans[0] = answer.son;
    ans[1] = answer.parent;
    return ans;
  }
  int gcd(int a, int b) {
    while (b != 0) {
      int temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }
  class BunSu {
    int parent = 0;
    int son = 0;
    public BunSu(int parent, int son) {
      this.parent = parent;
      this.son = son;
    }
    public Double answer() {
      return  (son/(double) parent);
    }
  }
  public static void main(String[] args) {
    G g = new G();
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    int[] answer = g.solution(n, k);
    System.out.println(answer[0]+" "+answer[1]);
    sc.close();

  }
  
}

