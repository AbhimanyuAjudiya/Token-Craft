import React from "react";
import "../Style/HeroSection.css"; // Importing the CSS file
import Reward from "../assets/Reward.png"; // Import Reward image

const HeroSection = () => {
  return (
    <section className="hero-container">
      {/* Left Side - Hero Text */}
      <div className="hero-content">
        <h2 className="hero-greeting">Hey There 👋</h2>
        <h1 className="hero-heading">Good Afternoon</h1>
        <p className="hero-name">Jeet Patel</p>
      </div>

      {/* Right Side - Reward Cards */}
      <div className="reward-cards">
        {/* First Reward Card */}
        <div className="reward-card">
          <img src={Reward} alt="Badge" className="corner-img" />
          <p className="reward-title">Rewards</p>
          <h2 className="reward-amount">
            69<span className="small-decimal">.50</span>
          </h2>
        </div>

        {/* Second Reward Card */}
        <div className="reward-card">
          <img src={Reward} alt="Badge" className="corner-img" />
          <p className="reward-title">Bonus</p>
          <h2 className="reward-amount">
            32<span className="small-decimal">.75</span>
          </h2>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
