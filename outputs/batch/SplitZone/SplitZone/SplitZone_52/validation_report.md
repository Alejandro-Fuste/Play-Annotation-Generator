# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_52`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [93–107], lower_priority='Action_ZoneBlock' annotated_start=96, effective_Action_ZoneBlock_start=108.
> - Segment 'Action_ZoneBlock' for track '24' has invalid range: start=172, end=170. Clamping end to start.
> - Action 'Action_PreSnap' range [10-39] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-157] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-170] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-193] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-184] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-144] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-227] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-312] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [171-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-293] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-300] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-324] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-92] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-81] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [98-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-12] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-204] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-184] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-220] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-183] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-351] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '24' starts at frame 173, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [173-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-330] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [334-341] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-272] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-353] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-249] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-325] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-348] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-359] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-292] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-311] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-355] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-356] for track '37' has 4 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.