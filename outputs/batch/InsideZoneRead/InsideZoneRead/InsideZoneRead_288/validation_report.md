# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_288`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_288/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [71–79], lower_priority='Action_ZoneBlock' annotated_start=74, effective_Action_ZoneBlock_start=80.
> - Action 'Action_None' range [134-157] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-146] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-269] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [71-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-128] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-182] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-231] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [122-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-233] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-267] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-249] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-149] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-184] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-232] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-190] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-214] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-245] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-260] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-207] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-252] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-263] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '32' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.