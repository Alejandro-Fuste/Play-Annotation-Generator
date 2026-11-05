# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_99`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 131 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [81-328] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-218] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-629] for track '1' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [81-319] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-383] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-424] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-629] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-116] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-339] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-381] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [81-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-136] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-262] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-364] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-348] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-401] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-204] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-242] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-380] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-517] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [520-560] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-174] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-422] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-180] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-288] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-611] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-418] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-218] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-629] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-31] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-105] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-351] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-403] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-213] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-442] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-616] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-431] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [434-439] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-616] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-270] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [268-434] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [436-624] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-388] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-401] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-363] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-377] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-392] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-421] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [424-425] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-443] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-552] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-570] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [573-576] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-584] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [587-588] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-479] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [586-587] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-593] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [600-602] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [601-602] for track '40' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.