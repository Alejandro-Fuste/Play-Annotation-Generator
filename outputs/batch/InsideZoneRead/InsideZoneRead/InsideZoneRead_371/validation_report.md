# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_371`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_371/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 36 |
| Ball Tracks | 2 |
| CSV events parsed | 22 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 742: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [5-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-204] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-177] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-40] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-139] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-35] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-46] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-32] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '12' starts at frame 59, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [59-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [63-210] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [19-23] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-209] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-25] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-63] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-130] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '36' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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