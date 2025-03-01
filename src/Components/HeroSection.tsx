import "../Style/HeroSection.css"; // Importing the CSS file
import Reward from "../assets/Reward.png"; // Import Reward image
import Progress from "../assets/Progress.png";

const HeroSection = () => {
  return (
    <>
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
              $ 69<span className="small-decimal">.50</span>
            </h2>
          </div>

          {/* Second Reward Card */}
          <div className="reward-card">
            <img src={Progress} alt="Badge" className="corner-img" />
            <p className="reward-title"> Progress</p>
            <h2 className="reward-amount">32</h2>
          </div>
        </div>
      </section>

      {/* New Section */}
      <section className="new-section">
  <div className="main-card">
    <div className="main-card-content">
      <p className="main-card-title">
        Your Total <br /> Reward Balance :
      </p>
      <h2 className="main-reward-amount">
        $ 69<span className="small-decimal">.50</span>
      </h2>
    </div>
    <button className="redeem-button">
      Redeem Now <span className="arrow-icon">➝</span>
    </button>
  </div>
</section>
    </>
  );
};

export default HeroSection;
