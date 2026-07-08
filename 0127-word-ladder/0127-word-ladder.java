class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

        Set<String> dict = new HashSet<>(wordList);

        if (!dict.contains(endWord))
            return 0;

        Queue<String> q = new LinkedList<>();
        q.offer(beginWord);

        Set<String> visited = new HashSet<>();
        visited.add(beginWord);

        int level = 1;

        while (!q.isEmpty()) {

            int size = q.size();

            while (size-- > 0) {

                String word = q.poll();
                if (word.equals(endWord))
                    return level;

                char[] arr = word.toCharArray();

                for (int i = 0; i < arr.length; i++) {

                    char old = arr[i];

                    for (char c = 'a'; c <= 'z'; c++) {

                        arr[i] = c;
                        String next = new String(arr);

                        if (dict.contains(next) && !visited.contains(next)) {
                            visited.add(next);
                            q.offer(next);
                        }
                    }

                    arr[i] = old;
                }
            }

            level++;
        }

        return 0;
    }
}