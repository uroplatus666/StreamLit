import plotly.express as px
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import pydeck as pdk
#from streamlit_extras.let_it_rain import rain


@st.cache_resource()
def load_model_1(model_name_1):
    rosgran = pd.read_csv(model_name_1)
    return (rosgran)


rosgran = load_model_1('https://raw.githubusercontent.com/uroplatus666/StreamLit/master/data/rosgran.csv')


@st.cache_resource()
def load_model_2(model_name_2):
    all_df_copy = pd.read_csv(model_name_2)
    return (all_df_copy)


all_df_copy = load_model_2('https://raw.githubusercontent.com/uroplatus666/refs/heads/StreamLit/master/data/all_df_copy.csv')

@st.cache_resource()
def load_model_3(model_name_3):
    people_zero = pd.read_csv(model_name_3)
    return (people_zero)


people_zero = load_model_3('https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/people_zero.csv')


@st.cache_resource()
def load_model_4(model_name_4):
    places_copy = pd.read_csv(model_name_4)
    return (places_copy)


places_copy = load_model_4('https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/places_copy.csv')


@st.cache_resource()
def load_model_5(model_name_5):
    push = pd.read_csv(model_name_5)
    return (push)


push = load_model_5('https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/push.csv')


@st.cache_resource()
def load_model_6(model_name_6):
    controls_else = pd.read_csv(model_name_6)
    return (controls_else)


controls_else = load_model_6('https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/controls_else.csv')


@st.cache_resource()
def load_model_7(model_name_7):
    places_count = pd.read_csv(model_name_7)
    return (places_count)


places_count = load_model_7('https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/places_count.csv')


@st.cache_resource()
def load_model_8(model_name_8):
    rosgran_count = pd.read_csv(model_name_8)
    return (rosgran_count)


rosgran_count = load_model_8('https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/rosgran_count.csv')


@st.cache_resource()
def load_model_9(model_name_9):
    country_else = pd.read_csv(model_name_9)
    return (country_else)


country_else = load_model_9('https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/country_else.csv')


@st.cache_resource()
def load_model_10(model_name_10):
    Center = pd.read_csv(model_name_10)
    return (Center)


Center = load_model_10('https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/Center.csv')


@st.cache_resource()
def load_model_11(model_name_11):
    ANN = pd.read_csv(model_name_11)
    return (ANN)


ANN = load_model_11('https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/ANN.csv')


@st.cache_resource()
def load_model_12(model_name_12):
    all_df_copy_na = pd.read_csv(model_name_12)
    return (all_df_copy_na)


all_df_copy_na = load_model_12(
    'https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/all_df_copy_na.csv')


@st.cache_resource()
def load_model_13(model_name_13):
    all_df_copy_places = pd.read_csv(model_name_13)
    return (all_df_copy_places)


all_df_copy_places = load_model_13(
    'https://raw.githubusercontent.com/uroplatus666/StreamLit/refs/heads/master/data/all_df_copy_places.csv')

# 4. Manual item selection
if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1)
    manual_select = st.session_state['menu_option']
    st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) - 1)
else:
    manual_select = None

selected = option_menu(
    menu_title='Меню',
    options=['Карты', 'Статистика по Федеральным округам',
             'Статистика по участкам'],
    icons=['geo-alt', 'bar-chart', 'flag'],
    menu_icon='tencent-qq',
    default_index=0,
    orientation='horizontal',
    manual_select=manual_select,
    key='menu',
)

if selected == 'Карты':
    with st.container():
        st.subheader('***Количество пересечений государственной границы России через пограничные пункты пропуска***',
                     divider='blue')
        category = st.selectbox(
            '**:gray[Выберите категорию:]**',
            ('Число людей', 'Легковые транспортные средства',
             'Грузовые транспортные средства',
             'Паспорта транспортных средств', 'Грузы в тоннах'))

        if category == 'Число людей':
            elevation = 0.13
        elif category == 'Легковые транспортные средства':
            elevation = 1.5
        elif category == 'Грузовые транспортные средства':
            elevation = 5
        elif category == 'Паспорта транспортных средств':
            elevation = 15
        elif category == 'Грузы в тоннах':
            elevation = 1.5

        col1, col2 = st.columns([7, 1])

        with col2:
            year = st.radio(
                "**:blue[Выберите год]**",
                [2017, 2018, 2019, 2020, 2021, 2022])
        with col1:
            st.pydeck_chart(pdk.Deck(
                initial_view_state=pdk.ViewState(
                    latitude=55.7522,
                    longitude=37.6156,
                    zoom=2,
                    pitch=50,
                ),
                layers=[pdk.Layer('ColumnLayer',
                                  data=all_df_copy[
                                      (all_df_copy['Категория'] == category) & (all_df_copy['Год'] == year)],
                                  get_position='[longitude, latitude]',
                                  radius=6000,
                                  elevation_scale=elevation,
                                  get_color='[31, 174, 233, 160]',
                                  get_elevation='Количество',
                                  pickable=True,
                                  extruded=True,
                                  ),
                        ],

                tooltip={
                    "html": "<b>{Вид}</b> <b>{Наименование пункта пропуска}</b>, количество пересечений: <b>{Количество}</b> единиц в год",
                    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial',
                              "z-index": "10000"},
                }
            ))
        st.write('**:grey[Описание]	:thinking_face:**')
        st.write(
            'Каждая колонка на карте – количество пересечений выбранной категории за выбранный год данного пропускного пункта. ' + \
            'Размер колонки прямо пропорционален количеству пересечений.')
    st.write('---')
    with st.container():

        st.subheader('***Перегруженные пропускные пункты***', divider='red')
        categoryy = st.selectbox(
            '**:gray[Выберите интересующую категорию:]**',
            ('Число людей', 'Легковые транспортные средства',
             'Грузовые транспортные средства',
             'Паспорта транспортных средств',
             'Грузы в тоннах'))

        col1, col2 = st.columns([7, 1])

        with col2:
            year = st.radio(
                "**:red[Выберите год]**",
                [2017, 2018, 2019, 2020, 2021, 2022])
        with col1:
            if categoryy == 'Число людей':
                if year == 2017:
                    st.write('**Количество перегруженных пропускных пунктов: :red[10]**')
                elif year == 2018:
                    st.write('**Количество перегруженных пропускных пунктов: :red[9]**')
                elif year == 2019:
                    st.write('**Количество перегруженных пропускных пунктов: :red[13]**')
                elif year == 2020:
                    st.write('**Количество перегруженных пропускных пунктов: :red[2]**')
                elif year == 2021:
                    st.write('**Количество перегруженных пропускных пунктов: :red[3]**')
                elif year == 2022:
                    st.write('**Количество перегруженных пропускных пунктов: :red[5]**')
            if categoryy == 'Легковые транспортные средства':
                if year == 2017:
                    st.write('**Количество перегруженных пропускных пунктов: :red[24]**')
                elif year == 2018:
                    st.write('**Количество перегруженных пропускных пунктов: :red[24]**')
                elif year == 2019:
                    st.write('**Количество перегруженных пропускных пунктов: :red[23]**')
                elif year == 2020:
                    st.write('**Количество перегруженных пропускных пунктов: :red[7]**')
                elif year == 2021:
                    st.write('**Количество перегруженных пропускных пунктов: :red[7]**')
                elif year == 2022:
                    st.write('**Количество перегруженных пропускных пунктов: :red[10]**')
            if categoryy == 'Грузовые транспортные средства':
                if year == 2017:
                    st.write('**Количество перегруженных пропускных пунктов: :red[20]**')
                elif year == 2018:
                    st.write('**Количество перегруженных пропускных пунктов: :red[22]**')
                elif year == 2019:
                    st.write('**Количество перегруженных пропускных пунктов: :red[23]**')
                elif year == 2020:
                    st.write('**Количество перегруженных пропускных пунктов: :red[21]**')
                elif year == 2021:
                    st.write('**Количество перегруженных пропускных пунктов: :red[23]**')
                elif year == 2022:
                    st.write('**Количество перегруженных пропускных пунктов: :red[26]**')
            if categoryy == 'Паспорта транспортных средств':
                if year == 2017:
                    st.write('**Количество перегруженных пропускных пунктов: :red[10]**')
                elif year == 2018:
                    st.write('**Количество перегруженных пропускных пунктов: :red[8]**')
                elif year == 2019:
                    st.write('**Количество перегруженных пропускных пунктов: :red[10]**')
                elif year == 2020:
                    st.write('**Количество перегруженных пропускных пунктов: :red[4]**')
                elif year == 2021:
                    st.write('**Количество перегруженных пропускных пунктов: :red[6]**')
                elif year == 2022:
                    st.write('**Количество перегруженных пропускных пунктов: :red[9]**')
            if categoryy == 'Грузы в тоннах':
                if year == 2017:
                    st.write('**Количество перегруженных пропускных пунктов: :red[10]**')
                elif year == 2018:
                    st.write('**Количество перегруженных пропускных пунктов: :red[8]**')
                elif year == 2019:
                    st.write('**Количество перегруженных пропускных пунктов: :red[10]**')
                elif year == 2020:
                    st.write('**Количество перегруженных пропускных пунктов: :red[4]**')
                elif year == 2021:
                    st.write('**Количество перегруженных пропускных пунктов: :red[6]**')
                elif year == 2022:
                    st.write('**Количество перегруженных пропускных пунктов: :red[9]**')
            st.pydeck_chart(pdk.Deck(
                initial_view_state=pdk.ViewState(
                    latitude=55.7522,
                    longitude=80.6156,
                    zoom=1.5,
                    pitch=50,
                ),
                layers=[pdk.Layer('ColumnLayer',
                                  data=all_df_copy_na[
                                      (all_df_copy_na['Категория'] == categoryy) & (all_df_copy_na['Год'] == year)],
                                  get_position='[longitude, latitude]',
                                  radius=20000,
                                  elevation_scale=1000,
                                  get_color='[205, 0, 0, 160]',
                                  get_elevation=1000,
                                  pickable=True,
                                  extruded=True,
                                  ),
                        ],

                tooltip={
                    "html": "<b>{Вид}</b> <b>{Наименование пункта пропуска}</b>, максимально допустимое количество пересечений превышено в <b>{Количество (Факт/Паспорт)}</b> раз(а)",
                    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial',
                              "z-index": "10000"},
                }
            ))
        st.write('**:grey[Описание]	:thinking_face:**')
        st.write('Каждая колонка на карте – перегруженный пропускной пункт. ' + \
                 'Размер колонок одинаковый.')
        question = st.checkbox('**:red[Какой пункт считается перегруженным]:grey_question:**')
        if question:
            st.write('**У каждого пункта пропуска есть максимальная установленная пропускная способность, ' + \
                     'но есть пропускные пункты, фактическое количество пересечений которых превышает максимально возморжное. ' + \
                     'Пропускной пункт считается перегруженным, ' + \
                     'если результат деления фактического количества пересечений на максимально возможно превышает единицу.**')
    st.write('---')

    with st.container():
        st.subheader('***Пропускные пункты с нулевым фактическим количеством пересечений***', divider='green')

        col1, col2 = st.columns([1, 7])
        with col1:
            st.write('')
            year_2 = st.radio(
                "**:green[Выберите год]**",
                [2017, 2018, 2019, 2020, 2021, 2022])
        with col2:
            col1, col2 = st.columns([1, 2.1])
            with col2:
                if year_2 == 2017:
                    st.markdown('''**:green[Функционирующие] :grey[пропускные пункты:] :green[19] :grey[единиц]**''')
                    st.markdown('''**:red[Не функционирующие] :grey[пропускные пункты:] :red[63] :grey[единицы]**''')
                elif year_2 == 2018:
                    st.markdown('''**:green[Функционирующие] :grey[пропускные пункты:] :green[24] :grey[единицы]**''')
                    st.markdown('''**:red[Не функционирующие] :grey[пропускные пункты:] :red[62] :grey[единицы]**''')
                elif year_2 == 2019:
                    st.markdown('''**:green[Функционирующие] :grey[пропускные пункты:] :green[20] :grey[единиц]**''')
                    st.markdown('''**:red[Не функционирующие] :grey[пропускные пункты:] :red[63] :grey[единицы]**''')
                elif year_2 == 2020:
                    st.markdown('''**:green[Функционирующие] :grey[пропускные пункты:] :green[24] :grey[единицы]**''')
                    st.markdown('''**:red[Не функционирующие] :grey[пропускные пункты:] :red[65] :grey[единиц]**''')
                elif year_2 == 2021:
                    st.markdown('''**:green[Функционирующие] :grey[пропускные пункты:] :green[62] :grey[единицы]**''')
                    st.markdown('''**:red[Не функционирующие] :grey[пропускные пункты:] :red[66] :grey[единиц]**''')
                elif year_2 == 2022:
                    st.markdown('''**:green[Функционирующие] :grey[пропускные пункты:] :green[30] :grey[единиц]**''')
                    st.markdown('''**:red[Не функционирующие] :grey[пропускные пункты:] :red[65] :grey[единиц]**''')

            st.pydeck_chart(pdk.Deck(
                initial_view_state=pdk.ViewState(
                    latitude=55.7522,
                    longitude=80.6156,
                    zoom=1.5,
                    pitch=50,
                ),
                layers=[pdk.Layer('ColumnLayer',
                                  data=places_copy[(places_copy['Категория'] == 'Число людей') &
                                                   (places_copy['Количество'] == 0) & (places_copy['Год'] == year_2)
                                                   & (places_copy['Функционирует/не функционирует'] == 'да')],
                                  get_position='[longitude, latitude]',
                                  radius_scale=900,
                                  get_color='[0, 168, 107, 210]',
                                  pickable=True,
                                  elevation=100000,
                                  elevation_scale=600,
                                  radius=10000,
                                  ),
                        pdk.Layer('ColumnLayer',
                                  data=places_copy[(places_copy['Категория'] == 'Число людей') &
                                                   (places_copy['Количество'] == 0) & (places_copy['Год'] == year_2)
                                                   & (places_copy['Функционирует/не функционирует'] == 'нет')],
                                  get_position='[longitude, latitude]',
                                  radius_scale=900,
                                  get_color='[204, 6, 5, 210]',
                                  pickable=True,
                                  elevation=100000,
                                  elevation_scale=600,
                                  radius=10000,
                                  ),
                        ],

                tooltip={
                    "html": '<b>{Вид}</b> <b>{Наименование пункта пропуска}</b>',
                    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial',
                              "z-index": "10000"},
                }

            ))
        st.write('**:grey[Описание]	:thinking_face:**')
        st.write('Каждая колонка на карте – функционирующий или не функционирующий пропускной пункт. ' + \
                 'Размер колонок одинаковый, цвет функционирующих пропускных пунктов - :green[зеленый], не функционирующих - :red[красный].')
    st.write('---')
    with st.container():
        st.subheader('***Классификация пропускных пунктов по режиму работы***', divider='blue')
        type = st.selectbox(
            '**:gray[Выберите режим работы пропускных пунктов:]**',
            ('Постоянный', 'Работающий на нерегулярной основе', 'Сезонный', 'Не определен', 'Временный'))
        if type == 'Постоянный':
            st.write('**Пропускных пунктов с :blue[постоянным] режимом работы :blue[298] штук**')
        elif type == 'Работающий на нерегулярной основе':
            st.write('**Пропускных пунктов с :blue[нерегулярным] режимом работы :blue[37] штук**')
        elif type == 'Сезонный':
            st.write('**Пропускных пунктов с :blue[сезонным] режимом работы :blue[16] штук**')
        elif type == 'Не определен':
            st.write('**Пропускных пунктов с :blue[не определенным] режимом работы :blue[16] штук**')
        elif type == 'Временный':
            st.write('**Пропускных пунктов с :blue[временным] режимом работы :blue[13] штук**')
        st.pydeck_chart(pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=55.7522,
                longitude=100.6156,
                zoom=1.5,
                pitch=50,
            ),

            layers=[pdk.Layer('ColumnLayer',
                              data=rosgran[(rosgran['Классификация по режиму работы'] == str.lower(type)) &
                                           ((rosgran['Сопредельное государство'] == 'Китайская Народная Республика') |
                                            (rosgran['Сопредельное государство'] == 'Финляндская Республика'))],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[72, 118, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[72, 118, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=rosgran[(rosgran['Классификация по режиму работы'] == str.lower(type)) &
                                           ((rosgran['Сопредельное государство'] == 'Республика Казахстан') |
                                            (rosgran['Сопредельное государство'] == 'Эстонская Республика'))],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[131, 111, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[131, 111, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=rosgran[(rosgran['Классификация по режиму работы'] == str.lower(type)) &
                                           ((rosgran['Сопредельное государство'] == 'Монголия') |
                                            (rosgran['Сопредельное государство'] == 'Латвийская Республика'))],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[240, 255, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[240, 255, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=rosgran[(rosgran['Классификация по режиму работы'] == str.lower(type)) &
                                           ((rosgran['Сопредельное государство'] == 'Республика Грузия') |
                                            (rosgran['Сопредельное государство'] == 'Королевство Норвегия'))],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[0, 0, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[0, 0, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=rosgran[(rosgran['Классификация по режиму работы'] == str.lower(type)) &
                                           ((rosgran['Сопредельное государство'] == 'Украина') |
                                            (rosgran['Сопредельное государство'] == 'утратило значение (Украина)'))],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[0, 245, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[0, 245, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=rosgran[(rosgran['Классификация по режиму работы'] == str.lower(type)) &
                                           ((rosgran[
                                                 'Сопредельное государство'] == 'Корейская Народно-Демократическая Республика') |
                                            (rosgran['Сопредельное государство'] == 'Республика Южная Осетия') |
                                            (rosgran['Сопредельное государство'] == 'Литовская Республика'))],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[127, 255, 212],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[127, 255, 212],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=rosgran[(rosgran['Классификация по режиму работы'] == str.lower(type)) &
                                           ((rosgran['Сопредельное государство'] == 'Республика Польша') |
                                            (rosgran['Сопредельное государство'] == 'Азербайджанская Республика'))],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[164, 211, 238],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[164, 211, 238],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=rosgran[(rosgran['Классификация по режиму работы'] == str.lower(type)) &
                                           (rosgran['Сосед'] == 'нет')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[255, 48, 48],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[255, 48, 48],
                              opacity=0.8
                              ),
                    ],

            tooltip={
                "html": '<b>{Вид}</b> <b>{Наименование пункта пропуска_y}</b>, \nсопредельное государство: <b>{Сосед}</b>',
                "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial',
                          "z-index": "10000"},
            }
        ))
        st.write('**:grey[Описание]	:thinking_face:**')
        st.write('Каждая колонка на карте – пропускной пункт с выбранным режимом работы. ' + \
                 'Размер колонок одинаковый.' + \
                 'Пропускные пункты, относящиеся к одному участку обозначены одним цветом, пропускные пункты, лежащие на разных участках, ' + \
                 'могут быть покрашены в один цвет, если они не являются соседними. ')

    st.write('---')
    with st.container():
        st.subheader('***Средневзвешенный центр распределения количества пересечений пропускных пунктов***',
                     divider='blue')
        category_ = st.selectbox(
            '**:gray[Выберите одну из категорий:]**',
            ('Число людей', 'Легковые транспортные средства',
             'Грузовые транспортные средства',
             'Паспорта транспортных средств', 'Грузы в тоннах'))
        st.pydeck_chart(pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=51.95957752,
                longitude=47.49039297,
                zoom=3,
                pitch=50,
            ),

            layers=[pdk.Layer('ColumnLayer',
                              data=Center[(Center['Категория'] == category_) &
                                          (Center['Год'] == '2017 год')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=75,
                              get_color='[0, 168, 107, 210]',
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[95, 103, 106],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=Center[(Center['Категория'] == category_) &
                                          (Center['Год'] == '2018 год')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=125,
                              get_color='[0, 168, 107, 210]',
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[79, 116, 126],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=Center[(Center['Категория'] == category_) &
                                          (Center['Год'] == '2019 год')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=175,
                              get_color='[0, 168, 107, 210]',
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[18, 127, 155],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=Center[(Center['Категория'] == category_) &
                                          (Center['Год'] == '2020 год')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color='[0, 168, 107, 210]',
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[11, 191, 237],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=Center[(Center['Категория'] == category_) &
                                          (Center['Год'] == '2021 год')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=275,
                              get_color='[0, 168, 107, 210]',
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[75, 215, 251],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=Center[(Center['Категория'] == category_) &
                                          (Center['Год'] == '2022 год')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=325,
                              get_color='[0, 168, 107, 210]',
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[160, 234, 253],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=Center[(Center['Категория'] == category_) &
                                          (Center['Год'] == 'Пропускная способность по паспорту')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=375,
                              get_color='[0, 168, 107, 210]',
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[7, 18, 246],
                              opacity=0.8
                              ),
                    ],

            tooltip={
                "html": '<b>{Год}</b>',
                "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial',
                          "z-index": "10000"},
            }

        ))
        st.write('**:grey[Описание]	:thinking_face:**')
        st.write('Каждая колонка на карте – средневзвешенное всех пересечений выбранной категории и года, ' + \
                 'ее размер увеличивается и цвет становится светлее при увеличении года,' + \
                 'пропускную способность по паспорту в каждой категории отображает самая высокая колонка ярко-синего цвета.')

        what = st.checkbox('**:blue[Что такое средневзвешенный центр]:grey_question:**')
        if what:
            st.write('**Средневзвешенный центр - точка,' + \
                     ' являющаяся средним местоположение всех объектов в наборе данных. Местоположение рассчитывается по выбранному признаку:' + \
                     ' в данном случае использовано количество пересечений разных категорий в разные года  ' + \
                     'и максимальное установленное количество пересечений разных категорий.**')
    st.write('---')
    with st.container():
        st.subheader('***Пространственная структура пропускных пунктов на участках***', divider='blue')
        method = st.selectbox(
            '**:gray[Выберите тип распределения пропускных пунктов:]**',
            ('Сгруппированное', 'Рассредоточенное',
             'Случайное'))
        if method == 'Сгруппированное':
            st.write('**У :blue[112] пропускны пунктов :blue[сгрупированная] пространственная структура**')
        elif method == 'Рассредоточенное':
            st.write('**У :blue[39] пропускны пунктов :blue[рассредоточенная] пространственная структура**')
        elif method == 'Случайное':
            st.write('**У :blue[35] пропускны пунктов :blue[случайная] пространственная структура**')

        st.pydeck_chart(pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=55.7522,
                longitude=100.6156,
                zoom=1.5,
                pitch=50,
            ),

            layers=[pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Китайская Народная Республика')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[72, 118, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[72, 118, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Республика Казахстан')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[131, 111, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[131, 111, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Монголия')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[240, 255, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[240, 255, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Финляндская Республика')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[0, 0, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[0, 0, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Украина')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[0, 245, 255],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[0, 245, 255],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Литовская Республика')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[127, 255, 212],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[127, 255, 212],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Республика Польша')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[164, 211, 238],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[164, 211, 238],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Эстонская Республика')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[188, 238, 104],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[188, 238, 104],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Латвийская Республика')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[238, 180, 180],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[238, 180, 180],
                              opacity=0.8
                              ),
                    pdk.Layer('ColumnLayer',
                              data=ANN[(ANN['Распределение'] == method) &
                                       (ANN['Сопредельное_государство'] == 'Азербайджанская Республика')],
                              get_position='[longitude,latitude]',
                              radius_scale=9000,
                              radius=10000,
                              elevation=100000,
                              elevation_scale=225,
                              get_color=[238, 174, 238],
                              pickable=True,
                              stroked=True,
                              filled=True,
                              get_fill_color=[238, 174, 238],
                              opacity=0.8
                              ),
                    ],

            tooltip={
                "html": '<b>{Вид}</b> <b>{Наименование_пункта_пропуска}</b>, <b>{Сопредельное_государство}</b>',
                "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial',
                          "z-index": "10000"},
            }
        ))
        st.write('**:grey[Описание]	:thinking_face:**')
        st.write('Каждая колонка на карте – пропускной пункт с выбранным типом распределения. ' + \
                 'Размер колонок одинаковый.' + \
                 'Пропускные пункты, относящиеся к одному участку обозначены одним цветом.')
        show = st.checkbox('**:blue[Посмотреть рассматриваемые участки]**')
        if show:
            col1, col2, col3 = st.columns([1.5, 1, 1])
            with col1:
                st.write('**:grey[Азербайджанская Республика]**')
                st.write('**:grey[Китайская Народная Республика]**')
                st.write('**:grey[Латвийская Республика]**')
                st.write('**:grey[Литовская Республика]**')
            with col2:
                st.write('**:grey[Монголия]**')
                st.write('**:grey[Республика Казахстан]**')
                st.write('**:grey[Республика Польша]**')
            with col3:
                st.write('**:grey[Украина]**')
                st.write('**:grey[Финляндская Республика]**')
                st.write('**:grey[Эстонская Республика]**')

    with st.container():
        col1, col2 = st.columns([2, 1])
        with col2:
            st.write('---')
            st.button("Перейти на следующую страницу", key='switch_button')

if selected == 'Статистика по Федеральным округам':

    with st.container():
        value = st.selectbox(
            '***:gray[Выберите график]***',
            ('Распределение пропускных пунктов',
             'Функционирование пропускных пунктов',
             'Пропускные пункты с нулевым фактическим количеством пересечений',
             'Сумма пересечений пропускных пунктов',
             'Усредненное количество пересечений пропускных пунктов',
             'Перегруженные пункты пропуска',
             'Процент наличия контроля определенного типа на пропускных пунктах',
             'Классификация пропускных пунктов по статусу',

             ))

        if value == 'Распределение пропускных пунктов':
            st.write('')
            st.subheader('Распределение пропускных пунктов:airplane:', divider='blue')
            fig = go.Figure(data=go.Heatmap(x=rosgran_count['Вид'],
                                            y=rosgran_count['Федеральный округ'],
                                            z=rosgran_count['Количество ПП'],
                                            colorscale="icefire",
                                            text=rosgran_count['Количество ПП'],
                                            colorbar=dict(title='<b>Количество пропускных пунктов</b>')))
            fig.update_xaxes(title_text="<b>Вид пропускного пункта</b>")
            fig.update_yaxes(title_text='<b>Федеральный округ</b>')

            hover_template = '<b>Федеральный округ</b>: %{y}<br>' + \
                             '<b>Вид пропускного пункта</b>: %{x}<br>' + \
                             '<b>Количество пропускных пунктов</b>: %{z}<extra></extra>'

            fig.update_traces(hovertemplate=hover_template, hoverongaps=False)
            fig.update_layout(height=600, width=1000, margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")


        elif value == 'Функционирование пропускных пунктов':
            st.write('')
            st.subheader('Функционирование пропускных пунктов:heavy_check_mark:', divider='blue')
            option = st.radio(
                "**:blue[Выберите статус работы пропускных пунктов]**",
                ['Функционируют:heavy_check_mark:', 'Не функционируют:x:'])
            if option == 'Функционируют:heavy_check_mark:':
                answer = 'да'
            elif option == 'Не функционируют:x:':
                answer = 'нет'
            fig = px.histogram(rosgran[rosgran['Функционирует/не функционирует'] == answer],
                               y='Федеральный округ',
                               color='Вид',
                               labels=dict(Вид='<b>Вид пропускного пункта</b>'), height=600)
            fig.update_xaxes(title_text='<b>Количество пропускных пунктов</b>')
            fig.update_yaxes(title_text='<b>Федеральный округ</b>')
            hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                             '<b>Федеральный округ</b>: %{y}<br>'
            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")

        elif value == 'Пропускные пункты с нулевым фактическим количеством пересечений':
            st.write('')
            st.subheader('Пропускные пункты с нулевым фактическим количеством пересечений:name_badge:')
            year = st.select_slider(
                "**:blue[Выберите год]**",
                [2017, 2018, 2019, 2020, 2021, 2022])
            option = st.radio(
                "**:blue[Выберите статус работы пропускных пунктов]**",
                ['Функционируют:heavy_check_mark:', 'Не функционируют:x:'])
            if option == 'Функционируют:heavy_check_mark:':
                answer = 'да'
            elif option == 'Не функционируют:x:':
                answer = 'нет'
            fig = px.histogram(
                people_zero[(people_zero['Год'] == year) & (people_zero['Функционирует/не функционирует'] == answer)],
                y="Федеральный округ",
                color='Вид',
                labels=dict(Вид='<b>Вид пропускного пункта</b>'),
                height=600, width=700)
            fig.update_yaxes(title_text='<b>Федеральный округ</b>')
            fig.update_xaxes(title_text='<b>Количество пропускных пунктов</b>')
            hover_template = '<b>Количество пропускных пунктов</b>: %{y}<br>' + \
                             '<b>Федеральный округ</b>: %{x}<br>'
            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")


        elif value == 'Сумма пересечений пропускных пунктов':
            st.write('')
            st.subheader('Сумма пересечений пропускных пунктов:bar_chart:', divider='blue')
            option = st.radio('**:blue[Выберите категорию:]**',
                              ('Число людей', 'Легковые транспортные средства',
                               'Грузовые транспортные средства',
                               'Паспорта транспортных средств', 'Грузы в тоннах'))
            fig = px.histogram(all_df_copy[all_df_copy['Категория'] == option], x="Количество", y="Федеральный округ",
                               facet_col='Год', orientation='h',
                               facet_col_wrap=2, color="Вид",
                               labels=dict(Вид='<b>Вид пропускного пункта</b>'), height=850, width=1000)
            fig.update_yaxes(col=1, title_text='<b>Федеральный округ</b>')
            fig.update_yaxes(col=2, title_text=None)
            fig.update_xaxes(row=2, title_text=None)
            fig.update_xaxes(row=1, title_text='<b>Сумма пересечений</b>')
            hover_template = '<b>Сумма пересечений</b>: %{x}<br>' + \
                             '<b>Федеральный округ</b>: %{y}<br>'
            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")

        elif value == 'Усредненное количество пересечений пропускных пунктов':
            st.write('')
            st.subheader('Усредненное количество пересечений пропускных пунктов:chart_with_downwards_trend:',
                         divider='blue')
            option = st.radio('**:blue[Выберите категорию:]**',
                              ('Число людей', 'Легковые транспортные средства',
                               'Грузовые транспортные средства',
                               'Паспорта транспортных средств', 'Грузы в тоннах'))
            fig = px.histogram(all_df_copy[all_df_copy['Категория'] == option],
                               x="Количество", y="Федеральный округ",
                               facet_col='Год', orientation='h', histfunc='avg',
                               facet_col_wrap=2, color="Вид",
                               labels=dict(Вид='<b>Вид пропускного пункта</b>', value=''), height=850, width=1000)
            fig.update_yaxes(col=1, title_text='<b>Федеральный округ</b>')
            fig.update_yaxes(col=2, title_text=None)
            fig.update_xaxes(row=3, title_text=None)
            fig.update_xaxes(row=2, title_text=None)
            fig.update_xaxes(row=1, title_text='<b>Усредненное количество пересечений</b>')
            hover_template = '<b>Усредненное количество пересечений</b>: %{x}<br>' + \
                             '<b>Федеральный округ</b>: %{y}<br>'
            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")

        elif value == 'Перегруженные пункты пропуска':
            st.write('')
            st.subheader('Перегруженные пункты пропуска:bomb:', divider='blue')
            option = st.radio('**:blue[Выберите категорию:]**',
                              ('Число людей', 'Легковые транспортные средства',
                               'Грузовые транспортные средства',
                               'Паспорта транспортных средств',
                               'Грузы в тоннах'))
            fig = px.bar(all_df_copy_na[all_df_copy_na['Категория'] == option],
                         x="Количество (Факт/Паспорт)", y="Федеральный округ",
                         facet_col='Год',
                         hover_name='Наименование пункта пропуска',
                         facet_col_wrap=2, color="Вид",
                         labels=dict(Вид='<b>Вид пропускного пункта</b>', value=''), height=850, width=1000)
            fig.update_yaxes(col=1, title_text='<b>Федеральный округ</b>')
            fig.update_yaxes(col=2, title_text=None)
            fig.update_xaxes(row=3, title_text=None)
            fig.update_xaxes(row=2, title_text=None)
            fig.update_xaxes(row=1, title_text='<b>Отношение фактического потока к паспортному</b>')
            hover_template = '<b>Наименование пункта пропуска</b>: %{hovertext}<br>' + \
                             '<b>Отношение фактического потока к паспортному</b>: %{x}<br>' + \
                             '<b>Федеральный округ</b>: %{y}'

            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")
            st.write()
            question = st.checkbox('**:red[Какой пункт считается перегруженным]:grey_question:**')
            if question:
                st.write('**У каждого пункта пропуска есть максимальная установленная пропускная способность,' + \
                         'но есть пропускные пункты, фактическое количество пересечений которых превышает максимально возморжное.' + \
                         'Пропускной пункт считается перегруженным,' + \
                         'если результат деления фактического количества пересечений на максимально возможно превышает единицу.**')

        elif value == 'Процент наличия контроля определенного типа на пропускных пунктах':
            st.write('')
            st.subheader('Процент наличия контроля определенного типа на пропускных пунктах:passport_control:',
                         divider='blue')
            option = st.radio('**:blue[Выберите тип контроля]**',
                              ('Таможенный', 'Пограничный',
                               'Транспортный', 'Санитарно-карантинный',
                               'Карантинный фитосанитарный', 'Ветеринарный'))
            fig = go.Figure(
                data=go.Heatmap(z=controls_else[controls_else['Тип контроля'] == option]['Процент контроля'],
                                x=controls_else[controls_else['Тип контроля'] == option]['Вид'],
                                y=controls_else[controls_else['Тип контроля'] == option]['Федеральный округ'],
                                colorscale='RdBu',
                                colorbar=dict(title='<b>Процент контроля</b>'),
                                text=controls_else[controls_else['Тип контроля'] == option]['Процент контроля'],
                                customdata=controls_else[controls_else['Тип контроля'] == option][['Федеральный округ',
                                                                                                   'Вид',
                                                                                                   'Процент контроля']])
                )

            fig.update_xaxes(title_text="<b>Вид пропускного пункта</b>")
            fig.update_yaxes(title_text='<b>Федеральный округ</b>')

            hover_template = '<b>Федеральный округ</b>: %{customdata[0]}<br>' + \
                             '<b>Вид пропускного пункта</b>: %{customdata[1]}<br>' + \
                             '<b>Процент контроля</b>: %{customdata[2]}%<extra></extra>'

            fig.update_traces(hovertemplate=hover_template, hoverongaps=False)
            fig.update_layout(
                width=800,  # Ширина графика
                height=600,  # Высота графика
                margin=dict(l=50, r=50, t=20, b=50),  # Отступы слева, справа, сверху и снизу
            )

            st.plotly_chart(fig, theme="streamlit")


        elif value == 'Классификация пропускных пунктов по статусу':
            st.write('')
            st.subheader('Классификация пропускных пунктов по статусу:label:', divider='blue')
            option = st.radio(
                "**:blue[Выберите статус работы пропускных пунктов]**",
                ['Многосторонний:heavy_check_mark:', 'Двусторонний:two:'])
            if option == 'Многосторонний:heavy_check_mark:':
                answer = 'многосторонний'
            elif option == 'Двусторонний:two:':
                answer = 'двусторонний'
            fig = px.histogram(rosgran[rosgran['Классификация по статусу'] == answer], y="Федеральный округ",
                               color='Вид', height=600, width=900)
            fig.update_layout(legend=dict(title="<b>Вид пропускного пункта</b>"))
            fig.update_yaxes(title_text='<b>Федеральный округ</b>')
            fig.update_xaxes(title_text='<b>Количество пропускных пунктов</b>')
            hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                             '<b>Федеральный округ</b>: %{y}<br>'

            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")

if selected == 'Статистика по участкам':

    with (((st.container()))):
        value = st.selectbox(
            '***:gray[Выберите график]***',
            ('Распределение пропускных пунктов',
             'Функционирование пропускных пунктов',
             'Пропускные пункты с нулевым фактическим количеством пересечений',
             'Сумма пересечений пропускных пунктов',
             'Усредненное количество пересечений пропускных пунктов',
             'Перегруженные пункты пропуска',
             'Процент наличия контроля определенного типа на пропускных пунктах',
             'Классификация пропускных пунктов по статусу',

             ))
        if value == 'Распределение пропускных пунктов':
            st.write('')
            st.subheader('Распределение пропускных пунктов:truck:', divider='blue')
            fig = go.Figure(data=go.Heatmap(x=places_count['Вид'],
                                            y=places_count['Сопредельное государство'],
                                            z=places_count['Количество ПП'],
                                            colorscale='RdGy',
                                            text=places_count['Количество ПП'],
                                            colorbar=dict(title='<b>Количество пропускных пунктов</b>')))

            fig.update_xaxes(title_text="<b>Вид пропускного пункта</b>")
            fig.update_yaxes(title_text='<b>Сопредельное государство</b>')

            hover_template = '<b>Сопредельное государство</b>: %{y}<br>' + \
                             '<b>Вид пропускного пункта</b>: %{x}<br>' + \
                             '<b>Количество пропускных пунктов</b>: %{z}<extra></extra>'

            fig.update_traces(hovertemplate=hover_template, hoverongaps=False)
            fig.update_layout(
                width=1000,  # Ширина графика
                height=600,  # Высота графика
                margin=dict(t=20),  # Отступы слева, справа, сверху и снизу
            )

            st.plotly_chart(fig, theme="streamlit")

        elif value == 'Функционирование пропускных пунктов':
            st.write('')
            st.subheader('Функционирование пропускных пунктов:heavy_check_mark:', divider='blue')
            option = st.radio(
                "**:blue[Выберите статус работы пропускных пунктов]**",
                ['Функционируют:heavy_check_mark:', 'Не функционируют:x:'])
            if option == 'Функционируют:heavy_check_mark:':
                answer = 'да'
            elif option == 'Не функционируют:x:':
                answer = 'нет'

            fig = px.histogram(places_copy[(places_copy['Категория'] == 'Число людей') &
                                           (places_copy['Год'] == 2022) &
                                           (places_copy['Функционирует/не функционирует'] == answer)],
                               y='Сопредельное государство', color='Вид',
                               labels=dict(Вид='<b>Вид пропускного пункта</b>'), height=600, width=900)
            fig.update_xaxes(title_text='<b>Количество пропускных пунктов</b>')
            fig.update_yaxes(title_text='<b>Сопредельное государство</b>')
            hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                             '<b>Сопредельное государство</b>: %{y}<br>'
            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")

        elif value == 'Пропускные пункты с нулевым фактическим количеством пересечений':
            st.write('')
            st.subheader('Пропускные пункты с нулевым фактическим количеством пересечений:name_badge:')
            year = st.select_slider(
                "**:blue[Выберите год]**",
                [2017, 2018, 2019, 2020, 2021, 2022])
            option = st.radio(
                "**:blue[Выберите статус работы пропускных пунктов]**",
                ['Функционируют:heavy_check_mark:', 'Не функционируют:x:'])
            if option == 'Функционируют:heavy_check_mark:':
                answer = 'да'
            elif option == 'Не функционируют:x:':
                answer = 'нет'
            fig = px.histogram(places_copy[(places_copy['Категория'] == 'Число людей') &
                                           (places_copy['Количество'] == 0) &
                                           (places_copy['Год'] == year) &
                                           (places_copy['Функционирует/не функционирует'] == answer)],
                               y="Сопредельное государство",
                               color='Вид', labels=dict(Вид='<b>Вид пропускного пункта</b>'),
                               height=500, width=800)
            fig.update_xaxes(title_text='<b>Количество пропускных пунктов</b>')
            fig.update_yaxes(title_text='<b>Сопредельное государство</b>')
            hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                             '<b>Сопредельное государство</b>: %{y}<br>'
            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")


        elif value == 'Сумма пересечений пропускных пунктов':
            st.write('')
            st.subheader('Сумма пересечений пропускных пунктов:bar_chart:', divider='blue')
            option = st.radio('**:blue[Выберите категорию:]**',
                              ('Число людей', 'Легковые транспортные средства',
                               'Грузовые транспортные средства',
                               'Паспорта транспортных средств', 'Грузы в тоннах'))
            fig = px.histogram(all_df_copy_places[all_df_copy_places['Категория'] == option],
                               x="Количество", y="Сопредельное государство",
                               facet_col='Год',
                               orientation='h', facet_col_wrap=2, color="Вид",
                               labels=dict(Вид='<b>Вид пропускного пункта</b>'), height=1450, width=1000)
            fig.update_yaxes(col=1, title_text='<b>Сопредельное государство</b>')
            fig.update_yaxes(col=2, title_text=None)
            fig.update_xaxes(row=3, title_text=None)
            fig.update_xaxes(row=2, title_text=None)
            fig.update_xaxes(row=1, title_text='<b>Сумма пересечений</b>')
            hover_template = '<b>Сумма пересечений</b>: %{x}<br>' + \
                             '<b>Сопредельное государство</b>: %{y}<br>'
            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")


        elif value == 'Усредненное количество пересечений пропускных пунктов':
            st.write('')
            st.subheader('Усредненное количество пересечений пропускных пунктов:chart_with_downwards_trend:',
                         divider='blue')
            option = st.radio('**:blue[Выберите категорию:]**',
                              ('Число людей', 'Легковые транспортные средства',
                               'Грузовые транспортные средства',
                               'Паспорта транспортных средств', 'Грузы в тоннах'))
            fig = px.histogram(all_df_copy_places[all_df_copy_places['Категория'] == option], x="Количество",
                               y="Сопредельное государство",
                               facet_col='Год', facet_col_wrap=2,
                               orientation='h', histfunc='avg', color="Вид",
                               labels=dict(Вид='<b>Вид пропускного пункта</b>', value=''), height=1450, width=1000)
            fig.update_yaxes(col=1, title_text='<b>Сопредельное государство</b>')
            fig.update_yaxes(col=2, title_text=None)
            fig.update_xaxes(row=3, title_text=None)
            fig.update_xaxes(row=2, title_text=None)
            fig.update_xaxes(row=1, title_tex='<b>Усредненное количество пересечений</b>')
            hover_template = '<b>Усредненное количество пересечений</b>: %{x}<br>' + \
                             '<b>Сопредельное государство</b>: %{y}<br>'
            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")


        elif value == 'Перегруженные пункты пропуска':
            st.write('')
            st.subheader('Перегруженные пункты пропуска:warning:', divider='blue')
            option = st.radio('**:blue[Выберите категорию:]**',
                              ('Число людей', 'Легковые транспортные средства',
                               'Грузовые транспортные средства',
                               'Паспорта транспортных средств',
                               'Грузы в тоннах'))
            fig = px.bar(push[push['Категория'] == option],
                         x="Количество (Факт/Паспорт)", y="Сопредельное государство",
                         facet_col='Год',
                         hover_name='Наименование пункта пропуска',
                         facet_col_wrap=1, color="Вид",
                         labels=dict(Вид='<b>Вид пропускного пункта</b>', value=''), height=1450, width=1000)
            fig.update_yaxes(col=1, title_text='<b>Сопредельное государство</b>')
            fig.update_yaxes(col=2, title_text=None)
            fig.update_xaxes(row=3, title_text=None)
            fig.update_xaxes(row=2, title_text=None)
            fig.update_xaxes(row=1, title_text='<b>Отношение фактического потока к паспортному</b>')
            hover_template = '<b>Наименование пункта пропуска</b>: %{hovertext}<br>' + \
                             '<b>Отношение фактического потока к паспортному</b>: %{x}<br>' + \
                             '<b>Сопредельное государство</b>: %{y}'

            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")
            st.write()
            question = st.checkbox('**:red[Какой пункт считается перегруженным]:grey_question:**')
            if question:
                st.write('**У каждого пункта пропуска есть максимальная установленная пропускная способность,' + \
                         'но есть пропускные пункты, фактическое количество пересечений которых превышает максимально возморжное.' + \
                         'Пропускной пункт считается перегруженным,' + \
                         'если результат деления фактического количества пересечений на максимально возможно превышает единицу.**')

        elif value == 'Процент наличия контроля определенного типа на пропускных пунктах':
            st.write('')
            st.subheader('Процент наличия контроля определенного типа на пропускных пунктах:passport_control:',
                         divider='blue')
            option = st.radio('**:blue[Выберите тип контроля]**',
                              ('Таможенный', 'Пограничный',
                               'Транспортный', 'Санитарно-карантинный',
                               'Карантинный фитосанитарный', 'Ветеринарный'))
            fig = go.Figure(data=go.Heatmap(z=country_else[country_else['Тип контроля'] == option]['Процент контроля'],
                                            x=country_else[country_else['Тип контроля'] == option]['Вид'],
                                            y=country_else[country_else['Тип контроля'] == option][
                                                'Сопредельное государство'],
                                            colorscale='RdBu',
                                            colorbar=dict(title='<b>Процент контроля</b>'),
                                            text=country_else[country_else['Тип контроля'] == option][
                                                'Процент контроля'],
                                            customdata=country_else[country_else['Тип контроля'] == option][
                                                ['Сопредельное государство',
                                                 'Вид', 'Процент контроля']])
                            )

            fig.update_xaxes(title_text="<b>Вид пропускного пункта</b>")
            fig.update_yaxes(title_text='<b>Сопредельное государство</b>')

            hover_template = '<b>Сопредельное государство</b>: %{customdata[0]}<br>' + \
                             '<b>Вид пропускного пункта</b>: %{customdata[1]}<br>' + \
                             '<b>Процент контроля</b>: %{customdata[2]}%<extra></extra>'

            fig.update_traces(hovertemplate=hover_template, hoverongaps=False)
            fig.update_layout(
                width=1000,  # Ширина графика
                height=700,  # Высота графика
                margin=dict(l=50, r=50, t=20, b=50),  # Отступы слева, справа, сверху и снизу
            )

            st.plotly_chart(fig, theme="streamlit")


        elif value == 'Классификация пропускных пунктов по статусу':
            st.write('')
            st.subheader('Классификация пропускных пунктов по статусу:label:', divider='blue')
            option = st.radio(
                "**:blue[Выберите статус работы пропускных пунктов]**",
                ['Многосторонний:heavy_check_mark:', 'Двусторонний:two:'])
            if option == 'Многосторонний:heavy_check_mark:':
                answer = 'многосторонний'
            elif option == 'Двусторонний:two:':
                answer = 'двусторонний'
            places = rosgran[(rosgran['Сопредельное государство'] != 'не применимо') &
                             (rosgran['Сопредельное государство'] != 'не применимо (ДНР)') &
                             (rosgran['Сопредельное государство'] != 'не применимо (ЛНР)') &
                             (rosgran['Сопредельное государство'] != 'не применимо (Херсонская обл.)')]
            fig = px.histogram(places[places['Классификация по статусу'] == answer], y="Сопредельное государство",
                               color='Вид', height=800, width=1000)
            fig.update_layout(legend=dict(title="<b>Вид пропускного пункта</b>"))
            fig.update_xaxes(title_text='<b>Количество пропускных пунктов</b>')
            fig.update_yaxes(title_text='<b>Сопредельное государство</b>')
            hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                             '<b>Сопредельное государство</b>: %{y}<br>'

            fig.update_traces(hovertemplate=hover_template)
            fig.update_xaxes(showspikes=True, spikemode='across')
            fig.update_layout(margin=dict(t=20))
            st.plotly_chart(fig, theme="streamlit")
