import jwt_decode from 'jwt-decode';

function jwtDecoder(token, param){
  var decodedToken = jwt_decode(token);
  return decodedToken[param];
};

export default jwtDecoder;