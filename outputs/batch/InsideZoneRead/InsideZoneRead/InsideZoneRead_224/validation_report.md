# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_224`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_224/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 448: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [113-299] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-232] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-299] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-249] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-183] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-224] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-225] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [243-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [134-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-132] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-248] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-264] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '30' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.