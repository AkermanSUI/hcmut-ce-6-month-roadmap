# LeetCode Log - HCMUT CE 6 Month Roadmap

## Thông tin chung

- Mục tiêu 6 tháng: 80-120 bài LeetCode
- Ngôn ngữ chính: C++
- Hướng đi: Computer Engineering -> Software / Data / AI
- Quy tắc: mỗi bài phải ghi lại ý tưởng, lỗi sai, pattern và ngày làm lại

---

## Quy tắc luyện LeetCode

1. Tự nghĩ ít nhất 10 phút trước khi xem gợi ý.
2. Nếu bí quá 25-30 phút thì đọc hint/editorial.
3. Sau khi hiểu lời giải, tự code lại từ đầu.
4. Ghi lại lỗi sai vào log.
5. Làm lại bài sau 3 ngày, 7 ngày, 14 ngày nếu bài đó quan trọng.

---

## Template ghi bài

```text
### Tên bài:
- Link:
- Topic:
- Độ khó:
- Ngày làm:
- Trạng thái: Solved / Need Review / Failed
- Ý tưởng:
- Lỗi sai:
- Pattern:
- Độ phức tạp:
- Ngày cần làm lại:
 ```
## 2026-06-13
### 1. Two Sum

- Link: https://leetcode.com/problems/two-sum/
- Topic: Array, Hash Table
- Độ khó: Easy
- Ngày làm: 2026-06-13
- Trạng thái: Solved
- Ý tưởng: Duyệt từng cặp i, j. Nếu nums[i] + nums[j] == target thì return {i, j}.
- Lỗi sai: Ban đầu nhầm return i,j; và chưa hiểu LeetCode không cần main/cout.
- Pattern: Brute Force / Nested Loop
- Độ phức tạp: O(n^2) time, O(1) memory
- Ngày cần làm lại: 2026-06-16
- - Cách tối ưu: Dùng unordered_map lưu value -> index. Với mỗi nums[i], tìm need = target - nums[i]. Nếu need đã tồn tại trong map thì return {mp[need], i}.
- Độ phức tạp tối ưu: Time O(n), Space O(n)


### 2. Contains Duplicate

- Link: https://leetcode.com/problems/contains-duplicate/
- Topic: Array, Hash Table, Sorting
- Độ khó: Easy
- Ngày làm: 2026-06-14
- Trạng thái: Solved
- Ý tưởng: Sort mảng tăng dần, sau đó kiểm tra hai phần tử kề nhau. Nếu nums[i] == nums[i + 1] thì có duplicate.
- Lỗi sai: Ban đầu nghĩ dùng hai vòng for để so từng cặp nhưng dễ bị Time Limit Exceeded vì O(n^2).
- Pattern: Sorting + Adjacent Check
- Độ phức tạp: Time O(n log n), Space O(1) hoặc O(log n)
- Ngày cần làm lại: 2026-06-17
- Cách tối ưu: Dùng unordered_set để lưu các số đã gặp. Nếu gặp lại số đã có trong set thì return true.
- Độ phức tạp tối ưu: Time O(n), Space O(n)


## 2026-06-14
### 3. Valid Anagram

- Link: https://leetcode.com/problems/valid-anagram/
- Topic: String, Sorting, Hash Table
- Độ khó: Easy
- Ngày làm: 2026-06-14
- Trạng thái: Solved
- Ý tưởng:
  - Cách 1: Sort hai chuỗi rồi so sánh. Nếu sau khi sort mà s == t thì là anagram.
  - Cách 2: Dùng mảng count[26], gặp ký tự trong s thì +1, gặp ký tự trong t thì -1. Cuối cùng nếu tất cả bằng 0 thì là anagram.
- Lỗi sai:
  - Ban đầu hiểu sai cách dùng compare(): s.compare(t) == 0 mới nghĩa là hai chuỗi giống nhau.
  - Không nên return false ngay khi gặp một ký tự chưa khớp nếu chưa kiểm tra hết.
- Pattern: Sorting / Frequency Array
- Độ phức tạp:
  - Cách sort: Time O(n log n), Space O(1) hoặc O(log n)
  - Cách count[26]: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-17


### 4. Move Zeroes

- Link: https://leetcode.com/problems/move-zeroes/
- Topic: Array, Two Pointers
- Độ khó: Easy
- Ngày làm: 2026-06-14
- Trạng thái: Solved
- Ý tưởng:
  - Cách 1: Tạo vector nonZero để lưu số khác 0, vector zeroes để lưu số 0.
  - Sau đó nối zeroes vào cuối nonZero rồi gán lại nums = nonZero.
- Lỗi sai:
  - Ban đầu nhầm nums[i] == '0' thay vì nums[i] == 0.
  - Ban đầu khởi tạo vector<int> newNum = {0}, làm dư số 0.
  - Ban đầu cout vector trực tiếp, nhưng LeetCode chỉ cần sửa nums, không cần cout.
- Pattern: Extra Array / Two Pointers
- Độ phức tạp:
  - Cách vector phụ: Time O(n), Space O(n)
  - Cách tối ưu two pointers: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-17

### 5. Best Time to Buy and Sell Stock

- Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Topic: Array, Dynamic Programming
- Độ khó: Easy
- Ngày làm: 2026-06-15
- Trạng thái: Solved
- Ý tưởng: Duyệt mảng một lần, luôn lưu giá mua thấp nhất đã gặp bằng minPrice. Với mỗi ngày, tính profit = prices[i] - minPrice rồi cập nhật maxProfit.
- Lỗi sai: Ban đầu dùng hai vòng for để xét mọi cặp mua-bán nên bị Time Limit Exceeded vì O(n^2).
- Pattern: One Pass / Track Minimum
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-18

### 6. Merge Sorted Array

- Link: https://leetcode.com/problems/merge-sorted-array/
- Topic: Array, Two Pointers, Sorting
- Độ khó: Easy
- Ngày làm: 2026-06-15
- Trạng thái: Solved
- Ý tưởng ban đầu: Chép nums2 vào phần trống cuối nums1, sau đó sort lại nums1.
- Lỗi sai / điểm cần cải thiện: Cách này pass nhưng chưa tận dụng việc nums1 và nums2 đã được sort sẵn.
- Pattern: Merge / Two Pointers from End
- Độ phức tạp:
  - Cách sort lại: Time O((m+n) log(m+n)), Space tùy sort
  - Cách tối ưu: Time O(m+n), Space O(1)
- Ngày cần làm lại: 2026-06-18


### 7. Valid Palindrome

- Link: https://leetcode.com/problems/valid-palindrome/
- Topic: Two Pointers, String
- Độ khó: Easy
- Ngày làm: 2026-06-15
- Trạng thái: Solved
- Ý tưởng: Tạo string mới sNew, chỉ giữ lại chữ cái/chữ số bằng isalnum(), chuyển về chữ thường bằng tolower(), sau đó dùng hai con trỏ left/right để kiểm tra palindrome.
- Lỗi sai: Chưa có lỗi lớn; cần nhớ isalnum() để lọc ký tự hợp lệ và tolower() để chuẩn hóa chữ hoa/thường.
- Pattern: Clean String + Two Pointers
- Độ phức tạp: Time O(n), Space O(n)
- Cách tối ưu sau này: Dùng two pointers trực tiếp trên chuỗi gốc để đạt Space O(1).
- Ngày cần làm lại: 2026-06-18

## 2026-06-15
### 8. Plus One

- Link: https://leetcode.com/problems/plus-one/
- Topic: Array, Math
- Độ khó: Easy
- Ngày làm: 2026-06-16
- Trạng thái: Solved
- Ý tưởng: Duyệt từ cuối vector về đầu. Nếu gặp chữ số nhỏ hơn 9 thì cộng 1 và return. Nếu gặp 9 thì đổi thành 0 và tiếp tục carry sang trái. Nếu toàn bộ là 9 thì chèn 1 vào đầu.
- Lỗi sai: Ban đầu xử lý trường hợp toàn số 9 bằng cách gán digits[0] = 1 nhưng thiếu thêm một phần tử mới; cũng có nguy cơ truy cập vượt biên digits[a].
- Pattern: Reverse Traversal / Carry
- Độ phức tạp: Time O(n), Space O(1) nếu không tính output
- Ngày cần làm lại: 2026-06-19


### 9. Remove Duplicates from Sorted Array

- Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- Topic: Array, Two Pointers
- Độ khó: Easy
- Ngày làm: 2026-06-16
- Trạng thái: Solved
- Ý tưởng: Vì mảng đã sort, các phần tử trùng nhau nằm cạnh nhau. Dùng k làm vị trí đặt phần tử unique tiếp theo. Nếu nums[i] != nums[i - 1] thì gán nums[k] = nums[i], rồi tăng k.
- Lỗi sai: Ban đầu thắc mắc vì sao phần dư cuối mảng vẫn còn mà vẫn pass; hiểu ra LeetCode chỉ kiểm tra k phần tử đầu tiên.
- Pattern: In-place / Slow-Fast Pointers
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-19

## 2026-06-17 - Review Hash Table + Two Pointers

### Bài đã làm lại
- Two Sum: unordered_map, Time O(n), Space O(n)
- Contains Duplicate: unordered_set, Time O(n), Space O(n)
- Valid Anagram: count[26], Time O(n), Space O(1)
- Move Zeroes: two pointers in-place, Time O(n), Space O(1)

### Kiến thức củng cố
- unordered_map dùng cho key -> value
- unordered_set dùng để kiểm tra đã xuất hiện chưa
- count[26] dùng khi chuỗi chỉ gồm a-z
- two pointers giúp sửa mảng in-place
- check trước rồi insert sau trong bài duplicate/two sum

### Điểm cần nhớ
- LeetCode không cần main/cout
- Hàm void thì sửa trực tiếp vector tham chiếu
- Hàm trả vector thì return vector



## 2026-06-18

### 10. Running Sum of 1d Array

- Link: https://leetcode.com/problems/running-sum-of-1d-array/
- Topic: Array, Prefix Sum
- Độ khó: Easy
- Ngày làm: 2026-06-18
- Trạng thái: Solved
- Ý tưởng: Duyệt từ trái sang phải, mỗi phần tử mới bằng tổng các phần tử từ đầu đến vị trí hiện tại. Có thể tạo vector mới hoặc sửa trực tiếp nums.
- Lỗi sai:
- Pattern: Prefix Sum / In-place
- Độ phức tạp: Time O(n), Space O(1) nếu sửa trực tiếp
- Ngày cần làm lại: 2026-06-21

### 11. Find Pivot Index

- Link: https://leetcode.com/problems/find-pivot-index/
- Topic: Array, Prefix Sum
- Độ khó: Easy
- Ngày làm: 2026-06-18
- Trạng thái: Solved
- Ý tưởng: Tính total sum của mảng. Khi duyệt từng index i, rightSum = total - leftSum - nums[i]. Nếu leftSum == rightSum thì return i. Sau đó cập nhật leftSum += nums[i].
- Lỗi sai:
- Pattern: Prefix Sum / Left Sum - Right Sum
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-21

### 12. Maximum Average Subarray I

- Link: https://leetcode.com/problems/maximum-average-subarray-i/
- Topic: Array, Sliding Window
- Độ khó: Easy
- Ngày làm: 2026-06-18
- Trạng thái: Solved
- Ý tưởng: Tính tổng cửa sổ đầu tiên độ dài k. Sau đó trượt cửa sổ bằng cách trừ phần tử rời khỏi cửa sổ và cộng phần tử mới đi vào. Cập nhật maxSum.
- Lỗi sai:
- Pattern: Fixed-size Sliding Window
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-21


## 2026-06-19

### 13. Maximum Average Subarray I

- Link: https://leetcode.com/problems/maximum-average-subarray-i/
- Topic: Array, Sliding Window
- Độ khó: Easy
- Ngày làm: 2026-06-19
- Trạng thái: Solved
- Ý tưởng: Tính tổng cửa sổ đầu tiên độ dài k. Sau đó trượt cửa sổ bằng cách trừ phần tử rời khỏi cửa sổ nums[i-k] và cộng phần tử mới nums[i]. Cập nhật maxSum.
- Lỗi sai:
- Pattern: Fixed-size Sliding Window
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-22

### 14. Max Consecutive Ones

- Link: https://leetcode.com/problems/max-consecutive-ones/
- Topic: Array, Counting
- Độ khó: Easy
- Ngày làm: 2026-06-19
- Trạng thái: Solved
- Ý tưởng: Duyệt mảng, nếu gặp 1 thì tăng count và cập nhật maxCount. Nếu gặp 0 thì reset count về 0.
- Lỗi sai:
- Pattern: Consecutive Counting / One Pass
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-22

## 2026-06-20

### 15. Length of Last Word

- Link: https://leetcode.com/problems/length-of-last-word/
- Topic: String
- Độ khó: Easy
- Ngày làm: 2026-06-20
- Trạng thái: Solved
- Ý tưởng: Duyệt từ cuối chuỗi, bỏ qua khoảng trắng cuối, sau đó đếm độ dài từ cuối cùng cho đến khi gặp khoảng trắng.
- Lỗi sai:
- Pattern: Reverse String Traversal
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-23

### 16. Reverse String

- Link: https://leetcode.com/problems/reverse-string/
- Topic: Two Pointers, String
- Độ khó: Easy
- Ngày làm: 2026-06-20
- Trạng thái: Solved
- Ý tưởng: Dùng left ở đầu, right ở cuối, swap hai ký tự rồi left++, right-- cho đến khi gặp nhau.
- Lỗi sai:
- Pattern: Two Pointers / In-place Swap
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-23

### 17. Reverse Vowels of a String

- Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
- Topic: Two Pointers, String
- Độ khó: Easy
- Ngày làm: 2026-06-20
- Trạng thái: Solved
- Ý tưởng: Dùng two pointers, bỏ qua ký tự không phải nguyên âm ở hai đầu. Khi cả hai đầu đều là nguyên âm thì swap.
- Lỗi sai:
- Pattern: Two Pointers / Character Filtering
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-23

## 2026-06-22

### 18. Middle of the Linked List

- Link: https://leetcode.com/problems/middle-of-the-linked-list/
- Topic: Linked List, Two Pointers
- Độ khó: Easy
- Ngày làm: 2026-06-22
- Trạng thái: Solved
- Ý tưởng: Dùng slow đi 1 bước, fast đi 2 bước. Khi fast đi hết list thì slow nằm ở giữa.
- Lỗi sai / điểm cần nhớ: Phải check `fast != nullptr && fast->next != nullptr` để tránh truy cập `fast->next` khi fast đã rỗng.
- Pattern: Slow-Fast Pointers
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-25

### 19. Reverse Linked List

- Link: https://leetcode.com/problems/reverse-linked-list/
- Topic: Linked List
- Độ khó: Easy
- Ngày làm: 2026-06-22
- Trạng thái: Solved
- Ý tưởng: Dùng 3 con trỏ `prev`, `cur`, `nextNode`. Mỗi vòng lưu node tiếp theo, bẻ `cur->next` về `prev`, rồi dời `prev` và `cur` tiến lên.
- Lỗi sai / điểm cần nhớ: Phải lưu `nextNode = cur->next` trước khi bẻ mũi tên, nếu không sẽ mất phần còn lại của list.
- Pattern: Pointer Reversal
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-25

## 2026-06-23

### 20. Linked List Cycle

- Link: https://leetcode.com/problems/linked-list-cycle/
- Topic: Linked List, Two Pointers
- Độ khó: Easy
- Ngày làm: 2026-06-23
- Trạng thái: Solved
- Ý tưởng: Dùng slow đi 1 bước, fast đi 2 bước. Nếu linked list có cycle thì slow và fast sẽ gặp nhau. Nếu không có cycle thì fast sẽ chạm nullptr.
- Lỗi sai:
- Pattern: Floyd Cycle Detection / Slow-Fast Pointers
- Độ phức tạp: Time O(n), Space O(1)
- Ngày cần làm lại: 2026-06-26

### 21. Merge Two Sorted Lists

- Link: https://leetcode.com/problems/merge-two-sorted-lists/
- Topic: Linked List, Recursion
- Độ khó: Easy
- Ngày làm: 2026-06-23
- Trạng thái: Solved
- Ý tưởng: Dùng dummy node và tail để xây list kết quả. So sánh list1->val và list2->val, nối node nhỏ hơn vào tail, rồi dịch con trỏ tương ứng.
- Lỗi sai:
- Pattern: Dummy Node / Merge
- Độ phức tạp: Time O(n + m), Space O(1)
- Ngày cần làm lại: 2026-06-26


## 2026-06-24

### 22. Valid Parentheses

- Link: https://leetcode.com/problems/valid-parentheses/
- Topic: Stack, String
- Độ khó: Easy
- Ngày làm: 2026-06-24
- Trạng thái: Solved
- Ý tưởng: Gặp ngoặc mở thì push vào stack. Gặp ngoặc đóng thì kiểm tra stack có rỗng không, sau đó so sánh với ngoặc mở tương ứng ở top. Nếu khớp thì pop. Cuối cùng stack phải rỗng.
- Lỗi sai / điểm cần nhớ: Ban đầu check nhầm `s.empty()` thay vì `st.empty()`. Trước khi gọi `st.top()` phải chắc chắn stack không rỗng.
- Pattern: Stack Matching
- Độ phức tạp: Time O(n), Space O(n)
- Ngày cần làm lại: 2026-06-27

### 23. Baseball Game

- Link: https://leetcode.com/problems/baseball-game/
- Topic: Stack, Simulation
- Độ khó: Easy
- Ngày làm: 2026-06-24
- Trạng thái: Solved
- Ý tưởng: Dùng vector như stack để lưu điểm hợp lệ. Số thì thêm vào, `C` thì xóa điểm trước, `D` thì thêm gấp đôi điểm trước, `+` thì thêm tổng hai điểm trước.
- Lỗi sai / điểm cần nhớ: `stoi(op)` dùng để chuyển string thành int, ví dụ `"5"` thành `5`.
- Pattern: Stack Simulation
- Độ phức tạp: Time O(n), Space O(n)
- Ngày cần làm lại: 2026-06-27


## 2026-06-25

### 24. Number of Recent Calls

- Link: https://leetcode.com/problems/number-of-recent-calls/
- Topic: Queue, Design
- Độ khó: Easy
- Ngày làm: 2026-06-25
- Trạng thái: Solved
- Dịch đề: Mỗi lần gọi `ping(t)` là có một request mới tại thời điểm `t`. Trả về số request nằm trong khoảng từ `t - 3000` đến `t`.
- Ý tưởng: Dùng queue lưu thời điểm request. Mỗi lần ping thì push `t`, sau đó pop các request quá cũ ở đầu queue.
- Lỗi sai / điểm cần nhớ: Request nghĩa là một lần gọi `ping(t)`. `q.front() < t - 3000` nghĩa là request đó đã nằm ngoài 3000ms gần nhất.
- Pattern: Sliding Window with Queue
- Độ phức tạp: Time O(n) tổng thể, mỗi phần tử vào/ra queue một lần; Space O(n)
- Ngày cần làm lại: 2026-06-28

### 25. Implement Queue using Stacks

- Link: https://leetcode.com/problems/implement-queue-using-stacks/
- Topic: Stack, Queue, Design
- Độ khó: Easy
- Ngày làm: 2026-06-25
- Trạng thái: Solved
- Dịch đề: Tự xây dựng một queue có các hàm `push`, `pop`, `peek`, `empty`, nhưng chỉ được dùng stack.
- Ý tưởng: Dùng hai stack `in` và `out`. `in` nhận phần tử mới. Khi cần lấy phần tử đầu queue mà `out` rỗng, chuyển toàn bộ từ `in` sang `out` để đảo thứ tự.
- Lỗi sai / điểm cần nhớ: Queue là vào trước ra trước, stack là vào sau ra trước. Hai stack giúp đảo thứ tự hai lần để lấy đúng phần tử vào đầu tiên.
- Pattern: Two Stacks
- Độ phức tạp: Amortized O(1) cho mỗi thao tác; Space O(n)
- Ngày cần làm lại: 2026-06-28

### 27. Remove All Adjacent Duplicates In String

- Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
- Topic: Stack, String
- Độ khó: Easy
- Ngày làm: 2026-06-26
- Trạng thái: Solved
- Dịch đề: Cho một chuỗi, nếu có hai ký tự giống nhau đứng cạnh nhau thì xóa cả hai. Lặp lại cho đến khi không còn cặp trùng cạnh nhau.
- Ý tưởng: Dùng `string res` như stack. Nếu ký tự hiện tại bằng ký tự cuối của `res` thì xóa ký tự cuối. Nếu không thì thêm ký tự hiện tại vào `res`.
- Lỗi sai / điểm cần nhớ: Hàm cần trả về `string`, nên không thể `return stack`. Dùng `res.back()`, `res.push_back()`, `res.pop_back()` sẽ gọn hơn dùng `stack<char>`.
- Pattern: Stack Cancellation
- Độ phức tạp: Time O(n), Space O(n)
- Ngày cần làm lại: 2026-06-29

## 2026-06-27

### 28. Min Stack

- Link: https://leetcode.com/problems/min-stack/
- Topic: Stack, Design
- Độ khó: Medium
- Ngày làm: 2026-06-27
- Trạng thái: Solved
- Dịch đề: Thiết kế stack có các hàm push, pop, top và getMin. Hàm getMin phải trả về phần tử nhỏ nhất trong stack một cách nhanh.
- Ý tưởng: Dùng hai stack. Stack chính lưu toàn bộ giá trị. Stack phụ `minSt` lưu các giá trị nhỏ nhất theo từng thời điểm.
- Lỗi sai / điểm cần nhớ: Dùng `<=` khi push vào `minSt` để xử lý trường hợp có nhiều phần tử nhỏ nhất giống nhau. Có thể dùng `vector<int>` như stack để code gọn và runtime ổn hơn.
- Pattern: Auxiliary Stack
- Độ phức tạp: Time O(1) cho mỗi thao tác, Space O(n)
- Ngày cần làm lại: 2026-06-30

### 29. Make The String Great

- Link: https://leetcode.com/problems/make-the-string-great/
- Topic: Stack, String
- Độ khó: Easy
- Ngày làm: 2026-06-27
- Trạng thái: Solved
- Dịch đề: Cho chuỗi `s`, nếu có hai ký tự cạnh nhau là cùng một chữ cái nhưng khác hoa/thường thì xóa cả hai. Lặp lại đến khi không còn cặp như vậy.
- Ý tưởng: Dùng `string res` như stack. Nếu ký tự hiện tại và ký tự cuối của `res` lệch nhau 32 trong bảng ASCII thì xóa ký tự cuối, ngược lại thì thêm ký tự hiện tại.
- Lỗi sai / điểm cần nhớ: `string` không có `.top()`, phải dùng `.back()`. Ngoài ra cần viết đúng `abs(res.back() - c) == 32`, không phải `abs(res.back() - c == 32)`.
- Pattern: Stack Cancellation
- Độ phức tạp: Time O(n), Space O(n)
- Ngày cần làm lại: 2026-06-30

## 2026-06-29

### 30. Binary Search

- Link: https://leetcode.com/problems/binary-search/
- Topic: Binary Search, Array
- Độ khó: Easy
- Ngày làm: 2026-06-29
- Trạng thái: Solved
- Dịch đề: Cho mảng `nums` đã sắp xếp tăng dần và số `target`. Nếu `target` có trong mảng thì trả về index, nếu không thì trả về `-1`.
- Ý tưởng: Dùng hai biến `left` và `right`, mỗi lần lấy `mid`. Nếu `nums[mid]` nhỏ hơn target thì tìm bên phải, nếu lớn hơn target thì tìm bên trái.
- Lỗi sai / điểm cần nhớ: Không dùng `left = mid++`. Phải dùng `left = mid + 1` để vùng tìm kiếm thật sự nhỏ lại, tránh Time Limit Exceeded.
- Pattern: Binary Search
- Độ phức tạp: Time O(log n), Space O(1)
- Ngày cần làm lại: 2026-07-02

### 31. Search Insert Position

- Link: https://leetcode.com/problems/search-insert-position/
- Topic: Binary Search, Array
- Độ khó: Easy
- Ngày làm: 2026-06-29
- Trạng thái: Solved
- Dịch đề: Cho mảng `nums` đã sắp xếp tăng dần và số `target`. Nếu target có trong mảng thì trả về index, nếu không thì trả về vị trí nên chèn target vào để mảng vẫn tăng dần.
- Ý tưởng: Dùng Binary Search. Nếu tìm thấy thì trả về `mid`. Nếu không tìm thấy, sau vòng lặp `left` chính là vị trí cần chèn.
- Lỗi sai / điểm cần nhớ: Khi target nhỏ hơn `nums[mid]`, nên dùng `right = mid - 1`, không phải `right = right - 1`.
- Pattern: Binary Search Insert Position
- Độ phức tạp: Time O(log n), Space O(1)
- Ngày cần làm lại: 2026-07-02


## 2026-06-30

### 32. Sqrt(x)

* Link: https://leetcode.com/problems/sqrtx/
* Topic: Binary Search, Math
* Độ khó: Easy
* Ngày làm: 2026-06-30
* Trạng thái: Solved
* Dịch đề: Cho số nguyên không âm `x`, trả về phần nguyên của căn bậc hai của `x`. Không được dùng hàm `sqrt`.
* Ý tưởng: Dùng Binary Search để tìm số lớn nhất `mid` sao cho `mid * mid <= x`.
* Lỗi sai / điểm cần nhớ: Khi tính `mid * mid`, nên dùng `long long` để tránh tràn số.
* Pattern: Binary Search on Answer
* Độ phức tạp: Time O(log x), Space O(1)
* Ngày cần làm lại: 2026-07-03

### 33. Valid Perfect Square

* Link: https://leetcode.com/problems/valid-perfect-square/
* Topic: Binary Search, Math
* Độ khó: Easy
* Ngày làm: 2026-06-30
* Trạng thái: Solved
* Dịch đề: Cho số nguyên dương `num`, kiểm tra xem `num` có phải số chính phương không. Số chính phương là số có dạng `k * k`.
* Ý tưởng: Dùng Binary Search để tìm xem có số `mid` nào thỏa `mid * mid == num` hay không.
* Lỗi sai / điểm cần nhớ: Khi bài yêu cầu kiểm tra bình phương hoặc căn bậc hai, nên nghĩ tới Binary Search on Answer. Dùng `long long` cho biến `square = mid * mid`.
* Pattern: Binary Search on Answer
* Độ phức tạp: Time O(log num), Space O(1)
* Ngày cần làm lại: 2026-07-03


## 2026-07-01

### 34. Guess Number Higher or Lower

- Link: https://leetcode.com/problems/guess-number-higher-or-lower/
- Topic: Binary Search, Interactive
- Độ khó: Easy
- Ngày làm: 2026-07-01
- Trạng thái: Solved
- Dịch đề: Có một số bí mật nằm trong khoảng từ 1 đến n. Dùng hàm guess(num) để biết số mình đoán lớn hơn, nhỏ hơn hay bằng số bí mật. Trả về số bí mật đó.
- Ý tưởng: Dùng Binary Search trên khoảng [1, n]. Nếu guess(mid) trả về 1 thì mid nhỏ quá, tìm bên phải. Nếu trả về -1 thì mid lớn quá, tìm bên trái. Nếu trả về 0 thì tìm đúng.
- Lỗi sai / điểm cần nhớ: Phải hiểu đúng ý nghĩa của `guess(mid)`: `1` nghĩa là đoán nhỏ quá, `-1` nghĩa là đoán lớn quá.
- Pattern: Binary Search with API
- Độ phức tạp: Time O(log n), Space O(1)
- Ngày cần làm lại: 2026-07-04

### 35. Arranging Coins

- Link: https://leetcode.com/problems/arranging-coins/
- Topic: Binary Search, Math
- Độ khó: Easy
- Ngày làm: 2026-07-01
- Trạng thái: Solved
- Dịch đề: Có n đồng xu, xếp thành cầu thang. Hàng 1 cần 1 đồng, hàng 2 cần 2 đồng, hàng k cần k đồng. Trả về số hàng đầy đủ có thể xếp được.
- Ý tưởng: Tìm số hàng lớn nhất k sao cho k * (k + 1) / 2 <= n. Dùng Binary Search on Answer để tìm k.
- Lỗi sai / điểm cần nhớ: Công thức tổng 1 + 2 + ... + k là `k * (k + 1) / 2`. Nên dùng `long long` để tránh tràn số.
- Pattern: Binary Search on Answer
- Độ phức tạp: Time O(log n), Space O(1)
- Ngày cần làm lại: 2026-07-04

## 2026-07-02

### 36. Squares of a Sorted Array

- Link: https://leetcode.com/problems/squares-of-a-sorted-array/
- Topic: Array, Two Pointers, Sorting
- Độ khó: Easy
- Ngày làm: 2026-07-02
- Trạng thái: Solved
- Dịch đề: Cho mảng `nums` đã sắp xếp tăng dần. Bình phương từng phần tử rồi trả về mảng mới cũng được sắp xếp tăng dần.
- Ý tưởng: Vì số âm lớn khi bình phương có thể thành số rất lớn, nên dùng hai con trỏ ở hai đầu mảng. So sánh bình phương của hai đầu, số lớn hơn đặt vào cuối mảng kết quả.
- Lỗi sai / điểm cần nhớ: Điền kết quả từ cuối về đầu vì mỗi lần chọn ra bình phương lớn nhất còn lại.
- Pattern: Two Pointers from Both Ends
- Độ phức tạp: Time O(n), Space O(n)
- Ngày cần làm lại: 2026-07-05

### 37. Reverse Words in a String III

- Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
- Topic: String, Two Pointers
- Độ khó: Easy
- Ngày làm: 2026-07-02
- Trạng thái: Solved
- Dịch đề: Cho một chuỗi gồm nhiều từ. Đảo ngược từng từ riêng lẻ nhưng giữ nguyên thứ tự các từ.
- Ý tưởng: Duyệt chuỗi để tìm từng từ. Khi gặp dấu cách hoặc hết chuỗi, đảo đoạn từ vừa tìm được.
- Lỗi sai / điểm cần nhớ: Khi gặp dấu cách ở index `i`, từ cần đảo là từ `left` đến `i - 1`, không được đảo cả dấu cách. Cần xử lý thêm từ cuối cùng bằng điều kiện `i == s.size()`.
- Pattern: Reverse Each Segment
- Độ phức tạp: Time O(n), Space O(1) nếu sửa trực tiếp trên string
- Ngày cần làm lại: 2026-07-05


## 2026-07-03

### 38. Fibonacci Number

- Link: https://leetcode.com/problems/fibonacci-number/
- Topic: Recursion, Dynamic Programming, Math
- Độ khó: Easy
- Ngày làm: 2026-07-03
- Trạng thái: Solved
- Dịch đề: Cho số nguyên `n`, trả về số Fibonacci thứ `n`. Công thức là `F(0)=0`, `F(1)=1`, `F(n)=F(n-1)+F(n-2)`.
- Ý tưởng: Dùng recursion. Nếu `n` là 0 hoặc 1 thì trả về luôn. Nếu không, trả về `fib(n - 1) + fib(n - 2)`.
- Lỗi sai / điểm cần nhớ: Recursion cần base case để dừng. Bản recursion cơ bản dễ hiểu nhưng chưa tối ưu, sau này sẽ học DP để tối ưu.
- Pattern: Basic Recursion
- Độ phức tạp: Recursion cơ bản Time O(2^n), Space O(n). Bản iterative Time O(n), Space O(1).
- Ngày cần làm lại: 2026-07-06

### 39. Power of Two

- Link: https://leetcode.com/problems/power-of-two/
- Topic: Recursion, Math, Bit Manipulation
- Độ khó: Easy
- Ngày làm: 2026-07-03
- Trạng thái: Solved
- Dịch đề: Cho số nguyên `n`, kiểm tra xem `n` có phải là lũy thừa của 2 không.
- Ý tưởng: Nếu `n == 1` thì đúng. Nếu `n <= 0` hoặc `n` là số lẻ khác 1 thì sai. Nếu không, tiếp tục kiểm tra `n / 2`.
- Lỗi sai / điểm cần nhớ: Không được `return n / 2` trong hàm bool, vì số khác 0 sẽ bị hiểu là `true`. Phải gọi lại hàm: `return isPowerOfTwo(n / 2)`.
- Pattern: Recursive Reduction
- Độ phức tạp: Time O(log n), Space O(log n) nếu dùng recursion.
- Ngày cần làm lại: 2026-07-06


## 2026-07-04

### 40. Reverse String

- Link: https://leetcode.com/problems/reverse-string/
- Topic: Two Pointers, String, Recursion
- Độ khó: Easy
- Ngày làm: 2026-07-04
- Trạng thái: Solved
- Dịch đề: Cho một mảng ký tự, đảo ngược mảng đó ngay trong mảng ban đầu, không tạo mảng mới.
- Ý tưởng: Dùng recursion với hai con trỏ `left` và `right`. Nếu `left >= right` thì dừng. Ngược lại, swap hai ký tự ở hai đầu rồi gọi tiếp với `left + 1` và `right - 1`.
- Lỗi sai / điểm cần nhớ: Cần viết hàm phụ `helper` để truyền thêm `left` và `right`, vì hàm chính của LeetCode chỉ nhận `vector<char>& s`.
- Pattern: Recursive Two Pointers
- Độ phức tạp: Time O(n), Space O(n) do recursion call stack
- Ngày cần làm lại: 2026-07-07

### 41. Add Digits

- Link: https://leetcode.com/problems/add-digits/
- Topic: Math, Recursion
- Độ khó: Easy
- Ngày làm: 2026-07-04
- Trạng thái: Solved
- Dịch đề: Cho một số nguyên `num`, lặp lại việc cộng các chữ số của nó cho đến khi kết quả chỉ còn một chữ số.
- Ý tưởng: Nếu `num < 10` thì trả về luôn. Nếu không, tính tổng các chữ số của `num`, rồi gọi lại `addDigits(sumDigits)`.
- Lỗi sai / điểm cần nhớ: Không nên để `sumDigits` bên ngoài hàm vì sẽ bị cộng dồn qua các lần gọi đệ quy. Base case phải check `num < 10`, không phải check `sumDigits`.
- Pattern: Recursive Reduction
- Độ phức tạp: Time O(log n) cho mỗi lần tính tổng chữ số, Space O(log n) nếu dùng recursion
- Ngày cần làm lại: 2026-07-07


## 2026-07-06

### 42. Maximum Depth of Binary Tree

- Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
- Topic: Tree, DFS, Recursion, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-06
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, trả về độ sâu lớn nhất của cây. Độ sâu lớn nhất là số node trên đường đi dài nhất từ root xuống node lá.
- Ý tưởng: Dùng recursion. Nếu root là nullptr thì trả về 0. Nếu không, tính độ sâu cây trái và cây phải, rồi trả về 1 + max(leftDepth, rightDepth).
- Lỗi sai:
- Pattern: Tree DFS Recursion
- Độ phức tạp: Time O(n), Space O(h), với h là chiều cao cây
- Ngày cần làm lại: 2026-07-09

### 43. Same Tree

- Link: https://leetcode.com/problems/same-tree/
- Topic: Tree, DFS, Recursion, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-06
- Trạng thái: Solved
- Dịch đề: Cho hai cây nhị phân p và q, kiểm tra xem chúng có giống hệt nhau về cấu trúc và giá trị hay không.
- Ý tưởng: Dùng recursion để so sánh từng cặp node. Nếu cả hai đều nullptr thì giống. Nếu chỉ một bên nullptr thì khác. Nếu cả hai tồn tại thì so sánh giá trị, rồi tiếp tục so sánh cây trái và cây phải.
- Lỗi sai:
- Pattern: Compare Two Trees
- Độ phức tạp: Time O(n), Space O(h)
- Ngày cần làm lại: 2026-07-09

## 2026-07-07

### 44. Invert Binary Tree

- Link: https://leetcode.com/problems/invert-binary-tree/
- Topic: Tree, DFS, Recursion, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-07
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, đảo ngược cây như soi gương bằng cách đổi chỗ cây con trái và cây con phải ở mỗi node.
- Ý tưởng: Dùng recursion. Nếu root là nullptr thì trả về nullptr. Nếu không, swap root->left và root->right, rồi tiếp tục invert hai cây con.
- Lỗi sai / điểm cần nhớ: Invert Tree không cần tạo node mới. Chỉ cần đổi mũi tên left/right. Nếu dùng cách lưu `leftInverted` và `rightInverted`, đó chỉ là lưu địa chỉ cây con sau khi recursion xử lý xong, không phải tạo node mới.
- Pattern: Tree Transformation
- Độ phức tạp: Time O(n), Space O(h)
- Ngày cần làm lại: 2026-07-10

### 45. Symmetric Tree

- Link: https://leetcode.com/problems/symmetric-tree/
- Topic: Tree, DFS, BFS, Recursion, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-07
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, kiểm tra xem cây có đối xứng qua trục giữa hay không.
- Ý tưởng: Kiểm tra cây trái và cây phải có phải ảnh gương của nhau không. Hai node mirror phải có giá trị bằng nhau, và left->left phải mirror với right->right, left->right phải mirror với right->left.
- Lỗi sai / điểm cần nhớ: So sánh đối xứng không phải left với left, right với right. Phải so sánh ngoài với ngoài và trong với trong: `left->left` với `right->right`, `left->right` với `right->left`.
- Pattern: Mirror Recursion
- Độ phức tạp: Time O(n), Space O(h)
- Ngày cần làm lại: 2026-07-10

## 2026-07-08

### 46. Binary Tree Inorder Traversal

- Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
- Topic: Stack, Tree, DFS, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-08
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, trả về danh sách giá trị các node theo thứ tự inorder.
- Ý tưởng: Inorder nghĩa là duyệt cây trái, lấy giá trị node hiện tại, rồi duyệt cây phải. Dùng recursion và vector `res` để lưu kết quả.
- Lỗi sai / điểm cần nhớ: Inorder là `Left -> Root -> Right`, nên `res.push_back(root->val)` nằm giữa hai lần gọi dfs.
- Pattern: Inorder Traversal
- Độ phức tạp: Time O(n), Space O(h) nếu không tính vector kết quả
- Ngày cần làm lại: 2026-07-11

### 47. Binary Tree Preorder Traversal

- Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
- Topic: Stack, Tree, DFS, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-08
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, trả về danh sách giá trị các node theo thứ tự preorder.
- Ý tưởng: Preorder nghĩa là lấy giá trị node hiện tại trước, rồi duyệt cây trái, sau đó duyệt cây phải. Dùng recursion và vector `res` để lưu kết quả.
- Lỗi sai / điểm cần nhớ: Preorder là `Root -> Left -> Right`, nên `res.push_back(root->val)` nằm đầu hàm dfs, sau base case.
- Pattern: Preorder Traversal
- Độ phức tạp: Time O(n), Space O(h) nếu không tính vector kết quả
- Ngày cần làm lại: 2026-07-11

## 2026-07-09

### 48. Binary Tree Postorder Traversal

- Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
- Topic: Stack, Tree, DFS, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-09
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, trả về danh sách giá trị các node theo thứ tự postorder.
- Ý tưởng: Postorder nghĩa là duyệt cây trái, duyệt cây phải, rồi mới lấy giá trị node hiện tại. Dùng recursion và vector `res` để lưu kết quả.
- Lỗi sai:
- Pattern: Postorder Traversal
- Độ phức tạp: Time O(n), Space O(h) nếu không tính vector kết quả
- Ngày cần làm lại: 2026-07-12

### 49. Path Sum

- Link: https://leetcode.com/problems/path-sum/
- Topic: Tree, DFS, Recursion, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-09
- Trạng thái: Solved
- Dịch đề: Cho cây nhị phân và số `targetSum`, kiểm tra xem có đường đi từ root đến leaf sao cho tổng giá trị các node bằng `targetSum` không.
- Ý tưởng: Dùng recursion. Mỗi lần đi xuống một node thì trừ `root->val` khỏi targetSum. Khi gặp node lá, kiểm tra targetSum có bằng giá trị node lá không.
- Lỗi sai:
- Pattern: Root-to-Leaf DFS
- Độ phức tạp: Time O(n), Space O(h)
- Ngày cần làm lại: 2026-07-12
  
## 2026-07-10

### 50. Minimum Depth of Binary Tree

- Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
- Topic: Tree, DFS, BFS, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-10
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, trả về độ sâu nhỏ nhất từ root đến một node lá.
- Ý tưởng: Dùng recursion. Nếu root rỗng thì trả về 0. Nếu là node lá thì trả về 1. Nếu chỉ có một bên con thì phải đi theo bên có con, không được lấy min với 0.
- Lỗi sai / điểm cần nhớ: Minimum Depth là đường ngắn nhất từ root đến node lá, không phải đến nullptr gần nhất.
- Pattern: Tree Depth DFS
- Độ phức tạp: Time O(n), Space O(h)
- Ngày cần làm lại: 2026-07-13

### 51. Balanced Binary Tree

- Link: https://leetcode.com/problems/balanced-binary-tree/
- Topic: Tree, DFS, Recursion, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-10
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, kiểm tra cây có balanced hay không. Balanced nghĩa là tại mọi node, chiều cao cây trái và cây phải lệch nhau không quá 1.
- Ý tưởng: Tính chiều cao cây trái và cây phải tại mỗi node. Nếu lệch quá 1 thì false. Sau đó kiểm tra tiếp cả cây trái và cây phải.
- Lỗi sai / điểm cần nhớ: Không chỉ kiểm tra root. Cần kiểm tra mọi node, nên phải return `isBalanced(root->left) && isBalanced(root->right)`.
- Pattern: Height Check
- Độ phức tạp: Bản dễ hiểu Time O(n^2) trong trường hợp xấu, Space O(h)
- Ngày cần làm lại: 2026-07-13


## 2026-07-11

### 52. Sum of Left Leaves

- Link: https://leetcode.com/problems/sum-of-left-leaves/
- Topic: Tree, DFS, BFS, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-11
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, tính tổng giá trị của tất cả node lá nằm bên trái cha của nó.
- Ý tưởng: Duyệt cây bằng recursion. Ở mỗi node, kiểm tra xem `root->left` có tồn tại và có phải node lá không. Nếu đúng thì cộng `root->left->val` vào kết quả.
- Lỗi sai / điểm cần nhớ: Không cộng mọi node. Chỉ cộng node thỏa hai điều kiện: là node lá và là con trái của cha nó.
- Pattern: Tree DFS with Condition
- Độ phức tạp: Time O(n), Space O(h)
- Ngày cần làm lại: 2026-07-14

### 53. Diameter of Binary Tree

- Link: https://leetcode.com/problems/diameter-of-binary-tree/
- Topic: Tree, DFS, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-11
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, trả về đường kính của cây. Đường kính là số cạnh trên đường đi dài nhất giữa hai node bất kỳ.
- Ý tưởng: Tại mỗi node, đường đi dài nhất đi qua node đó bằng `height(left) + height(right)`. Dùng biến `ans` để lưu giá trị lớn nhất trong quá trình tính height.
- Lỗi sai / điểm cần nhớ: `ans = max(ans, leftHeight + rightHeight)` dùng để cập nhật đường kính. `return 1 + max(leftHeight, rightHeight)` dùng để trả chiều cao cho node cha. Diameter lấy cả hai bên, height chỉ chọn một bên dài nhất.
- Pattern: Tree Height + Global Answer
- Độ phức tạp: Time O(n), Space O(h)
- Ngày cần làm lại: 2026-07-14

## 2026-07-13

### 54. Search in a Binary Search Tree

- Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
- Topic: Tree, Binary Search Tree, DFS, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-13
- Trạng thái: Solved
- Dịch đề: Cho root của một Binary Search Tree và một giá trị `val`, tìm node có giá trị bằng `val`. Nếu tìm thấy thì trả về node đó, nếu không thì trả về nullptr.
- Ý tưởng: Dựa vào tính chất BST. Nếu `val` nhỏ hơn `root->val` thì tìm bên trái. Nếu lớn hơn thì tìm bên phải. Nếu bằng thì trả về root.
- Lỗi sai / điểm cần nhớ: Không được `return root->left` hoặc `root->right` ngay, vì node cần tìm có thể nằm sâu hơn. Phải gọi tiếp `searchBST(root->left/right, val)`.
- Pattern: BST Search
- Độ phức tạp: Time O(h), Space O(h) nếu dùng recursion
- Ngày cần làm lại: 2026-07-16

### 55. Range Sum of BST

- Link: https://leetcode.com/problems/range-sum-of-bst/
- Topic: Tree, Binary Search Tree, DFS, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-13
- Trạng thái: Solved
- Dịch đề: Cho một BST và hai số `low`, `high`, tính tổng tất cả node có giá trị nằm trong đoạn `[low, high]`.
- Ý tưởng: Dựa vào tính chất BST để bỏ nhánh không cần xét. Nếu node hiện tại nhỏ hơn `low` thì chỉ đi phải. Nếu lớn hơn `high` thì chỉ đi trái. Nếu nằm trong đoạn thì cộng node hiện tại và xét cả hai bên.
- Lỗi sai / điểm cần nhớ: Khi node nằm trong range, phải cộng node hiện tại và tiếp tục xét cả cây trái lẫn cây phải, không được return sum ngay.
- Pattern: BST Pruning
- Độ phức tạp: Time O(n) trường hợp xấu, Space O(h)
- Ngày cần làm lại: 2026-07-16


## 2026-07-14

### 56. Minimum Absolute Difference in BST

- Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
- Topic: Tree, DFS, Binary Search Tree, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-14
- Trạng thái: Solved
- Dịch đề: Cho một BST, tìm hiệu tuyệt đối nhỏ nhất giữa giá trị của hai node bất kỳ.
- Ý tưởng: Duyệt inorder để lấy giá trị theo thứ tự tăng dần. Vì mảng đã tăng dần nên hiệu nhỏ nhất chỉ cần xét giữa hai phần tử kề nhau.
- Lỗi sai / điểm cần nhớ: BST duyệt inorder sẽ ra dãy tăng dần.
- Pattern: BST Inorder Sorted
- Độ phức tạp: Time O(n), Space O(n)
- Ngày cần làm lại: 2026-07-17

### 57. Increasing Order Search Tree

- Link: https://leetcode.com/problems/increasing-order-search-tree/
- Topic: Tree, DFS, Binary Search Tree, Binary Tree
- Độ khó: Easy
- Ngày làm: 2026-07-14
- Trạng thái: Solved
- Dịch đề: Cho một BST, sắp xếp lại cây thành dạng tăng dần sao cho node nhỏ nhất đứng đầu, mỗi node chỉ có con phải và không có con trái.
- Ý tưởng: Duyệt inorder để lấy các node theo thứ tự tăng dần, sau đó nối các node lại bằng con trỏ right và đặt left của mỗi node thành nullptr.
- Lỗi sai / điểm cần nhớ: Nếu dùng `vector<TreeNode*>` thì phải `push_back(root)`, không phải `push_back(root->val)`, vì cần lưu node thật để nối lại cây.
- Pattern: BST Inorder Rebuild
- Độ phức tạp: Time O(n), Space O(n)
- Ngày cần làm lại: 2026-07-17

## 2026-07-15

### 58. Validate Binary Search Tree

- Link: https://leetcode.com/problems/validate-binary-search-tree/
- Topic: Tree, DFS, Binary Search Tree, Binary Tree
- Độ khó: Medium
- Ngày làm: 2026-07-15
- Trạng thái: Solved
- Dịch đề: Cho một cây nhị phân, kiểm tra xem cây đó có phải là Binary Search Tree hợp lệ không.
- Ý tưởng: Duyệt inorder để lấy giá trị node theo thứ tự. Với BST hợp lệ, kết quả inorder phải là dãy tăng nghiêm ngặt.
- Lỗi sai / điểm cần nhớ: Khi kiểm tra vector inorder, phải tránh truy cập vượt mảng. Nên duyệt từ `i = 1` và so sánh `res[i] <= res[i - 1]`.
- Pattern: BST Validation by Inorder
- Độ phức tạp: Time O(n), Space O(n)
- Ngày cần làm lại: 2026-07-18

### 59. Two Sum IV - Input is a BST

- Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
- Topic: Tree, DFS, BFS, Binary Search Tree, Two Pointers
- Độ khó: Easy
- Ngày làm: 2026-07-15
- Trạng thái: Solved
- Dịch đề: Cho một BST và số `k`, kiểm tra xem có hai node khác nhau trong cây có tổng bằng `k` không.
- Ý tưởng: Duyệt inorder để lấy mảng tăng dần, sau đó dùng two pointers để tìm hai số có tổng bằng `k`.
- Lỗi sai / điểm cần nhớ: Vì cần hai node khác nhau nên dùng điều kiện `left < right`, không dùng `left <= right`.
- Pattern: BST Inorder + Two Pointers
- Độ phức tạp: Time O(n), Space O(n)
- Ngày cần làm lại: 2026-07-18


## 2026-07-16

### 60. Lowest Common Ancestor of a Binary Search Tree

- Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- Topic: Tree, Binary Search Tree, DFS, Binary Tree
- Độ khó: Medium
- Ngày làm: 2026-07-16
- Trạng thái: Solved
- Dịch đề: Cho một BST và hai node p, q, tìm tổ tiên chung thấp nhất của hai node đó.
- Ý tưởng: Dựa vào tính chất BST. Nếu cả p và q nhỏ hơn root thì đi trái. Nếu cả hai lớn hơn root thì đi phải. Nếu chúng nằm khác phía hoặc một node bằng root thì root là đáp án.
- Lỗi sai / điểm cần nhớ: Node có thể là tổ tiên của chính nó. Có thể thêm `if (root == nullptr) return nullptr;` để code an toàn hơn.
- Pattern: BST Navigation
- Độ phức tạp: Time O(h), Space O(h) nếu dùng recursion
- Ngày cần làm lại: 2026-07-19

### 61. Convert Sorted Array to Binary Search Tree

- Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
- Topic: Array, Divide and Conquer, Tree, Binary Search Tree
- Độ khó: Easy
- Ngày làm: 2026-07-16
- Trạng thái: Solved
- Dịch đề: Cho một mảng đã sắp xếp tăng dần, chuyển nó thành một cây BST cân bằng chiều cao.
- Ý tưởng: Chọn phần tử giữa làm root. Nửa trái của mảng tạo cây con trái, nửa phải tạo cây con phải. Dùng recursion để xây cây.
- Lỗi sai / điểm cần nhớ: Bài này input là mảng, chưa có node sẵn, nên cần `new TreeNode(nums[mid])` để tạo node mới.
- Pattern: Divide and Conquer Build Tree
- Độ phức tạp: Time O(n), Space O(log n) nếu cây cân bằng, chưa tính cây kết quả
- Ngày cần làm lại: 2026-07-19

## 2026-07-18

### 64. Trim a Binary Search Tree

- Link: https://leetcode.com/problems/trim-a-binary-search-tree/
- Topic: Tree, Binary Search Tree, DFS, Binary Tree
- Độ khó: Medium
- Ngày làm: 2026-07-18
- Trạng thái: Solved
- Dịch đề: Cho một BST và hai số `low`, `high`, cắt cây sao cho chỉ còn các node có giá trị nằm trong đoạn `[low, high]`.
- Ý tưởng: Dựa vào tính chất BST. Nếu node hiện tại nhỏ hơn `low` thì bỏ node đó và cây trái, chỉ xét cây phải. Nếu node hiện tại lớn hơn `high` thì bỏ node đó và cây phải, chỉ xét cây trái. Nếu node nằm trong range thì giữ lại và trim tiếp hai cây con.
- Lỗi sai / điểm cần nhớ: Khi node nằm trong range thì không chỉ return root ngay, mà phải gắn lại `root->left = trimBST(...)` và `root->right = trimBST(...)`.
- Pattern: BST Pruning
- Độ phức tạp: Time O(n), Space O(h)
- Ngày cần làm lại: 2026-07-21

### 65. Delete Node in a BST

- Link: https://leetcode.com/problems/delete-node-in-a-bst/
- Topic: Tree, Binary Search Tree, Binary Tree
- Độ khó: Medium
- Ngày làm: 2026-07-18
- Trạng thái: Solved
- Dịch đề: Cho một BST và giá trị `key`, xóa node có giá trị bằng `key` sao cho cây sau khi xóa vẫn là BST.
- Ý tưởng: Tìm node cần xóa bằng tính chất BST. Nếu node không có con trái thì trả về cây phải. Nếu không có con phải thì trả về cây trái. Nếu có cả hai con thì lấy node nhỏ nhất bên cây phải để thay thế.
- Lỗi sai / điểm cần nhớ: Khi đi tìm key ở cây trái/phải, phải gắn lại `root->left = deleteNode(...)` hoặc `root->right = deleteNode(...)`, không được return cây con trực tiếp làm mất root. Với node có hai con, copy successor lên rồi xóa successor cũ ở cây phải.
- Pattern: BST Delete
- Độ phức tạp: Time O(h), Space O(h) nếu dùng recursion
- Ngày cần làm lại: 2026-07-21


## 2026-07-19

### Review - Insert into a Binary Search Tree

- Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
- Topic: Tree, Binary Search Tree, Recursion
- Trạng thái: Reviewed
- Ý tưởng: Nếu gặp `nullptr` thì tạo node mới bằng `new TreeNode(val)`. Nếu `val` nhỏ hơn root thì chèn vào trái, nếu lớn hơn thì chèn vào phải.
- Lỗi sai / điểm cần nhớ: Vì bài này làm thay đổi cây, phải gắn kết quả đệ quy lại: `root->left = insertIntoBST(...)` hoặc `root->right = insertIntoBST(...)`, rồi `return root`.

### Review - BST Return Pattern

- Ghi nhớ:
  - Tìm / tính / kiểm tra -> return kết quả trực tiếp.
  - Sửa / chèn / xóa / cắt / dựng cây -> gắn lại con trỏ rồi return root.
 
## 2026-07-20

### 66. Last Stone Weight

- Link: https://leetcode.com/problems/last-stone-weight/
- Topic: Heap, Priority Queue
- Độ khó: Easy
- Ngày làm: 2026-07-20
- Trạng thái: Solved
- Dịch đề: Cho một mảng trọng lượng các viên đá. Mỗi lượt lấy hai viên nặng nhất ra đập nhau. Nếu bằng nhau thì cả hai biến mất, nếu khác nhau thì viên còn lại có trọng lượng bằng hiệu của hai viên. Trả về trọng lượng viên cuối cùng hoặc 0 nếu không còn viên nào.
- Ý tưởng: Dùng `priority_queue<int>` để luôn lấy được viên đá nặng nhất. Mỗi vòng pop hai viên lớn nhất, nếu khác nhau thì push lại hiệu.
- Lỗi sai / điểm cần nhớ: `pq.pop()` không trả về giá trị. Muốn lấy giá trị phải dùng `pq.top()` trước rồi mới `pq.pop()`.
- Pattern: Max Heap Simulation
- Độ phức tạp: Time O(n log n), Space O(n)
- Ngày cần làm lại: 2026-07-23

### 67. Kth Largest Element in an Array

- Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
- Topic: Heap, Priority Queue, Sorting
- Độ khó: Medium
- Ngày làm: 2026-07-20
- Trạng thái: Solved
- Dịch đề: Cho mảng `nums` và số `k`, trả về phần tử lớn thứ k trong mảng.
- Ý tưởng: Có thể dùng max heap bằng cách push toàn bộ phần tử vào `priority_queue`, pop `k - 1` lần rồi return `pq.top()`. Cách tối ưu hơn là dùng min heap size k để chỉ giữ lại k phần tử lớn nhất.
- Lỗi sai / điểm cần nhớ: `priority_queue<int>` mặc định là max heap. Nếu muốn min heap thì dùng `priority_queue<int, vector<int>, greater<int>>`.
- Pattern: Kth Element with Heap
- Độ phức tạp: Max heap toàn bộ Time O(n log n), Space O(n). Min heap size k Time O(n log k), Space O(k).
- Ngày cần làm lại: 2026-07-23


## 2026-07-21

### 68. Top K Frequent Elements

- Link: https://leetcode.com/problems/top-k-frequent-elements/
- Topic: Hash Table, Heap, Priority Queue
- Độ khó: Medium
- Ngày làm: 2026-07-21
- Trạng thái: Solved
- Dịch đề: Cho mảng `nums` và số `k`, trả về `k` phần tử xuất hiện nhiều nhất trong mảng.
- Ý tưởng: Dùng `unordered_map` để đếm tần suất xuất hiện của từng số. Sau đó dùng `priority_queue<pair<int,int>>` để lấy các phần tử có tần suất cao nhất.
- Lỗi sai / điểm cần nhớ: `priority_queue<pair<int,int>>` ưu tiên `.first` trước. Muốn ưu tiên theo tần suất thì phải push `{count, num}`, sau đó lấy `pq.top().second`.
- Pattern: Frequency Map + Max Heap
- Độ phức tạp: Time O(n log n), Space O(n)
- Ngày cần làm lại: 2026-07-24

### 69. K Closest Points to Origin

- Link: https://leetcode.com/problems/k-closest-points-to-origin/
- Topic: Array, Math, Heap, Priority Queue
- Độ khó: Medium
- Ngày làm: 2026-07-21
- Trạng thái: Solved
- Dịch đề: Cho danh sách điểm `[x, y]`, trả về `k` điểm gần gốc tọa độ `(0,0)` nhất.
- Ý tưởng: Khoảng cách bình phương từ điểm đến gốc là `x*x + y*y`. Dùng max heap size `k` để giữ lại `k` điểm gần nhất. Nếu heap lớn hơn `k`, pop điểm xa nhất ra.
- Lỗi sai / điểm cần nhớ: Không cần dùng `sqrt`. So sánh `x*x + y*y` là đủ. Với `vector<vector<int>> points`, mỗi `point` là một `vector<int>` gồm `[x, y]`. Có thể dùng `auto point` hoặc tốt hơn là `const auto& point`.
- Pattern: K Closest with Heap
- Độ phức tạp: Time O(n log k), Space O(k)
- Ngày cần làm lại: 2026-07-24

## 2026-07-22

### 70. Kth Largest Element in a Stream

- Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
- Topic: Heap, Priority Queue, Design
- Độ khó: Easy
- Ngày làm: 2026-07-22
- Trạng thái: Solved
- Dịch đề: Thiết kế class KthLargest. Mỗi lần thêm một số mới vào stream, trả về phần tử lớn thứ k hiện tại.
- Ý tưởng: Dùng min heap size k để giữ lại k số lớn nhất. Vì là min heap nên `pq.top()` là số nhỏ nhất trong k số lớn nhất, tức là phần tử lớn thứ k.
- Lỗi sai / điểm cần nhớ: Phải gán `sizeK = k` trước vòng lặp. Nếu để trong vòng lặp, khi `nums` rỗng thì `sizeK` chưa được gán giá trị.
- Pattern: Min Heap Size K
- Độ phức tạp: Constructor O(n log k), add O(log k), Space O(k)
- Ngày cần làm lại: 2026-07-25

### 71. Relative Ranks

- Link: https://leetcode.com/problems/relative-ranks/
- Topic: Heap, Priority Queue, Sorting
- Độ khó: Easy
- Ngày làm: 2026-07-22
- Trạng thái: Solved
- Dịch đề: Cho mảng điểm số, trả về thứ hạng của từng người. Top 1, 2, 3 lần lượt nhận Gold Medal, Silver Medal, Bronze Medal.
- Ý tưởng: Dùng max heap lưu `{score, index}`. Heap lấy điểm cao nhất trước, còn `index` giúp điền kết quả về đúng vị trí ban đầu.
- Lỗi sai / điểm cần nhớ: `priority_queue<pair<int,int>>` ưu tiên `.first` trước. Nếu lưu `{score, index}` thì `pq.top().first` là điểm cao nhất, `pq.top().second` là vị trí ban đầu.
- Pattern: Max Heap Ranking
- Độ phức tạp: Time O(n log n), Space O(n)
- Ngày cần làm lại: 2026-07-25


## 2026-07-23

### 72. Sort Characters By Frequency

- Link: https://leetcode.com/problems/sort-characters-by-frequency/
- Topic: Hash Table, Heap, Priority Queue, Sorting
- Độ khó: Medium
- Ngày làm: 2026-07-23
- Trạng thái: Solved
- Dịch đề: Cho chuỗi `s`, hãy sắp xếp các ký tự theo tần suất xuất hiện giảm dần.
- Ý tưởng: Dùng `unordered_map<char,int>` để đếm tần suất từng ký tự. Sau đó dùng max heap `priority_queue<pair<int,char>>`, push `{count, char}` để lấy ký tự có tần suất cao nhất trước.
- Lỗi sai / điểm cần nhớ: Với `pair<int,char>`, heap ưu tiên `.first` trước, nên muốn ưu tiên tần suất thì phải để `count` ở `.first`.
- Pattern: Frequency Map + Max Heap
- Độ phức tạp: Time O(n log m), Space O(m), với `m` là số ký tự khác nhau.
- Ngày cần làm lại: 2026-07-26

### 73. The K Weakest Rows in a Matrix

- Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
- Topic: Matrix, Heap, Priority Queue, Sorting
- Độ khó: Easy
- Ngày làm: 2026-07-23
- Trạng thái: Solved
- Dịch đề: Cho ma trận gồm `1` là soldier và `0` là civilian, trả về index của `k` hàng yếu nhất. Hàng yếu hơn là hàng có ít soldier hơn.
- Ý tưởng: Đếm số soldier của từng hàng, sau đó dùng min heap lưu `{soldiers, index}` để lấy hàng yếu nhất trước.
- Lỗi sai / điểm cần nhớ: Khi đếm soldier phải kiểm tra `mat[i][j] == 1`, không được `soldiers++` cho mọi phần tử vì sẽ đếm cả số `0`.
- Pattern: Min Heap with Pair
- Độ phức tạp: Time O(m*n + m log m), Space O(m)
- Ngày cần làm lại: 2026-07-26
