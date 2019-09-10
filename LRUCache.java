import java.util.*;

class LRUCache {

    //Use double linked list and hashmap
    private HashMap<Integer,Node> map = new HashMap<>();
    private int Cache_Size;
    private Node head = null;
    private Node tail = null;
    private Node temp;
    private int pop_key;
    public LRUCache(int capacity) {
        Cache_Size = capacity;
    }

    public int get(int key) {
        if(map.containsKey(key)){
            temp = map.get(key);
            updateLinkedlist(temp);
            return temp.value;
        }else{
            return -1;
        }
    }

    public static void main(String [ ] args){
        LRUCache cache = new LRUCache( 2 /* capacity */ );
        cache.get(2);
        cache.put(2,6);
        cache.get(1);
        cache.put(1,5);
        cache.put(1,2);
        cache.get(1);
        cache.get(2);

        // returns 4

    }
    public void put(int key, int value) {

        if(!map.containsKey(key)){
            if (map.size() < Cache_Size){
                addnewnode(key,value);
            }else{
                pop_key = poptheoldest();
                map.remove(pop_key);
                addnewnode(key,value);

            }
        }else{
            map.get(key).value = value;
            updateLinkedlist(map.get(key));
        }

    }
    private void addnewnode(int key,int value){
        temp = new Node(key,value);
        if(head == null && tail == null){
            head = temp;
            tail = temp;
        }else{
            addtotail(temp);
        }
        map.put(key,temp);   //First element will be the oldest. Last element is the newest.
    }
    private void addtotail(Node node){
        node.prev = tail;
        tail.next = node;
        tail = node;

    }
    private int poptheoldest(){
        int key = head.key;
        if(head.next != null){
            head = head.next;
            head.prev = null;
        }else{
            head = null;
            tail = null;
        }
        return key;

    }
    private void updateLinkedlist(Node node){
        if(head == tail){
            //do nothing;
        }else if(head == node){
            head = node.next;
            head.prev = null;
            node.prev = tail;
            node.next = null;
            tail.next = node;
            tail = node;
        }else if(tail == node){
            //do nothing, already the newest.
        }else{
            node.prev.next = node.next;
            node.next.prev = node.prev;
            tail.next = node;
            node.prev = tail;
            node.next = null;
            tail = node;
        }
    }
}


class Node{
    public Node prev;
    public Node next;
    public int value;
    public int key;
    public Node(int key, int value) {
        prev = null;
        next = null;
        this.value = value;
        this.key = key;
    }


}
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

