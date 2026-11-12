# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_310`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_310/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 622: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 622: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [33-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [43-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-129] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [116-241] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [55-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [77-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [139-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-169] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [171-176] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-165] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-50] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-269] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-66] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-99] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-196] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-77] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [33-46] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-67] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-130] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [33-91] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-138] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-217] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-168] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-197] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-150] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-151] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-171] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-183] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-204] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-262] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-220] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-241] for track '30' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [227-234] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-268] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [236-244] for track '32' has 3 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.