import "../Style/History.css";
import { FaClock } from "react-icons/fa"; // Importing clock icon

const History = () => {
  const transactions = [
    { date: "29/02/25", time: "10:15 AM", type: "Purchase", points: 10 },
    { date: "01/03/25", time: "02:30 PM", type: "Referral Bonus", points: 15 },
    { date: "05/03/25", time: "06:45 AM", type: "Points Redeemed", points: 5 },
    { date: "05/03/25", time: "06:45 AM", type: "Points Redeemed", points: 5 },
    { date: "05/03/25", time: "06:45 AM", type: "Points Redeemed", points: 5 },
    { date: "29/02/25", time: "10:15 AM", type: "Purchase", points: 10 },
    { date: "01/03/25", time: "02:30 PM", type: "Referral Bonus", points: 15 },
    { date: "05/03/25", time: "06:45 AM", type: "Points Redeemed", points: 5 },
        

    
  ];

  return (
    <section className="history-container">
      {transactions.map((transaction, index) => (
        <div className="history-card" key={index}>
          <div className="history-circle-wrap">
            <div className="history-outer-circle">
              <div className="history-inner-circle">{transaction.points}</div>
            </div>
          </div>
          <div className="history-card-content">
            <div className="history-transaction-info">
              <div className="history-info-item">
                <FaClock className="history-clock-icon" />
                <div className="history-info-text">
                  <span className="history-info-label">Time</span>
                  <span className="history-info-value">
                    {transaction.date}, {transaction.time}
                  </span>
                </div>
              </div>
              <div className="history-divider"></div> {/* Vertical Line */}
              <div className="history-info-item">
                <span className="history-info-label">Type</span>
                <span className="history-info-value">{transaction.type}</span>
              </div>
            </div>
            <button className="history-more-btn">More Info</button>
          </div>
        </div>
      ))}
    </section>
  );
};

export default History;
