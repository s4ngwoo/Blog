from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

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
                )
        post_002 = Post.objects.create(
                title='second post.',
                subtitle='subtitle of second post',
                content = 'there are second all the time.',
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
