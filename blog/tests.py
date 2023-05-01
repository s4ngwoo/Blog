from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post, PostCategory, PostSeries, PostTag

# Create your tests here.

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        # 1.1 포스트 목록 페이지를 가저옴.
        response = self.client.get('/')
        # 1.2 정상적으로 페이지가 로드 됨.
        self.assertEqual(response.status_code, 200)
        # 1.3 페이지 타이틀은 'Reinvent the wheel'이다.
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Reinvent the wheel')
        # 1.4 네비게이션 바가 있다.
        navbar = soup.nav
        # 1.5 'Home', 'About', 'Archive', 'Contact'라는 문구가 네비게이션 바에 있다.
        self.assertIn('Home', navbar.text)
        self.assertIn('About', navbar.text)
        self.assertIn('Archive', navbar.text)
        self.assertIn('Contact', navbar.text)

        # 2.1 메인 영역에 게시물이 하나도 없다면
        self.assertEqual(Post.objects.count(), 0)
        # 2.2 '아직 게시물이 없습니다.'라는 문구가 보인다.
        main_area = soup.find('div', id='main-area')
        self.assertIn('No Post.', main_area.text)
        
        # 3.1 게시물이 2개 있다면
        post_001 = Post.objects.create(
                title='first post.',
                subtitle='subtitle of first post',
                content = 'hello world!',
                branch = 1,
                )
        post_002 = Post.objects.create(
                title='second post.',
                subtitle='subtitle of second post',
                content = 'there are second all the time.',
                branch = 1,
                )
        self.assertEqual(Post.objects.count(), 2)

        # 3.2 포스트 목룍 페이지를 새로고침 했을때
        response = self.client.get('/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)
        # 3.3 메인 영역에 포스트 2개의 타이틀이 존재한다.
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        # 3.4 '아직 게시물이 없습니다.'라는 문구는 더이상 보이지 않는다.
        self.assertNotIn("No Post.", main_area.text)

    def test_post_detail(self):
        # 1.1 포스트가 하나 있다.
        category_001 = PostCategory.objects.create(
                title = 'cat',
                )
        series_001 = PostSeries.objects.create(
                title = 'se',
                )
        tag_001 = PostTag.objects.create(
                title = 'ta',
                )
        post_001 = Post.objects.create(
                title = 'first post.',
                subtitle = 'subtitle of first post.',
                content = 'content of first post.',
                branch = 1,
                category = category_001,
                series = series_001,
                tag = tag_001,
                )
        # 1.2 그 포스트의 url은 '/1/' 이다.
        self.assertEqual(post_001.get_absolute_url(), '/1/')

        # 2. 첫 번째 포스트이 상세 페이지 테스트
        # 2.1 첫 번째 포스트의 url로 접근하면 정상적으로 작동한다
        response = self.client.get(post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 2.2 포스트 목록 페이지와 똑같은 내비게이션 바가 있다.
        navbar = soup.nav
        self.assertIn('Home', navbar.text)
        self.assertIn('About', navbar.text)
        self.assertIn('Archive', navbar.text)
        self.assertIn('Contact', navbar.text)

        # 2.3 첫 번째 포스트의 제목이 웹 브라우저 탭 타이틀에 들어 있다.
        self.assertIn(post_001.title, soup.title.text)

        # 2.4 첫 번째 포스트의 제목이 헤더의 타이틀 영역에 있다.
        header_area = soup.find('div', id='header-area')
        title_area = soup.find('div', id='title-area')
        self.assertIn(post_001.title, title_area.text)
        # 2.5 첫 번째 포스트의 내용(content)이 포스트 영역에 있다.
        post_area = soup.find('div', id='post-area')
        self.assertIn(post_001.content, post_area.text)
        # 2.6 첫 번째 포스트의 카테고리가 포스트 영역에 있다.
        self.assertIn(str(post_001.category), post_area.text)
        # 2.7 첫 번째 포스트의 시리즈가 포스트 영역에 있다.
        self.assertIn(str(post_001.series), post_area.text)
        # 2.8 첫 번째 포스트의 태그가 포스트 영역에 있다.
        self.assertIn(str(post_001.tag), post_area.text)


