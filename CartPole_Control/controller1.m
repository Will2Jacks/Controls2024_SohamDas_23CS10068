function u = controller1(X, params, X_desired) %#ok<*FNDEF>
    % Extract parameters from the params structure
    g = params.g;      % gravity
    M = params.M;      % mass of cart
    m = params.m;      % mass of pendulum
    L = params.L;      %#ok<*NASGU> % length of pendulum
    tol = 0.1;         % tolerance for stabilization
    
    % Extract current state variables
    x = X(1);       % cart position
    theta = X(3);   % pendulum angle
    
    % Extract desired state variables
    x_desired = X_desired(1);       % desired cart position
    theta_desired = 0;  % desired pendulum angle (upright position)
    
    % Controller gains

    Kp_theta = 25;
    Ki_theta = 0.175;
    Kd_theta = 60;
    
    % Calculate errors           
    error_theta = theta_desired - theta;  % error for pendulum angle
    
    % Define persistent variables for integral and previous error for cart position
   
    persistent integral_term_theta
    persistent prev_error_theta
    
    % Initialize integral term and previous error if not already initialized
    % if isempty(integral_term_x)
    %     integral_term_x = 0;
    %     prev_error_x = 0;
    % end
    if isempty(integral_term_theta)
        integral_term_theta = 0;
        prev_error_theta = 0;
    end
    
    % Update integral term for cart position
    % integral_term_x = integral_term_x + error_x;
    integral_term_theta = integral_term_theta + error_theta;
    
    % Compute control signal for cart position using PID control law
    % u_x = Kp_x * error_x + Ki_x * integral_term_x + Kd_x * (error_x - prev_error_x);
    u_theta = Kp_theta * error_theta + Ki_theta * integral_term_theta + Kd_theta * (error_theta - prev_error_theta);
    
    % Combine control signals for both cart position and pendulum angle
    u_combined =u_theta;
    
    % Apply anti-windup to the integral term
    if abs(u_combined) > 10  % If control signal saturates
        % integral_term_x = integral_term_x - error_x;  % Reset integral term
        integral_term_theta = integral_term_theta - error_theta;  % Reset integral term
    end
    
    % Update previous error for cart position

    prev_error_theta = error_theta;
    
    % Set the combined control signal
    u = u_combined;
end