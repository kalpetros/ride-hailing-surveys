import PropTypes from 'prop-types';
import React from 'react';

export const Button = (props) => {
  const { text, disabled } = props;

  return (
    <button className="button" disabled={disabled}>
      {text}
    </button>
  );
};

Button.defaultProps = {
  text: '',
  disabled: false,
};

Button.propTypes = {
  text: PropTypes.string,
  disabled: PropTypes.bool,
};
