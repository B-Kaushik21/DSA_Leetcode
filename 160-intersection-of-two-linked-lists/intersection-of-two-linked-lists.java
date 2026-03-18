/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> sett=new HashSet<>();
        while(headA!=null){
            sett.add(headA);
            headA=headA.next;
        }
        while(headB!=null){
            if(sett.contains(headB)) return headB;
            sett.add(headB);
            headB=headB.next;
        }
        return null;
    }
}