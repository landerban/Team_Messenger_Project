import React from 'react';
import '../css/navbar.css';
import OverlayAnimation from './OverlayAnimation';
import websiteLogo from '/vite.svg';

export default function NavBar({ isDark, isAnimating, toggleDark, toggleLan, isEng }) {
  return (
    <header className={isDark ? 'dark' : ''}>
      <nav className="navbar navbar-expand-lg navbar-dark bg-light-custom px-3">
        <a className="navbar-brand" href="#">
          <img src={websiteLogo} alt="Profile Icon" className="profile-icon" />
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <a className="nav-link" href="#">Home</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Chats</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">About Us</a>
            </li>
          </ul>
          <div className="d-flex align-items-center">
            <button className="btn btn-outline-light auth-button me-2">Log In</button>

            {/* Dark Mode Toggle Button */}
            <button
              className="btn btn-outline-light dark-mode me-2"
              onClick={toggleDark}
              disabled={isAnimating} // Disable button during animation
            >
              {isDark ? 'D' : 'L'}
            </button>

            {/* Overlay Animation */}
            <OverlayAnimation isAnimating={isAnimating} isDark={isDark} />

            {/* Language Toggle Button */}
            <button
              className="btn btn-outline-light auth-button me-2"
              onClick={toggleLan}
            >
              {isEng ? 'Eng' : 'Kor'}
            </button>
          </div>
        </div>
      </nav>
    </header>
  );
}
