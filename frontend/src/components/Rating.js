import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import PropTypes from 'prop-types';
import React from 'react';

export const Rating = (props) => {
  const { selection, onSelect } = props;

  const items = Array(5)
    .fill(1)
    .map((item, index) => {
      const stars = Array(index + 1)
        .fill(1)
        .map((item, index) => {
          return <FontAwesomeIcon key={`rating-${index}`} icon="star" />;
        });

      return (
        <div
          key={`rating-choice-${index}`}
          className={
            selection === index + 1
              ? 'Survey__rating_item Survey__rating_item--selected'
              : 'Survey__rating_item'
          }
          onClick={() => {
            onSelect(index + 1);
          }}
        >
          {stars}
        </div>
      );
    });

  return <div className="Survey__rating">{items}</div>;
};

Rating.defaultProps = {
  selection: 5,
  onSelect: () => {},
};

Rating.propTypes = {
  selection: PropTypes.number,
  onSelect: PropTypes.func,
};
