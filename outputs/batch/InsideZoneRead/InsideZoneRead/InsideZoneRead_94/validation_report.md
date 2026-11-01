# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_94`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_94/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 31 |
| Ball Tracks | 2 |
| CSV events parsed | 19 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [109–127], lower_priority='Action_ZoneBlock' annotated_start=114, effective_Action_ZoneBlock_start=128.
> - Action 'Action_ZoneBlock' range [114-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-191] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-217] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-283] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-207] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [139-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [149-221] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-182] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [184-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-263] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-277] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-125] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-186] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-224] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-177] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-171] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [173-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-329] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-275] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-288] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-314] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-242] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-249] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-323] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-289] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-278] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-329] for track '28' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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