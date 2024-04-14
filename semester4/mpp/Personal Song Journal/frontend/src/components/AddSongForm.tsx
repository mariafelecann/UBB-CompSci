import axios from 'axios';
import {useState} from 'react';
import './AddSongForm.style.css';
import {ISong} from './MySong.type';

type AddSongProps = {
    onBackButtonClick: () => void;
    onSubmitHandler: (data: ISong) => void;
};
const AddSong = (props: AddSongProps) => {
    const {onBackButtonClick, onSubmitHandler} = props;
    const [title, SetTitle] = useState('');
    const [artist, SetArtist] = useState('');
    const [rating, SetRating] = useState('');
    const [review, SetReview] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const titleChangeHandler = (e: any) => {
        SetTitle(e.target.value);
    };

    const artistChangeHandler = (e: any) => {
        SetArtist(e.target.value);
    };
    const ratingChangeHandler = (e: any) => {
        SetRating(e.target.value);
    };
    const reviewChangeHandler = (e: any) => {
        SetReview(e.target.value);
    };
    const onSubmitClickHandler = (e: any) => {
        e.preventDefault();
        const titleError = validateTitle(title);
        const artistError = validateArtist(artist);
        const ratingError = validateRating(rating);
        const reviewError = validateReview(review);

        if (titleError || artistError || ratingError || reviewError) {
            onBackButtonClick();
        } else {
            const data: ISong = {
                id: new Date().toJSON().toString(),
                title: title,
                artist: artist,
                rating: parseInt(rating),
                review: review,
            };

            //onSubmitHandler(data);
            // onBackButtonClick();

            axios
                .post(`http://localhost:3000/crud-operations/${data.id}`, data)
                .then((response) => {
                    console.log('Song added successfully:', response.data);
                    onSubmitHandler(data);
                    onBackButtonClick();
                })
                .catch((error) => {
                    if (
                        error.response &&
                        error.response.status === 404 &&
                        error.response.data === 'Song already exists'
                    ) {
                        setErrorMessage('Song already exists');
                    } else {
                        console.error(
                            'There was an error adding the song:',
                            error.toString(),
                        );
                    }
                });
        }
    };

    const validateTitle = (title: string): string | null => {
        if (!title || typeof title !== 'string') {
            return 'title should be a string';
        }
        return null;
    };

    const validateArtist = (artist: string): string | null => {
        if (!artist || typeof artist !== 'string') {
            return 'artist should be a string';
        }
        return null;
    };

    const validateRating = (rating: string): string | null => {
        const parsedRating = parseInt(rating);
        if (isNaN(parsedRating)) {
            return 'rating should be a number';
        }
        return null;
    };

    const validateReview = (review: string): string | null => {
        if (!review || typeof review !== 'string') {
            return 'review should be a string';
        }
        return null;
    };
    return (
        <form
            className='add-song-form-container'
            onSubmit={onSubmitClickHandler}
        >
            <header>
                <h3>Add a new Song!</h3>
            </header>
            <div className='elements-container'>
                <div>
                    <label>Title:</label>
                    <input
                        className='input-box'
                        type='text'
                        value={title}
                        onChange={titleChangeHandler}
                    />
                </div>
                <div>
                    <label>Artist:</label>
                    <input
                        className='input-box'
                        type='text'
                        value={artist}
                        onChange={artistChangeHandler}
                    />
                </div>
                <div>
                    <label>Rating:</label>
                    <input
                        className='input-box'
                        type='text'
                        value={rating}
                        onChange={ratingChangeHandler}
                    />
                </div>
                <div>
                    <label>Review:</label>
                    <input
                        className='input-box'
                        type='text'
                        value={review}
                        onChange={reviewChangeHandler}
                    />
                </div>
            </div>
            <div className='buttons-container'>
                <button onClick={onBackButtonClick}>Back</button>
                <button type='submit'>Add Song</button>
            </div>
            {errorMessage && (
                <div className='popup'>
                    <p>{errorMessage}</p>
                    <button
                        onClick={() => {
                            setErrorMessage('');
                            onBackButtonClick;
                        }}
                    >
                        Close
                    </button>
                </div>
            )}
        </form>
    );
};

export default AddSong;
