import React from 'react';
import { render } from 'react-dom';
import './public.css'; // ./public.css uses a special loader, refer to webpack config

import ReactApp from './reactApplication';

render(<ReactApp />, document.getElementById('app'));
