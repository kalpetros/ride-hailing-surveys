export default function getFormData(data) {
  const surveyData = {};

  Object.keys(data).forEach((item) => {
    const ids = item.split('_');
    const questionId = ids[1];
    const isCheckbox = item.indexOf('choice') >= 0;

    if (isCheckbox) {
      if (surveyData[questionId] === undefined) {
        surveyData[questionId] = [];
      }
      const choiceId = ids[ids.length - 1];

      if (data[item]) {
        surveyData[questionId].push(choiceId);
      }
    } else {
      const answer = data[item] === null ? '' : data[item];
      surveyData[questionId] = answer;
    }
  });

  return surveyData;
}
