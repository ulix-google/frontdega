import { useEffect, useState } from 'react';
import Tooltip from '@uiw/react-tooltip';
import './App.css';
import HeatMap from '@uiw/react-heat-map';
import { API } from './api/api';

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
    <div>
      <HeatMap
        value={heatMapData}
        weekLabels={['', 'Mon', '', 'Wed', '', 'Fri', '']}
        startDate={new Date('2022/09/01')}
        width={900}
        rectRender={(props, data) => {
          // if (!data.count) return <rect {...props} />;
          return (
            <Tooltip placement="top" content={`count: ${data.count || 0}`}>
              <rect {...props} />
            </Tooltip>
          );
        }}
      />
    </div>
  )
};

export default App;
