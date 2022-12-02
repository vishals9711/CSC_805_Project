import { Button, Card, Col, Input, Row, Skeleton, Statistic } from 'antd';
import React from 'react';
import { getPredictions } from '../services/cancerAPI';
import { PREDICTION_FEATURES } from './constants';

const Prediction = (): React.ReactElement => {
  const [inputValues, setInputValues] = React.useState({} as { [key: string]: string });
  const [prediction, setPrediction] = React.useState<null | number>(null);

  const handleGetPrediction = () => {
    setPrediction(null);
    setTimeout(() => {
      getPredictions(inputValues)
        .then((data) => setPrediction(data))
        .catch((err) => console.error(err));
    }, 1000);

  };

  return (
    <Row gutter={[16, 48]} justify={'center'}>
      {PREDICTION_FEATURES.map((data, index) => (
        <Col className='gutter-row' span={6} key={`${data}_${index}`}>
          <Input
            addonBefore={data.label}
            onChange={(e) =>
              setInputValues({
                ...inputValues,
                [data.key]: e.target.value,
              })
            }
          />
        </Col>
      ))}

      <Col className='gutter-row' span={24} style={{ marginTop: '3rem' }}>
        <Button size={'large'} onClick={handleGetPrediction}>
          Get Prediction
        </Button>
      </Col>
      <Col className='gutter-row' span={24} style={{ marginTop: '3rem' }}>
        <Card style={{ width: '300px', margin: 'auto' }}>
          {prediction === null ? (
            <Skeleton active round />
          ) : (
            <Statistic title='Prediction' value={prediction} precision={2} valueStyle={{ color: '#3f8600' }} />
          )}
        </Card>
      </Col>
    </Row>
  );
};

export default Prediction;
