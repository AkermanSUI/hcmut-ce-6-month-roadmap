# Weekly Review - HCMUT CE 6 Month Roadmap

## Week 0 - 2026-06-13 to 2026-06-14

### Việc đã hoàn thành
- Tạo folder bookmark học tập
- Tạo GitHub repo hcmut-ce-6-month-roadmap
- Tạo leetcode-log.md
- Tạo cs50-notes.md
- Mở đúng CS50x 2026
- Làm bài Two Sum
- Làm bài Contains Duplicate

### Kiến thức đã học
- LeetCode không cần main/cout, chỉ cần return đúng kiểu
- vector<int> là mảng động trong C++
- return {i, j} để trả về vector chứa 2 index
- sort(nums.begin(), nums.end()) dùng để sắp xếp vector tăng dần
- Brute force thường dễ hiểu nhưng có thể O(n^2)
- Sort giúp đưa bài Contains Duplicate về O(n log n)

### Lỗi sai đã gặp
- Nhầm return i,j; thay vì return {i, j}
- Ban đầu chưa hiểu cách LeetCode gọi hàm trong class Solution
- Nghĩ tới vét cạn trước nên bị lo Time Limit Exceeded

### Mục tiêu tuần 1
- Làm 5-8 bài LeetCode Easy
- Nắm chắc Array, String, Hash Table
- Học lại C++ vector, string, unordered_map, unordered_set
- Ghi log đầy đủ sau mỗi bài

### Bài LeetCode tuần 1
- Valid Anagram
- Move Zeroes
- Best Time to Buy and Sell Stock
- Merge Sorted Array
- Valid Palindrome
- Plus One
- Remove Duplicates from Sorted Array


## 2026-06-17 - Review Hash Table + Two Pointers

### Nội dung đã hoàn thành
- Ôn lại Two Sum bằng unordered_map
- Ôn lại Contains Duplicate bằng unordered_set
- Ôn Valid Anagram bằng count[26]
- Ôn Move Zeroes bằng two pointers in-place
- Học khái niệm hash table, hash function, key-value, collision

### Kiến thức cần nhớ
- unordered_set dùng để kiểm tra phần tử đã xuất hiện chưa
- unordered_map dùng để lưu key -> value
- Hash table giúp tra cứu trung bình O(1)
- Với bài duplicate/intersection/frequency/pair sum, nên nghĩ tới hash table
- Với bài cần sửa trực tiếp vector, chú ý in-place và dấu &

### Điểm đã tiến bộ
- Không còn chỉ nghĩ brute force
- Bắt đầu biết nhìn pattern: Hash Table, Two Pointers, One Pass
- Biết phân biệt pass được và tối ưu đúng ý đề


## Week 1 Review - 2026-06-15 to 2026-06-21

### Bài LeetCode đã làm

- Two Sum
- Contains Duplicate
- Valid Anagram
- Move Zeroes
- Best Time to Buy and Sell Stock
- Merge Sorted Array
- Valid Palindrome
- Plus One
- Remove Duplicates from Sorted Array
- Running Sum of 1d Array
- Find Pivot Index
- Maximum Average Subarray I
- Max Consecutive Ones
- Length of Last Word

### Pattern đã học

- Brute Force
- Hash Table
- Sorting
- One Pass
- Two Pointers
- In-place Array
- Prefix Sum
- Sliding Window
- String Traversal
- Frequency Array
- Carry

### Kiến thức C++ đã học

- vector<int>
- vector<char>
- string
- sort()
- push_back()
- insert()
- unordered_set
- unordered_map
- isalnum()
- tolower()
- swap()
- return vector
- hàm void sửa trực tiếp vector tham chiếu

### Lỗi sai đã gặp

- Nhầm return i,j; thay vì return {i, j}
- Nhầm '0' với 0
- Nhầm " " với ' '
- Quên LeetCode không cần main/cout
- Truy cập vượt chỉ số vector
- Dùng brute force O(n^2) nên bị Time Limit Exceeded
- Chưa quen việc LeetCode chỉ kiểm tra k phần tử đầu trong bài Remove Duplicates

### Bài học quan trọng

- Không phải cứ pass là tối ưu.
- Khi đề có duplicate, frequency, intersection, pair sum thì nghĩ tới Hash Table.
- Khi đề yêu cầu sửa trực tiếp vector thì nghĩ tới In-place.
- Khi xét hai đầu hoặc nén mảng thì nghĩ tới Two Pointers.
- Khi tính tổng đoạn hoặc tổng trái/phải thì nghĩ tới Prefix Sum.
- Khi xét đoạn con liên tiếp thì nghĩ tới Sliding Window.

### Mục tiêu tuần 2

- Làm chắc String + Two Pointers
- Bắt đầu Linked List cơ bản
- Ôn lại Array/Hash Table
- Duy trì ghi log sau mỗi bài

## Week 2 Review - 2026-06-22 to 2026-06-28

### Chủ đề đã học

- Linked List
- Stack
- Queue
- Stack Design
- String as Stack

### Bài LeetCode đã làm

- Middle of the Linked List
- Reverse Linked List
- Linked List Cycle
- Merge Two Sorted Lists
- Valid Parentheses
- Baseball Game
- Number of Recent Calls
- Implement Queue using Stacks
- Backspace String Compare
- Remove All Adjacent Duplicates In String
- Min Stack
- Make The String Great

### Pattern đã học

- Slow-Fast Pointers
- Pointer Reversal
- Floyd Cycle Detection
- Dummy Node
- Stack Matching
- Stack Simulation
- Queue FIFO
- Two Stacks
- String as Stack
- Stack Cancellation
- Auxiliary Stack

### Kiến thức C++ đã học

- ListNode*
- nullptr
- node->next
- stack<int>
- stack<char>
- queue<int>
- string as stack
- push()
- pop()
- top()
- front()
- back()
- empty()
- size()
- push_back()
- pop_back()
- stoi()
- abs()

### Lỗi sai đã gặp

- Gọi fast->next khi fast có thể là nullptr
- Quên lưu nextNode trước khi bẻ cur->next trong Reverse Linked List
- Check nhầm s.empty() thay vì st.empty()
- Dùng string nhưng gọi .top(), đúng phải là .back()
- Return stack trong khi hàm yêu cầu return string
- Viết sai ngoặc: abs(res.back() - c == 32) thay vì abs(res.back() - c) == 32

### Bài yếu cần ôn thêm

- Reverse Linked List
- Merge Two Sorted Lists
- Min Stack
- Implement Queue using Stacks

### Bài học quan trọng

- Linked List là thao tác với mũi tên next.
- Stack dùng khi cần xử lý phần tử gần nhất trước đó.
- Queue dùng khi cần xử lý theo thứ tự vào trước ra trước.
- string có thể dùng như stack khi xử lý chuỗi và cần trả về chuỗi.
- Trước khi dùng top(), back(), front() phải đảm bảo container không rỗng.

### Mục tiêu tuần 3

- Bắt đầu Binary Search
- Ôn lại Two Pointers
- Làm quen Recursion cơ bản
- Tiếp tục duy trì log sau mỗi bài


## Week 3 Review - 2026-06-29 to 2026-07-05

### Chủ đề đã học
- Binary Search
- Binary Search on Answer
- Two Pointers
- Recursion

### Bài quan trọng
- Binary Search
- Sqrt(x)
- Arranging Coins
- Reverse Words in a String III
- Power of Two
- Add Digits

### Lỗi cần nhớ
- `left = mid++` gây TLE
- `right = right - 1` chưa chuẩn, nên dùng `right = mid - 1`
- `mid * mid` nên dùng `long long`
- Gặp dấu cách ở `i` thì đảo từ `left` đến `i - 1`
- `return n / 2` sai trong hàm bool
- Recursion phải có base case

### Mục tiêu tuần sau
- Học Binary Tree cơ bản
- Ôn recursion qua cây


## Week 4 Review - 2026-07-06 to 2026-07-12

### Chủ đề đã học

- Binary Tree
- Tree DFS
- Tree Recursion
- Tree Traversal
- Tree Depth / Height
- Root-to-Leaf Path
- Mirror Recursion
- Global Answer in Tree

### Bài LeetCode đã làm

- Maximum Depth of Binary Tree
- Same Tree
- Invert Binary Tree
- Symmetric Tree
- Binary Tree Inorder Traversal
- Binary Tree Preorder Traversal
- Binary Tree Postorder Traversal
- Path Sum
- Minimum Depth of Binary Tree
- Balanced Binary Tree
- Sum of Left Leaves
- Diameter of Binary Tree

### Pattern đã học

- Tree DFS Recursion
- Compare Two Trees
- Tree Transformation
- Mirror Recursion
- Inorder Traversal
- Preorder Traversal
- Postorder Traversal
- Root-to-Leaf DFS
- Tree Depth DFS
- Height Check
- Tree DFS with Condition
- Tree Height + Global Answer

### Kiến thức C++ đã học

- TreeNode*
- root->val
- root->left
- root->right
- nullptr
- helper function
- vector<int>& res
- recursion return int
- recursion return bool
- global variable ans

### Lỗi sai đã gặp

- Chưa quen tư duy TreeNode* và con trỏ
- Nhầm node lá với nullptr
- Minimum Depth không được lấy min với nhánh nullptr
- Sum of Left Leaves không phải cộng mọi node, chỉ cộng left leaf
- Balanced Tree phải kiểm tra mọi node, không chỉ root
- Diameter dùng ans để lưu đường kính, còn hàm height vẫn return chiều cao
- Traversal chỉ khác vị trí push_back(root->val)

### Bài yếu cần ôn thêm

- Minimum Depth of Binary Tree
- Balanced Binary Tree
- Sum of Left Leaves
- Diameter of Binary Tree
- Symmetric Tree

### Bài học quan trọng

- Tree recursion thường bắt đầu bằng `if (root == nullptr)`.
- Với tree, mỗi node thường hỏi cùng một câu hỏi cho left và right.
- Traversal khác nhau ở vị trí xử lý root.
- Height trả về cho node cha sử dụng.
- Diameter cần biến ans vì đáp án có thể nằm ở bất kỳ node nào.
- Node lá là node không có cả left và right.

### Mục tiêu tuần sau

- Ôn lại Binary Tree nếu còn yếu
- Bắt đầu Binary Search Tree hoặc Recursion nâng nhẹ
- Làm thêm bài tổng hợp DSA Easy/Medium nhẹ
