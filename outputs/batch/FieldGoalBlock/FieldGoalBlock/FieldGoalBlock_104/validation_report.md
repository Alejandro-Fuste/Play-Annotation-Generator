# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_104`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_104/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 210: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-26] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-43] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-52] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-75] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-145] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-64] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-96] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-114] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-50] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-148] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-185] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-233] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-127] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-41] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-91] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-38] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-129] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-148] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-67] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [30-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-168] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-234] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-14] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-242] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-11] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-37] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-64] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-95] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-67] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-166] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-218] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-252] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-124] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-105] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-164] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-231] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-115] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-125] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-135] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-269] for track '26' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [134-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-202] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-234] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-162] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-194] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-218] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-269] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-269] for track '32' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.