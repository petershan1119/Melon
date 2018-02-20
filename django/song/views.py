from django.db.models import Q
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

    Song과 연결된 Artist의 name에 keyword가 포함되는 경우
    Song과 연결된 Album의 title에 keyword가 포함되는 경우
        를 모두 포함(or -> Q object)하는 쿼리셋을 'songs'에 할당

    songs_from_artists
    songs_from_albums
    songs_from_title
    위 세 변수에 위의 조건 3개에 부합하는 쿼리셋을 각각 전달
    세 변수를 이용해 검색 결과를 3단으로 분리해서 출력
        -> 아티스트로 검색한 노래 결과, 앨범으로 검색한 노래 결과, 제목으로 검색한 노래 결과
    """
    # context = {}
    # if request.method == 'POST':
    # print(request.GET)
    # print(type(request.GET))
    # print(request.GET['keyword'])

    keyword = request.GET.get('keyword')

    # keyword = request.POST['keyword'].strip()

    # if keyword:
    #     songs_from_artists = Song.objects.filter(album__artists__name__contains=keyword)
    #     songs_from_albums = Song.objects.filter(album__title__contains=keyword)
    #     songs_from_title = Song.objects.filter(title__contains=keyword)

        # songs = Song.objects.filter(
        #     Q(album__title__contains=keyword)|
        #     Q(album__artists__name__contains=keyword)|
        #     Q(title__contains=keyword)
        # ).distinct()

        # if not songs_from_artists:
        #     context['form_error1'] = "찾는 아티스트의 노래가 없습니다."
        # else:
        #     context['songs_from_artists'] = songs_from_artists
        # if not songs_from_albums:
        #     context['form_error2'] = "찾는 앨범의 노래가 없습니다."
        # else:
        #     context['songs_from_albums'] = songs_from_albums
        # if not songs_from_title:
        #     context['form_error3'] = "찾는 타이틀의 노래가 없습니다."
        # else:
        #     context['songs_from_title'] = songs_from_title

    # [ {'type'" '아티스트', 'songs': QuerySet<Song>},
    #   {'type': '앨범', 'songs': QuerySet<Song>},
    #   {'type': '타이틀', 'songs': QuerySet<Song>} ]

    context = {
        'song_infos': [],
    }
    if keyword:
        q1 = Q(album__artists__name__contains=keyword)
        q2 = Q(album__title__contains=keyword)
        q3 = Q(title__contains=keyword)
        # songs_from_artists = Song.objects.filter(album__artists__name__contains=keyword)
        # songs_from_albums = Song.objects.filter(album__title__contains=keyword)
        # songs_from_title = Song.objects.filter(title__contains=keyword)

        for type, q in zip(('아티스트명', '앨범명', '타이틀명'), (q1, q2, q3)):
            context['song_infos'].append({
                'type': type,
                'songs': Song.objects.filter(q),
            })
    return render(request, 'song/song_search.html', context)