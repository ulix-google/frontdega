import { useEffect, useState } from 'react';
import Tooltip from '@uiw/react-tooltip';
import './App.css';
import HeatMap from '@uiw/react-heat-map';
import { API } from './api/api';

document.body.style.backgroundColor = "#19ADED";

function App() {

  const [heatMapData, setHeatMapData] = useState([]);

  useEffect(() => {
    const fetchMessage = async () => {
      try {
        const response = await API.getTotalPullUps();
        console.log(response);
        setHeatMapData(response);
      } catch (error) {
        console.error(error);
      }
    }
    fetchMessage();
  }, []);

  return (
    <div
      style={{
        backgroundColor: '#EBDC5A',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}>
      <HeatMap
        value={heatMapData}
        weekLabels={['', 'Mon', '', 'Wed', '', 'Fri', '']}
        startDate={new Date('2022/09/01')}
        width={900}
        panelColors={{
          0: '#E8E7E7',
          1: '#ECDDDA',
          5: '#ECB0A5',
          10: '#EA7863',
          20: '#EA472A',
        }}
        rectRender={(props, data) => {
          return (
            <Tooltip placement="top" content={`${data.count || 0} pullups on ${data.date}`}>
              <rect {...props} />
            </Tooltip>
          );
        }}
      />
    </div>
  )
};

export default App;
