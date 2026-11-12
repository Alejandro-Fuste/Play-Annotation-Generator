# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_26`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_26/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 35 |
| Ball Tracks | 2 |
| CSV events parsed | 20 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 95 frames exceeds threshold 90 frames [start=110, end=204].
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 111 frames exceeds threshold 90 frames [start=110, end=220].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 111 frames exceeds threshold 90 frames [start=110, end=220].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (LT) duration 111 frames exceeds threshold 90 frames [start=110, end=220].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [107–119], lower_priority='Action_ZoneBlock' annotated_start=110, effective_Action_ZoneBlock_start=120.
> - Action 'Action_SplitBlock' range [113-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [200-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-166] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-204] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-228] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-214] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-251] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [165-340] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [350-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-353] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-155] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-197] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-106] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-237] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-220] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-263] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-261] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [264-324] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-212] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-243] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-226] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-237] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-261] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-351] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-286] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-308] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [310-337] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-286] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-354] for track '34' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.