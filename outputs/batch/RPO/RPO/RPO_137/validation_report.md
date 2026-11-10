# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_137`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_137/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 248: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [46-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-117] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-199] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-237] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-54] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-72] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-128] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '21' starts at frame 47, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [47-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-39] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-55] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-121] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-134] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-173] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-227] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-197] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-218] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-235] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-194] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-238] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '36' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.