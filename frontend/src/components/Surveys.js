import { Questions } from './Questions';

import PropTypes from 'prop-types';
import React from 'react';

export const Surveys = (props) => {
  const { data, register } = props;

  const list = data.map((item, index) => {
    return (
      <div key={`survey-${index}`}>
        <h2>{item.name}</h2>
        <Questions data={item.questions} register={register} />
      </div>
    );
  });

  return list;
};

Surveys.defaultProps = {
  data: [],
  register: () => {},
};

Surveys.propTypes = {
  data: PropTypes.array,
  register: PropTypes.func,
};
