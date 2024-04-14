import axios from 'axios';
import {useEffect, useState} from 'react';
import {IMessageEvent, w3cwebsocket as W3CWebSocket} from 'websocket';
import AddSong from '../components/AddSongForm';
import EditSong from '../components/EditSongForm';
import {ISong} from '../components/MySong.type';
import {PageEnum} from '../components/PageEnum';
import SongList from '../components/SongList';
import Diagram from './Diagram';
import ErrorPage from './ErrorPage';
import './Home.style.css';
import SortFilter from './SortFilter';

const Home = () => {
    const [MySongList, SetSongList] = useState([] as ISong[]);
    const [ShownPage, SetShownPage] = useState(PageEnum.list);
    const [DataToEdit, SetDataToEdit] = useState({} as ISong);
    const [errorMessage, setErrorMessage] = useState('');
    const [connectionErrorMessage, setConnectionErrorMessage] = useState('');
    const [isOnline, setIsOnline] = useState(navigator.onLine);
    const client = new W3CWebSocket('ws://localhost:4000/');

    useEffect(() => {
        const handleOnlineStatus = () => {
            setIsOnline(navigator.onLine);
        };

        window.addEventListener('online', handleOnlineStatus);
        window.addEventListener('offline', handleOnlineStatus);

        return () => {
            window.removeEventListener('online', handleOnlineStatus);
            window.removeEventListener('offline', handleOnlineStatus);
        };
    }, []);

    useEffect(() => {
        if (!isOnline) {
            SetShownPage(PageEnum.error);
            setConnectionErrorMessage(
                'Internet is down. Please try again later.',
            );
            return;
        }

        axios
            .get('http://localhost:3000/crud-operations/songs')
            .then((response) => {
                SetSongList(response.data);
                console.log(response.data);
            })
            .catch((error) => {
                setConnectionErrorMessage(
                    'Server error. Please try again later.',
                );
                SetShownPage(PageEnum.error);
                console.error('Error fetching songs:', error);
            });
    }, [isOnline]);

    // const _setSongList = (list: ISong[]) => {
    //     SetSongList(list);
    //     window.localStorage.setItem('Song List', JSON.stringify(list));
    // };
    useEffect(() => {
        // Handle incoming messages from WebSocket server
        client.onmessage = (message: IMessageEvent) => {
            // Ensure the data is treated as a string
            const dataString =
                typeof message.data === 'string'
                    ? message.data
                    : new TextDecoder().decode(message.data);
            const updatedSongs = JSON.parse(dataString);
            SetSongList(updatedSongs);
        };
    }, []);

    const onAddSongClickHandle = () => {
        SetShownPage(PageEnum.add);
    };

    const onDiagramClickHandler = () => {
        SetShownPage(PageEnum.diagram);
    };

    const onSearchClickHandler = () => {
        SetShownPage(PageEnum.sort_filter);
    };

    const showListPage = () => {
        SetShownPage(PageEnum.list);
    };

    const onSubmitAddSong = (data: ISong) => {
        SetSongList([...MySongList, data]);
    };

    const onClickDeleteSong = (data: ISong) => {
        const indexToDelete = MySongList.indexOf(data);
        if (indexToDelete) {
            const temporarySongList = [...MySongList];
            temporarySongList.splice(indexToDelete, 1);
            SetSongList(temporarySongList);

            axios
                .delete(`http://localhost:3000/crud-operations/${data.id}`)
                .then((response) => {
                    console.log('Song deleted successfully:', response.data);
                })
                .catch((error) => {
                    console.error(
                        'There was an error deleting the song:',
                        error.toString(),
                    );
                });
        } else {
            console.log('error in deleting');
        }
    };

    const onClickEditSong = (data: ISong) => {
        SetShownPage(PageEnum.edit);
        SetDataToEdit(data);
    };

    const UpdateSong = (data: ISong) => {
        try {
            const filteredData = MySongList.filter((x) => x.id === data.id)[0];
            const indexToUpdate = MySongList.indexOf(filteredData);
            const temporaryData = [...MySongList];
            temporaryData[indexToUpdate] = data;
            SetSongList(temporaryData);

            axios
                .put(`http://localhost:3000/crud-operations/${data.id}`, data)
                .then((response) => {
                    console.log('Song updated successfully:', response.data);
                })
                .catch((error) => {
                    if (error.response && error.response.status === 404) {
                        setErrorMessage(error.response.data);
                    } else {
                        console.error(
                            'There was an error updating the song:',
                            error.toString(),
                        );
                    }
                });
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className='container'>
            <header className='header-title'>
                <h2 className='title'>Your Personal Music Journal</h2>
            </header>
            <aside className='sidebar'>
                <button onClick={onDiagramClickHandler}>Diagram</button>
                <button onClick={onSearchClickHandler}>
                    Search and Filter
                </button>
                <button
                    onClick={() => console.log('Navigate to About Us page')}
                >
                    About Us
                </button>
            </aside>
            <section className='content'>
                {ShownPage == PageEnum.list && (
                    <div className='container'>
                        <input
                            className='add-form'
                            type='button'
                            value={'Add New Song'}
                            onClick={onAddSongClickHandle}
                        />
                        <div className='song-list-container'>
                            <div className='song-list-wrapper'>
                                <SongList
                                    list={MySongList}
                                    onDeleteClickHandler={onClickDeleteSong}
                                    onEditClickHandler={onClickEditSong}
                                />
                            </div>
                        </div>
                    </div>
                )}
                {ShownPage == PageEnum.add && (
                    <AddSong
                        onBackButtonClick={showListPage}
                        onSubmitHandler={onSubmitAddSong}
                    />
                )}
                {ShownPage == PageEnum.edit && (
                    <EditSong
                        data={DataToEdit}
                        onBackButtonClick={showListPage}
                        onUpdateClickHandler={UpdateSong}
                    />
                )}
                {ShownPage == PageEnum.diagram && (
                    <Diagram
                        list={MySongList}
                        onBackButtonClick={showListPage}
                    />
                )}
                {ShownPage == PageEnum.sort_filter && (
                    <SortFilter
                        list={MySongList}
                        onBackButtonClick={showListPage}
                    />
                )}
                {ShownPage == PageEnum.error && (
                    <ErrorPage
                        new_error={connectionErrorMessage}
                        onBackButtonClick={showListPage}
                    />
                )}
                {errorMessage && (
                    <div className='popup' style={{color: 'red'}}>
                        <p>{errorMessage}</p>
                        <button onClick={() => setErrorMessage('')}>
                            Close
                        </button>
                    </div>
                )}
            </section>
        </div>
    );
};

export default Home;
