import {ISong} from './MySong.type';
import './SongDetailsModal.style.css';

type DetailsModalProps = {
    onClose: () => void;
    data: ISong;
};

const SongModal = (props: DetailsModalProps) => {
    const {onClose, data} = props;
    return (
        <div id='myModal' className='modal'>
            <div className='modal-content'>
                <span className='close' onClick={onClose}>
                    &times;
                </span>
                <div>
                    <div>
                        <h3 className='h-style'>
                            <label className='label-style'>{data.title}</label>
                            <label className='label-style'> by </label>
                            <label className='label-style'>{data.artist}</label>
                        </h3>
                    </div>
                    <div>
                        <h4 className='h-style'>
                            Your thoughts on this song:{' '}
                        </h4>
                        <label className='label-style'>
                            Rating: {data.rating}{' '}
                        </label>
                    </div>
                    <div>
                        <label className='label-style'>
                            Review: {data.review}
                        </label>
                    </div>
                </div>
            </div>
        </div>
    );
};
export default SongModal;
