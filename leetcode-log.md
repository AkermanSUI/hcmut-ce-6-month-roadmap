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
