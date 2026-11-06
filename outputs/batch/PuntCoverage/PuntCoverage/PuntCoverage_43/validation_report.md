# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_43`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-65] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-81] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-260] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-260] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-80] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-93] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-250] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-42] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-129] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-21] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-56] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-48] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-107] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-139] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-269] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-166] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-87] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-97] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-135] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-213] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-116] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-262] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-246] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-139] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-168] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-179] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-158] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-176] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-181] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-187] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-220] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-234] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-269] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-194] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-200] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-238] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-256] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-234] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-245] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '37' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.