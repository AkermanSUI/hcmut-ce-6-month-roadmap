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

