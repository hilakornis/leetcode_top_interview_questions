/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    
    public void aux(Node node_org, Node node_copy, HashMap<Integer, Node> map){
        
        // boolean was_explored = map.get(node_copy.val).neighbors != null;        
        // if(was_explored){
        //     return;
        // }
        // was_explored = false;
        Node clone;
        for(Node n : node_org.neighbors){
            if(map.keySet().contains(n.val)){
                 clone = map.get(n.val);
            }
            else{
                clone = new Node(n.val);     
                map.put(n.val, clone);
                aux(n, clone, map);    
            }
            node_copy.neighbors.add(clone);
        }
        
        
        
    }
    
    public Node cloneGraph(Node node) {
        if(node == null)
            return null;
        HashMap<Integer, Node> map = new HashMap<Integer, Node>();
        Node copy = new Node(node.val);
        map.put(copy.val, copy);
        aux(node,copy, map);
        return copy;
    }
}