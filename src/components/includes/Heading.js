import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const Heading = () => {
  useEffect(() => {
    categoriesNames();
    categoryEvent();
  }, []);

  const [categories, setCategories] = useState([]);

  const categoryEvent = () => {
    let categoryBTN = document.getElementById('js-btn');
    let categoryBox = document.getElementById('js-categories-box');

    categoryBTN.addEventListener('click', () => {
      categoryBox.classList.toggle('boxactive');
    });
  };

  const categoriesNames = async () => {
    const data = await fetch(
      'http://localhost:5000/api/public/websites/categories'
    );
    const names = await data.json();
    setCategories(names);
  };

  return (
    <div className="heading-component">
      <h1 className="page-title">Explore Beautiful Websites</h1>
      <h2 className="page-discription">
        Showcase of Brilliant Homepages,Blogs and Landing Pages
      </h2>
      <button className="category-btn" id="js-btn">
        <span>categories</span>
        <i className="arrow"></i>
      </button>

      <div id="js-categories-box" className="categories-box">
        {categories.map((item, i) => (
          <Link className="category-item">
            <div key={i} className="box-item">
              {item.name}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Heading;
