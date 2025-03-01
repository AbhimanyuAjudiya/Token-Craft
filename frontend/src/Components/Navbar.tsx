import { useState, useRef, useEffect } from "react";
import "../Style/Navbar.css";

const Navbar = () => {
  const [activeTab, setActiveTab] = useState("Dashboard");
  const tabs = ["Dashboard", "My Rewards", "Redeem", "Achievement"];
  const navRefs = useRef([]);

  const [indicatorStyle, setIndicatorStyle] = useState({ left: 0, width: 0 });

  useEffect(() => {
    const activeIndex = tabs.indexOf(activeTab);
    if (navRefs.current[activeIndex]) {
      const { offsetLeft, offsetWidth } = navRefs.current[activeIndex];
      setIndicatorStyle({ left: offsetLeft, width: offsetWidth });
    }
  }, [activeTab]);

  return (
    <nav className="navbar">
      <ul className="nav-list">
        {tabs.map((tab, index) => (
          <li
            key={tab}
            ref={(el) => (navRefs.current[index] = el)}
            className={`nav-item ${activeTab === tab ? "active" : ""}`}
            onClick={() => setActiveTab(tab)}
          >
            {tab}
          </li>
        ))}
      </ul>
      <div className="indicator" style={{ left: indicatorStyle.left, width: indicatorStyle.width }} />
    </nav>
  );
};

export default Navbar;
