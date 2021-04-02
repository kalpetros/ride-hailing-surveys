import './styles/index.scss';

import { Button } from './components/Button';
import { Rating } from './components/Rating';
import { Surveys } from './components/Surveys';

import getFormData from './utils';
import registerIcons from './registerIcons';

import { useForm } from 'react-hook-form';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';

registerIcons();

const App = () => {
  const { handleSubmit, register } = useForm();
  const [data, setData] = useState([]);
  const [rating, setRating] = useState(4);
  const [status, setStatus] = useState('pending');
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Initiate a get request passing a test user
    axios
      .get('http://localhost:8000/api/v1/surveys/', {
        params: { user: 'test@test.com' },
      })
      .then((response) => {
        if (response.data.errors) return;
        setData(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const submit = (data) => {
    // Initiate a post request passing a test user
    let postData = {
      user: 'test@test.com',
      rating: rating,
      survey: getFormData(data),
    };

    axios
      .post('http://localhost:8000/api/v1/feedback/', postData)
      .then((response) => {
        if (response.data.errors) return;
        setData([]);
        setStatus('done');
        setMessage(response.data.msg);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="container">
      {status === 'pending' ? (
        <div className="Survey">
          <form onSubmit={handleSubmit(submit)}>
            <h1>Rate your ride</h1>
            <Rating selection={rating} onSelect={setRating} />
            {data.length ? (
              <>
                <h1>Help us improve by answering the following...</h1>
                <Surveys data={data} register={register} />
              </>
            ) : null}
            <div>
              <Button text="Submit" />
            </div>
          </form>
        </div>
      ) : (
        <h1>{message}</h1>
      )}
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
