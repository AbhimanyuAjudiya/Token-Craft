import "../Style/Card.css";

const Redeem = () => {
  const offers = [
    { title: "Unlock 10% off Odoo services", date: "Listed on 28/02/25", points: 10 },
    { title: "Exclusive 15% off ERP solutions", date: "Listed on 01/03/25", points: 15 },
    { title: "Get 20% off CRM upgrades", date: "Listed on 05/03/25", points: 20 },
    { title: "Save 10% on inventory tools", date: "Listed on 10/03/25", points: 10 },
    { title: "Special 25% off HR modules", date: "Listed on 15/03/25", points: 25 },
    { title: "Enjoy 10% off accounting software", date: "Listed on 20/03/25", points: 10 },
    { title: "Unlock 30% off eCommerce tools", date: "Listed on 25/03/25", points: 30 },
    { title: "Get 10% off project management", date: "Listed on 30/03/25", points: 10 },
    { title: "Save 15% on marketing tools", date: "Listed on 05/04/25", points: 15 },
    { title: "Exclusive 20% off analytics", date: "Listed on 10/04/25", points: 20 },
  ];

  return (
    <section className="Redeem-container">
      {offers.map((offer, index) => (
        <div className="Redeem-card" key={index}>
          <div className="Redeem-image"></div>
          <div className="Redeem-content">
            <h3 className="Redeem-title">{offer.title}</h3>
            <p className="Redeem-date">{offer.date}</p>
            <div className="Redeem-footer">
              <div className="Redeem-points">
                <div className="Redeem-circle">
                  <div className="Redeem-inner-circle"></div>
                </div>
                <span className="Redeem-points-value">{offer.points}</span>
              </div>
              <button className="Redeem-button">Redeem</button>
            </div>
          </div>
        </div>
      ))}
    </section>
  );
};

export default Redeem;
