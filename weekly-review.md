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
