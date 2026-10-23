# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_2`
- **Input XML**: `output_showcase_final/PuntBlock/PuntBlock_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 5: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureRecovery' for track '23' has invalid range: start=223, end=180. Clamping end to start.
> - Action 'Action_None' range [18-64] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-60] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-207] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-78] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-178] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-228] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-224] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-234] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [69-116] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [122-133] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [140-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-251] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-98] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-156] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-37] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-46] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-252] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-48] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-66] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-78] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-104] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-192] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-160] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-157] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-206] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-204] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-223] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-207] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-249] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-263] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-226] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-263] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-265] for track '43' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.