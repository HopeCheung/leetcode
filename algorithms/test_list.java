public class InList {
	public IntList(int head, IntList tail){
		this.head = head;
		this.tail = tail;
	}

	static IntList incrLList(IntList P, int n){
		if (P == null)
			return null;
		IntList last, result;
		result = last = new Intlist(P.head+n, null);
		while (P.tail != null){
			P = P.tail;
			last.tail = new IntList(P.head+n,null);
			last = last.tail;
		}
		return result;
	}
}