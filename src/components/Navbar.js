import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  useEffect(() => {
    btnEvent();
  }, []);

  const btnEvent = () => {
    let mainNav = document.getElementById('js-menu');
    let navBarToggle = document.getElementById('js-navbar-toggle');
    let navLink = document.querySelectorAll('.nav-links');

    navLink.forEach((btn) => {
      btn.addEventListener('click', () => {
        mainNav.classList.remove('active');
      });
    });

    navBarToggle.addEventListener('click', () => {
      mainNav.classList.toggle('active');
    });
  };

  return (
    <nav className="navbar bg-white">
      <span className="navbar-toggle" id="js-navbar-toggle">
        <i className="material-icons">menu</i>
      </span>
      <Link to="/" className="logo">
        Wayapplied
      </Link>
      <ul className="main-nav" id="js-menu">
        <li>
          <Link to="/" className="nav-links">
            browse
          </Link>
        </li>
        <li>
          <Link to="/about" className="nav-links">
            about
          </Link>
        </li>
        <li>
          <Link to="/submit" className="nav-links">
            submit
          </Link>
        </li>
      </ul>
      <div className="search">
        <i className="material-icons">search</i>
        <span>search</span>
      </div>
    </nav>
  );
};

export default Navbar;
