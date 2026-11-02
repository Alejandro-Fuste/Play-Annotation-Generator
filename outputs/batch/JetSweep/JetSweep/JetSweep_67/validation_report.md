# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_67`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [76–88], lower_priority='Action_ZoneBlock' annotated_start=77, effective_Action_ZoneBlock_start=89.
> - Segment 'Action_JetMotion' for track '20' has invalid range: start=117, end=105. Clamping end to start.
> - Action 'Action_BlockSecondLevel' range [103-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-114] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-118] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [76-127] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [77-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-130] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-30] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-73] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-115] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-115] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [117-164] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [173-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [187-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-167] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-209] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-221] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-259] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-269] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-240] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-251] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-259] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '30' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.