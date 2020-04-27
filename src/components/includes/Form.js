import React, { useState, useEffect } from 'react';

const Form = (props) => {
  const [Categories, setCategories] = useState([]);
  const [email, setemail] = useState('');
  const [description, setdescription] = useState('');
  const [website, setwebsite] = useState('');
  const [url, seturl] = useState('');
  const [category, setcategory] = useState('');
  const [message, setmessage] = useState('');

  useEffect(() => {
    categoriesNames();
  }, []);

  const categoriesNames = async () => {
    const data = await fetch(
      'http://localhost:5000/api/public/websites/categories'
    );
    const names = await data.json();
    const name = names[0].name;
    setcategory(name);
    setCategories(names);
  };

  const handleEmailChange = (e) => {
    setemail(e.target.value);
  };
  const handleDescriptionChange = (e) => {
    setdescription(e.target.value);
  };

  const handleWebsiteChange = (e) => {
    setwebsite(e.target.value);
  };

  const handleUrlChange = (e) => {
    seturl(e.target.value);
  };
  const handleCategoryChange = (e) => {
    setcategory(e.target.value);
  };

  const onSubmit = (e) => {
    e.preventDefault();
    const new_website = { email, description, category, url, website };
    console.log(new_website);
    fetch('http://localhost:5000/api/public/submit/website', {
      method: 'POST',
      body: JSON.stringify(new_website),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((res) => res.json())
      .then((res) => {
        if (res) {
          setmessage(res);
        }
      })
      .catch((err) => console.log(err));
  };

  return (
    <form onSubmit={onSubmit}>
      <input
        type="text"
        placeholder="Enter Website Name e.g: example"
        name="website_name"
        value={website}
        onChange={handleWebsiteChange}
        required="required"
      />
      <input
        type="text"
        placeholder="Enter Website URL e.g: https://example.com"
        name="url"
        value={url}
        onChange={handleUrlChange}
        required="required"
      />
      <input
        type="email"
        placeholder="Enter Your Email"
        name="email"
        value={email}
        onChange={handleEmailChange}
        required="required"
      />
      <input
        type="text"
        placeholder="Enter Description"
        name="description"
        value={description}
        onChange={handleDescriptionChange}
      />
      <select
        className="category-selector"
        value={category}
        onChange={handleCategoryChange}
        name="category">
        {Categories.map((item, i) => (
          <option key={i}>{item.name}</option>
        ))}
      </select>
      {message ? <div className="success">Thanks for your submission</div> : ''}
      <input className="submit-btn" type="submit" />
    </form>
  );
};

export default Form;
