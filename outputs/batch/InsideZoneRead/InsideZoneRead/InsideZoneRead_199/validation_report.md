# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_199`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_199/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 32 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [26–41], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=42.
> - Action 'Action_None' range [26-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-82] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-239] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-66] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-80] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-124] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-122] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [72-84] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [124-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '10' starts at frame 42, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [42-61] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-105] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-229] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [94-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-214] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '32' has 2 frames without a visible bounding box.
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