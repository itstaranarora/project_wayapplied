import React from 'react';
import Form from './includes/Form';

const Submit = () => {
  const onSubmit = (e) => {
    console.log({ e });
    fetch('http://localhost:5000/api/public/submit/website', {
      method: 'POST',
      body: JSON.stringify(e),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((res) => {
        console.log(res);
      })
      .catch((err) => console.log(err));
  };

  return (
    <section className="submit-form bg-primary">
      <h1>Help us improve our collection</h1>
      <Form onSubmit={onSubmit} />
    </section>
  );
};

export default Submit;
