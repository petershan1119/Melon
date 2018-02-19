from django.http import HttpResponse
from django.shortcuts import render
from song.models import Song

def song_list(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(request, 'song/song_list.html', context)


def song_search(request):
    """
    사용할 URL: song/search
    사용할 Template: templates/song/song_search.html
        form안에
            input한개, button한개 배치

    1. song/urls.py에 URL작성
    2. templates/song/song_search.html 작성
    3. 이 함수에서 return render(..)

    - GET, POST 분기
    1. input의 name을 keyword로 지정
    2. 이 함수를 request.method가 'GET'일 때와 'POST'일 때로 분기
    3. request.method가 'POST'일 때
        request.POST dict의 'keyword'키에 해당하는 값을
        HttpResponse로 출력
    4. request.method가 'GET'일 때
        이전에 하던 템플릿 출력을 유지

    - Query Filter로 검색하기
    1. keyword가 자신의 'title'에 포함되는 Song 쿼리셋 생성
    2. 위 쿼리셋을 'songs' 변수에 할당
    3. context dict를 만들고 'songs'키에 songs변수를 할당
    4. render의 3번째 인수로 context 전달
    5. templates에 전달된 'songs'를 출력
    """
    context = {}
    if request.method == 'POST':
        keyword = request.POST['keyword'].strip()
        songs = Song.objects.filter(title__contains=keyword)
        if not songs or not keyword:
            context['form_error'] = "찾는 노래가 없습니다."
        else:
            context = {
                'songs': songs,
            }
    return render(request, 'song/song_search.html', context)