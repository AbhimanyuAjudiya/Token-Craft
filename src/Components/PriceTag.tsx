import "../Style/Pricetag.css"

const PriceTag = () => {
  return (
    <div className="price-tag">
      <div className="price-circle">
        <div className="price-inner-circle"></div>
      </div>
      <span className="price-amount">$60</span>
    </div>
  );
};

export default PriceTag;