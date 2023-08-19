# Documents:

#### https://www.codehub.com.vn/Python-Co-Ban

## Naming convention:
Trong cộng đồng Python, có một số quy tắc đặt tên phổ biến mà nhiều người lập trình viên thường tuân theo. Những quy tắc này giúp mã nguồn trở nên dễ đọc và thống nhất hơn khi làm việc cùng nhau trong các dự án lớn. Dưới đây là một số quy tắc đặt tên phổ biến trong Python:

1. **Module và Package:**
   - Sử dụng chữ thường và dấu gạch dưới (`snake_case`) cho tên module và package.
   - Ví dụ: `my_module.py`, `my_package`.

2. **Biến và Hàm:**
   - Sử dụng chữ thường và dấu gạch dưới (`snake_case`) cho tên biến và hàm.
   - Ví dụ: `my_variable`, `calculate_total`.

3. **Lớp:**
   - Sử dụng chữ cái viết hoa đầu tiên (`CamelCase` hoặc `PascalCase`) cho tên lớp.
   - Ví dụ: `MyClass`, `DataProcessing`.

4. **Hằng số:**
   - Sử dụng chữ in hoa và dấu gạch dưới (`UPPER_CASE_WITH_UNDERSCORES`) cho tên hằng số.
   - Ví dụ: `MAX_VALUE`, `PI`.

5. **Biến dạng Private:**
   - Sử dụng dấu gạch dưới bắt đầu tên biến để chỉ ra rằng nó là biến "private" trong module (`_variable`).
   - Ví dụ: `_private_variable`.

6. **Biến Magic (Special Methods):**
   - Sử dụng hai dấu gạch dưới bắt đầu và kết thúc tên biến để chỉ ra các biến "magic" hoặc các phương thức đặc biệt (`__method__`).
   - Ví dụ: `__init__`, `__str__`.

7. **Biến Global:**
   - Tránh sử dụng tên biến gây nhầm lẫn với các từ khóa ngôn ngữ Python, như `str`, `list`, `int`, bằng cách thêm một dấu gạch dưới sau từ khóa (`str_`, `list_`).

8. **Tên dự án và thư mục:**
   - Sử dụng chữ thường và dấu gạch dưới (`snake_case`) cho tên thư mục và dự án.
   - Ví dụ: `my_project`, `data_processing`.

Nhớ rằng quy tắc đặt tên là một phần quan trọng của coding convention và có thể thay đổi tùy theo dự án hoặc tổ chức. Nếu bạn đang làm việc trong một dự án cụ thể, hãy kiểm tra xem liệu có quy tắc đặt tên cụ thể nào bạn cần tuân theo.