import PropTypes from 'prop-types';
import React from 'react';

export const MultiInput = (props) => {
  const {
    reference,
    id,
    name,
    type,
    label,
    placeholder,
    value,
  } = props;

  return (
    <div className="MultiInput">
      <div className="MultiInput__element">
        <input
          ref={reference}
          id={id}
          name={name}
          type={type}
          placeholder={placeholder}
          value={value}
        />
        <label htmlFor={id} className="MultiInput__label">
          {label}
        </label>
      </div>
    </div>
  );
};

MultiInput.defaultProps = {
  reference: {},
  id: '',
  name: '',
  type: 'text',
  label: '',
  placeholder: '',
  value: '',
};

MultiInput.propTypes = {
  reference: PropTypes.func,
  id: PropTypes.string.isRequired,
  name: PropTypes.string,
  type: PropTypes.oneOf(['checkbox', 'radio']),
  label: PropTypes.string,
  placeholder: PropTypes.string,
  value: PropTypes.string,
};
