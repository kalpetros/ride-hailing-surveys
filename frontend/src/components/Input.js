import PropTypes from 'prop-types';
import React from 'react';

export const Input = (props) => {
  const {
    reference,
    id,
    name,
    type,
    label,
    placeholder,
    defaultValue,
  } = props;

  return (
    <div className="input">
      <label htmlFor={id} className="input__label">
        {label}
      </label>
      <div className="input__element">
        <input
          ref={reference}
          id={id}
          name={name}
          type={type}
          placeholder={placeholder}
          defaultValue={defaultValue}
        />
      </div>
    </div>
  );
};

Input.defaultProps = {
  reference: {},
  id: '',
  name: '',
  type: 'text',
  label: '',
  placeholder: '',
  defaultValue: '',
};

Input.propTypes = {
  reference: PropTypes.func,
  id: PropTypes.string.isRequired,
  name: PropTypes.string,
  type: PropTypes.oneOf(['text', 'number']),
  label: PropTypes.string,
  placeholder: PropTypes.string,
  defaultValue: PropTypes.string,
};
