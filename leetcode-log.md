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
