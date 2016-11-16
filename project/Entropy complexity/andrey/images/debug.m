% function stsim2 = stsim2(im1, im2, Nsc, Nor)
% Specify number of scales and orientations, window size
clear all;
close all;

Nor = 4;
Nsc = 3;

im1 = imread('01.tif');
im2 = imread('10.tif');

bands1 = get_pyramid_sub(im1, Nsc, Nor);
bands2 = get_pyramid_sub(im2, Nsc, Nor);

bands1n = get_pyramid_noSub(im1, Nsc, Nor);
bands2n = get_pyramid_noSub(im2, Nsc, Nor);

win = 7;

% Initialize maps for holding results, fill them in with results within one
% scale/orientation, i.e., with downsampling
maps{Nor*Nsc+3,Nor*(Nsc-1)+Nsc*(factorial(Nor)/factorial(2)/factorial(Nor-2))} = 0;

% Bandpasses
cntr = 1;
for scale = 1:Nsc
    for orient = 1:Nor
        im1 = bands1{scale,orient};
        im2 = bands2{scale,orient};
        maps{cntr,1} = compute_L_term((im1), (im2), win);
        maps{cntr,2} = compute_C_term((im1), (im2), win);
        maps{cntr,3} = compute_C01_term((im1), (im2), win);
        maps{cntr,4} = compute_C10_term((im1), (im2), win);
        cntr = cntr+1;
    end;
end;

cntr

% Lowpass
im1 = bands1{Nsc+1,1};
im2 = bands2{Nsc+1,1};
maps{cntr,1} = compute_L_term((im1), (im2), win);
maps{cntr,2} = compute_C_term((im1), (im2), win);
maps{cntr,3} = compute_C01_term((im1), (im2), win);
maps{cntr,4} = compute_C10_term((im1), (im2), win);

cntr = cntr+1;

% High pass
im1 = bands1{Nsc+2,1};
im2 = bands2{Nsc+2,1};
maps{cntr,1} = compute_L_term((im1), (im2), win);
maps{cntr,2} = compute_C_term((im1), (im2), win);
maps{cntr,3} = compute_C01_term((im1), (im2), win);
maps{cntr,4} = compute_C10_term((im1), (im2), win);
cntr = cntr+1;

% Compute cross correlation stuff that requires no downsampling
%% CORRECT THE CROSS STUFF!!!! (numbering)
cntc = 1;
for scale = 2:Nsc-1
    scale
    for orient=1:Nor

        im11 = abs(bands1n{scale-1,orient});
        im12 = abs(bands1n{scale,orient});

        im21 = abs(bands2n{scale-1,orient});
        im22 = abs(bands2n{scale,orient});

        maps{cntr,cntc} = compute_Cross_term(im11,im12,im21,im22,win);

        cntc = cntc+1;


        im13 = abs(bands1n{scale+1,orient});

        im23 = abs(bands2n{scale+1,orient});

        maps{cntr,cntc} = compute_Cross_term(im13,im12,im23,im22,win);


        cntc = cntc+1;

    end;

end


for scale=1:Nsc

    for orient=1:Nor-1

        im11 = abs(bands1n{scale,orient});

        im21 = abs(bands2n{scale,orient});

        for orient2=orient+1:Nor

            im13 = abs(bands1n{scale,orient2});

            im23 = abs(bands2n{scale,orient2});

            maps{cntr,cntc} = compute_Cross_term(im11,im13,im21,im23,win);


            cntc = cntc+1;

        end;

    end;

end;

% Me
stsim2 = compute_stsim_add_col_cross_lp(maps,0,1,0,[1:size(maps,2)],1);

% % Xiaonan
% stsim = compute_stsim_add_col_cross_lp(maps,0,1,0,[],1);
