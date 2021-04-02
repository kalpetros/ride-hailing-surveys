import { Input } from './Input';
import { MultiInput } from './MultiInput';

import { useForm } from 'react-hook-form';
import PropTypes from 'prop-types';
import React from 'react';

export const Questions = (props) => {
  const { data, register } = props;

  const list = data.map((question, qIndex) => {
    if (question.survey_type === 'RA') {
      const choices = question.choices.map((choice, index) => {
        return (
          <MultiInput
            key={`question_${question.id}-choice-${choice.id}`}
            id={`question_${question.id}`}
            name={`question_${question.id}`}
            type="radio"
            value={choice.text}
            label={choice.text}
            reference={register}
          />
        );
      });

      return (
        <div key={`question-${question.id}`} className="Question">
          <label className="label">{question.title}</label>
          {choices}
        </div>
      );
    }

    if (question.survey_type === 'MU') {
      const choices = question.choices.map((choice, index) => {
        return (
          <MultiInput
            key={`question-${question.id}-choice-${choice.id}`}
            id={`question_${question.id}_choice_${choice.id}`}
            name={`question_${question.id}_choice_${choice.id}`}
            type="checkbox"
            label={choice.text}
            reference={register}
          />
        );
      });

      return (
        <div key={`question-${question.id}`} className="Question">
          <label className="label">{question.title}</label>
          {choices}
        </div>
      );
    }

    return (
      <div key={`question-${question.id}`} className="Question">
        <Input
          id={`question_${question.id}`}
          name={`question_${question.id}`}
          label={question.title}
          reference={register}
        />
      </div>
    );
  });

  return list;
};

Questions.defaultProps = {
  data: [],
  register: () => {},
};

Questions.propTypes = {
  data: PropTypes.array,
  register: PropTypes.func,
};
