import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import PropTypes from 'prop-types';
import React from 'react';

export const Input = (props) => {
  const { id, type, label, placeholder, value, onChange } = props;

  return (
    <div className="input">
      <label htmlFor={id} className="input__label">
        {label}
      </label>
      <div className="input__element">
        <input
          id={id}
          type={type}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
        />
      </div>
    </div>
  );
};

Input.defaultProps = {
  id: '',
  type: 'text',
  label: '',
  placeholder: '',
  value: '',
  onChange: () => {},
};

Input.propTypes = {
  id: PropTypes.string.isRequired,
  type: PropTypes.oneOf(['text', 'number']),
  label: PropTypes.string,
  placeholder: PropTypes.string,
  value: PropTypes.string,
  onChange: PropTypes.func,
};
