
from django.utils.safestring import mark_safe

class Pagenation:

    def __init__(self, current_page, total_count, cc=None):
        self.per_page_num = 10  # 每页展示10条数据
        self.cc = cc
        self.current_page = current_page

        total_page_number, b = divmod(total_count, self.per_page_num)  # 5
        # 总页码数量
        if b:
            total_page_number += 1

        show_page_number = 11  # 总共展示11个页码
        if total_page_number > show_page_number:
            half_page_number = show_page_number // 2
            if current_page <= half_page_number:
                page_number_start = 1
                page_number_end = show_page_number + 1

            elif (current_page + half_page_number) > total_page_number:
                page_number_start = total_page_number - show_page_number + 1
                page_number_end = total_page_number + 1

            else:
                page_number_start = current_page - half_page_number  # 11   6
                page_number_end = current_page + half_page_number + 1  # 16
            self.page_num_range = range(page_number_start, page_number_end)
        else:

            self.page_num_range = range(1, total_page_number+1)  # [1,2,3,4,5]

    @property
    def page_data_start(self):
        return (self.current_page - 1) * self.per_page_num

    @property
    def end_data_start(self):
        return self.current_page*self.per_page_num


    def page_html(self):
        page_html_start = '''
             <nav aria-label="Page navigation">
                  <ul class="pagination">
                    <li>
                      <a href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                      </a>
                    </li>
        '''

        for i in self.page_num_range:
            if self.cc:

                s = f'<li><a href="?page={i}&{self.cc}">{i}</a></li>'
            else:
                s = f'<li><a href="?page={i}">{i}</a></li>'
            page_html_start += s

        page_html_end = '''
            <li>
              <a href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </nav>
        '''
        page_all_html = page_html_start + page_html_end
        return mark_safe(page_all_html)

