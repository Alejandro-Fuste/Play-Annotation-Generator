# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_148`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_148/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (RG) duration 94 frames exceeds threshold 90 frames [start=82, end=175].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 101 frames exceeds threshold 90 frames [start=82, end=182].
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [80–90], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=91.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 101 frames exceeds threshold 90 frames [start=82, end=182].
> - Action 'Action_ZoneBlock' range [82-155] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-168] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-173] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-248] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [212-229] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-251] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-266] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-183] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-249] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-181] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-207] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-231] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-250] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-182] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-227] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-253] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [60-102] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [180-243] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-250] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-182] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-204] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-263] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-178] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-247] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-250] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-248] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-231] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-243] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-248] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-261] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-240] for track '32' has 2 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.