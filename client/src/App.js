import logo from './logo.svg';
import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [data, setData] = useState([])

  useEffect(() => {
    try {
    axios
      .get("http://127.0.0.1:8001/data")
      .then((res) => {
        setData(res.data)
      })
    } catch (error) {
      // Handle the error here
      setData([])
    }
  }, [])

  return (
    <div className='app-container'>
      <div className='app-heading'>Mutual Funds</div>
      <div className='app-subheading'>Annualized Data</div>
    <div className='tab'>
    <table className='table'>
      <thead>
        <tr>
          <th>Fund Name</th>
          <th>1_year</th>
          <th>2_year</th>
          <th>3_year</th>
          <th>7_year</th>
          <th>10_year</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item['fund']}>
            <td>{item['fund']}</td>
            <td>{item['1_year']}</td>
            <td>{item['2_year']}</td>
            <td>{item['3_year']}</td>
            <td>{item['7_year']}</td>
            <td>{item['10_year']}</td>
            
          </tr>
        ))}
      </tbody>
    </table>
    </div>
    </div>
  );
}

export default App;
