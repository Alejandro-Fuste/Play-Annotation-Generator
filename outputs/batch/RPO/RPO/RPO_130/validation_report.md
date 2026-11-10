# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_130`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_130/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 238: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [55-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-129] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-42] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-121] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-174] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 55, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [55-55] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-61] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-88] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-96] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [108-151] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-54] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-195] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.